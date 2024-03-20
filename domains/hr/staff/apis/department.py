from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.hr.staff.services.department import department_actions as actions
from app.domains.hr.staff import schemas
from app.utils.deps import get_db

from fastapi import APIRouter, Depends

department_router = APIRouter()


@department_router.get("/departments", response_model=List[schemas.DepartmentSchema], tags=["departments"])
def list_departments(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    departments = actions.get_all(db=db, skip=skip, limit=limit)
    return departments


@department_router.post(
    "/departments", response_model=schemas.DepartmentSchema, status_code=HTTP_201_CREATED, tags=["departments"]
)
def create_Department(*, db: Session = Depends(get_db), Department_in: schemas.DepartmentCreate) -> Any:
    Department = actions.create(db=db, obj_in=Department_in)
    return Department


@department_router.put(
    "/departments/{id}",
    response_model=schemas.DepartmentSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["departments"],
)
def update_Department(
    *, db: Session = Depends(get_db), id: UUID4, department_in: schemas.DepartmentUpdate,
) -> Any:
    department = actions.get(db=db, id=id)
    if not department:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Department not found")
    department = actions.update(db=db, db_obj=department, obj_in=department_in)
    return department


@department_router.get(
    "/departments/{id}",
    response_model=schemas.DepartmentSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["departments"],
)
def get_department(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    Department = actions.get(db=db, id=id)
    if not Department:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Department not found")
    return Department


@department_router.delete(
    "/departments/{id}",
    response_model=schemas.DepartmentSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["departments"],
)
def delete_Department(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    Department = actions.get(db=db, id=id)
    if not Department:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Department not found")
    Department = actions.remove(db=db, id=id)
    return Department
