from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends,  HTTPException, APIRouter
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session
from datetime import datetime, date
from app.domains.hr.staff.services.staff import staff_actions as actions
from app.domains.hr.staff import schemas
from app.utils.deps import get_db
from fastapi.encoders import jsonable_encoder
import sys
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from app.domains.hr.staff.models import Staff
from app.domains.common.models.sector import Sector
from app.domains.common.models.practice_area import PracticeArea

staff_router = APIRouter()


@staff_router.get("/staffs", response_model=List[schemas.StaffSchema], tags=["staffs"])
def list_staffs(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    staffs = actions.get_all(db=db, skip=skip, limit=limit)
    return staffs


@staff_router.post(
    "/staffs", response_model=schemas.StaffSchema, status_code=HTTP_201_CREATED, tags=["staffs"]
)
def create_staff(*, db: Session = Depends(get_db), staff_in: schemas.StaffCreate) -> Any:
    # print(request.dict(exclude_none=True))

    staff_in_dict = staff_in.dict(exclude_unset=True)
    sector_ids = staff_in_dict.pop("sector_ids", [])
    practice_area_ids = staff_in_dict.pop("practice_area_ids", [])
    try:
        staff = Staff(**staff_in_dict)

        if sector_ids:
            sectors = db.query(Sector).filter(Sector.id.in_(sector_ids)).all()
            if sectors:
                staff.sectors.extend(sectors)

        if practice_area_ids:
            practice_areas = db.query(PracticeArea).filter(
                PracticeArea.id.in_(practice_area_ids))
            if practice_areas:
                staff.practice_areas.extend(practice_areas)
        db.add(staff)
        db.commit()
        db.refresh(staff)
        return staff

    except IntegrityError:
        db.rollback()
        # log error
        raise HTTPException(
            status_code=409, detail="{}".format(sys.exc_info()[1]))

    except:
        db.rollback()
        # log error
        raise HTTPException(status_code=500, detail="{}: {}".format(
            sys.exc_info()[0], sys.exc_info()[1]))


@staff_router.put(
    "/staffs/{id}",
    response_model=schemas.StaffSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["staffs"],
)
def update_staff(*, db: Session = Depends(get_db), id: UUID4,
                 staff_in: schemas.StaffUpdate) -> Any:
    try:
        staff = actions.get(db=db, id=id)
        if not staff:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND, detail="staff not found")
        _staff_in_dict = staff_in.dict()
        sector_ids = _staff_in_dict.pop("sector_ids", [])
        practice_area_ids = _staff_in_dict.pop("practice_area_ids", [])
        staff = actions.update(db=db, db_obj=staff, obj_in=staff_in)

        if staff:
            if sector_ids:
                sectors = db.query(Sector).filter(
                    Sector.id.in_(sector_ids)).all
                if sectors:
                    staff.sectors.extend(sectors)

                if practice_area_ids:
                    practice_areas = db.query(PracticeArea).filter(
                        PracticeArea.id.in_(practice_area_ids))
                    if practice_areas:
                        staff.practice_areas.extend(practice_areas)
        db.add(staff)
        db.commit()
        db.refresh(staff)
        return staff

    except KeyError:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="staffnot found")
    except IntegrityError:
        db.rollback()
        # log error
        raise HTTPException(
            status_code=409, detail="{}".format(sys.exc_info()[1]))
    except:
        db.rollback()
        # log error
        raise HTTPException(status_code=500, detail="{}: {}".format(
            sys.exc_info()[0], sys.exc_info()[1]))


@staff_router.get(
    "/staffs/{id}",
    response_model=schemas.StaffSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["staffs"],
)
def get_staff(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    staff = actions.get(db=db, id=id)
    if not staff:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="staff not found")
    return staff


@staff_router.delete(
    "/staffs/{id}",
    response_model=schemas.StaffSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["staffs"],
)
def delete_staff(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    staff = actions.get(db=db, id=id)
    if not staff:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="staff not found")
    staff = actions.remove(db=db, id=id)
    return staff


@staff_router.get(
    "/staffs/{id}",
    response_model=schemas.StaffSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["staffs"],
)
def get_staff(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    staff = actions.get(db=db, id=id)
    if not staff:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="staff not found")
    return staff


# add sectors


@staff_router.put("/staffs/{staff_id}/addsectors",
                  response_model=schemas.StaffSchema,
                  tags=["staff"])
def remove_staff_sectors(*, db: Session = Depends(get_db), staff_id: UUID4,
                         related_object: schemas.RelatedObject) -> Any:
    sector_ids = related_object.ids
    return actions.remove_sectors(staff_id, db, sector_ids)


@staff_router.put("/staffs/{staff_id}/addsectorwww",
                  response_model=schemas.StaffSchema,
                  tags=["staff"])
def add_staff_sectors(*, db: Session = Depends(get_db), staff_id: UUID4,
                      related_object: schemas.RelatedObject) -> Any:
    return actions.add_sectors(staff_id, db, related_object)

# remove sectors


# add  practice_areas

# remove practice_areas
