from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.hr.appraisal.schemas import staff_appraisal as schemas
from app.utils.deps import get_db
from app.domains.hr.appraisal.services import staff_appraisal_actions as actions


staff_appraisal_router = APIRouter()


@staff_appraisal_router.get("/staff_appraisals", response_model=List[schemas.StaffAppraisalSchema], tags=["staff_appraisals"])
def list_staff_appraisals(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    staff_appraisals = actions.get_all(db=db, skip=skip, limit=limit)
    return staff_appraisals


@staff_appraisal_router.post(
    "/staff_appraisals", response_model=schemas.StaffAppraisalSchema, status_code=HTTP_201_CREATED, tags=["staff_appraisals"]
)
def create_staff_appraisal(*, db: Session = Depends(get_db), staff_appraisal_in: schemas.StaffAppraisalCreate) -> Any:
    staff_appraisal = actions.create(db=db, obj_in=staff_appraisal_in)
    return staff_appraisal


@staff_appraisal_router.put(
    "/staff_appraisals/{id}",
    response_model=schemas.StaffAppraisalSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["staff_appraisals"],
)
def update_staff_appraisal(
    *, db: Session = Depends(get_db), id: UUID4, staff_appraisal_in: schemas.StaffAppraisalUpdate,
) -> Any:
    staff_appraisal = actions.staff_appraisal.get(db=db, id=id)
    if not staff_appraisal:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="staff_appraisal not found")
    staff_appraisal = actions.update(db=db, db_obj=staff_appraisal, obj_in=staff_appraisal_in)
    return staff_appraisal


@staff_appraisal_router.get(
    "/staff_appraisals/{id}",
    response_model=schemas.StaffAppraisalSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["staff_appraisals"],
)
def get_staff_appraisal(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    staff_appraisal = actions.get(db=db, id=id)
    if not staff_appraisal:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="staff_appraisal not found")
    return staff_appraisal


@staff_appraisal_router.delete(
    "/staff_appraisals/{id}",
    response_model=schemas.StaffAppraisalSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["staff_appraisals"],
)
def delete_staff_appraisal(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    staff_appraisal = actions.get(db=db, id=id)
    if not staff_appraisal:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="staff_appraisal not found")
    staff_appraisal = actions.remove(db=db, id=id)
    return staff_appraisal