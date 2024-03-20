from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.hr.appraisal.schemas import department_appraisal as schemas
from app.utils.deps import get_db
from app.domains.hr.appraisal.services.department_appraisal import department_appraisal_actions as actions


department_appraisal_router = APIRouter()


@department_appraisal_router.get("/department_appraisals", response_model=List[schemas.DepartmentAppraisalSchema], tags=["department_appraisals"])
def list_department_appraisals(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    department_appraisals = actions.get_all(db=db, skip=skip, limit=limit)
    return department_appraisals


@department_appraisal_router.post(
    "/department_appraisals", response_model=schemas.DepartmentAppraisalSchema, status_code=HTTP_201_CREATED, tags=["department_appraisals"]
)
def create_department_appraisal(*, db: Session = Depends(get_db), department_appraisal_in: schemas.DepartmentAppraisalCreate) -> Any:
    department_appraisal = actions.create(db=db, obj_in=department_appraisal_in)
    return department_appraisal


@department_appraisal_router.put(
    "/department_appraisals/{id}",
    response_model=schemas.DepartmentAppraisalSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["department_appraisals"],
)
def update_department_appraisal(
    *, db: Session = Depends(get_db), id: UUID4, department_appraisal_in: schemas.DepartmentAppraisalUpdate,
) -> Any:
    department_appraisal = actions.department_appraisal.get(db=db, id=id)
    if not department_appraisal:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="department_appraisal not found")
    department_appraisal = actions.update(db=db, db_obj=department_appraisal, obj_in=department_appraisal_in)
    return department_appraisal


@department_appraisal_router.get(
    "/department_appraisals/{id}",
    response_model=schemas.DepartmentAppraisalSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["department_appraisals"],
)
def get_department_appraisal(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    department_appraisal = actions.get(db=db, id=id)
    if not department_appraisal:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="department_appraisal not found")
    return department_appraisal


@department_appraisal_router.delete(
    "/department_appraisals/{id}",
    response_model=schemas.DepartmentAppraisalSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["department_appraisals"],
)
def delete_department_appraisal(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    department_appraisal = actions.get(db=db, id=id)
    if not department_appraisal:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="department_appraisal not found")
    department_appraisal = actions.remove(db=db, id=id)
    return department_appraisal