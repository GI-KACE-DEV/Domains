from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.hr.appraisal.schemas import staff_target as schemas
from app.utils.deps import get_db

from app.domains.hr.appraisal.services import staff_target_actions as actions


staff_target_router = APIRouter()


@staff_target_router.get("/staff_targets", response_model=List[schemas.StaffTargetSchema], tags=["staff_targets"])
def list_staff_targets(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    staff_targets = actions.get_all(db=db, skip=skip, limit=limit)
    return staff_targets


@staff_target_router.post(
    "/staff_targets", response_model=schemas.StaffTargetSchema, status_code=HTTP_201_CREATED, tags=["staff_targets"]
)
def create_staff_target(*, db: Session = Depends(get_db), staff_target_in: schemas.StaffTargetCreate) -> Any:    
    
    staff_target = actions.create(db=db, obj_in=staff_target_in)
    return staff_target


@staff_target_router.put(
    "/staff_targets/{id}",
    response_model=schemas.StaffTargetSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["staff_targets"],
)
def update_staff_target(
    *, db: Session = Depends(get_db), id: UUID4, staff_target_in: schemas.StaffTargetUpdate,
) -> Any:
    staff_target = actions.get(db=db, id=id)
    if not staff_target:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="staff_target not found")
    staff_target = actions.update(db=db, db_obj=staff_target, obj_in=staff_target_in)
    return staff_target


@staff_target_router.get(
    "/staff_targets/{id}",
    response_model=schemas.StaffTargetSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["staff_targets"],
)
def get_staff_target(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    staff_target = actions.get(db=db, id=id)
    if not staff_target:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="staff_target not found")
    return staff_target


@staff_target_router.delete(
    "/staff_targets/{id}",
    response_model=schemas.StaffTargetSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["staff_targets"],
)
def delete_staff_target(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    staff_target = actions.get(db=db, id=id)
    if not staff_target:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="staff_target not found")
    staff_target = actions.remove(db=db, id=id)
    return staff_target