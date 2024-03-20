from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.hr.appraisal.schemas import department_target as schemas
from app.utils.deps import get_db
from app.domains.hr.appraisal.services import department_target_actions as actions


department_target_router = APIRouter(prefix="")


@department_target_router.get("/department_targets", response_model=List[schemas.DepartmentTargetSchema], tags=["department_targets"])
def list_department_targets(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    department_targets = actions.get_all(db=db, skip=skip, limit=limit)
    return department_targets


@department_target_router.post(
    "/department_targets", response_model=schemas.DepartmentTargetSchema, status_code=HTTP_201_CREATED, tags=["department_targets"]
)
def create_department_target(*, db: Session = Depends(get_db), department_target_in: schemas.DepartmentTargetCreate) -> Any:
    department_target = actions.create(db=db, obj_in=department_target_in)
    return department_target


@department_target_router.put(
    "/department_targets/{id}",
    response_model=schemas.DepartmentTargetSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["department_targets"],
)
def update_department_target(
    *, db: Session = Depends(get_db), id: UUID4, department_target_in: schemas.DepartmentTargetUpdate,
) -> Any:
    department_target = actions.get(db=db, id=id)
    if not department_target:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="department_target not found")
    department_target = actions.update(db=db, db_obj=department_target, obj_in=department_target_in)
    return department_target


@department_target_router.get(
    "/department_targets/{id}",
    response_model=schemas.DepartmentTargetSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["department_targets"],
)
def get_department_target(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    department_target = actions.get(db=db, id=id)
    if not department_target:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="department_target not found")
    return department_target


@department_target_router.delete(
    "/department_targets/{id}",
    response_model=schemas.DepartmentTargetSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["department_targets"],
)
def delete_department_target(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    department_target = actions.get(db=db, id=id)
    if not department_target:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="department_target not found")
    department_target = actions.remove(db=db, id=id)
    return department_target