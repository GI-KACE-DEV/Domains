
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.hr.staff.services.designation import designation_actions as actions
from app.domains.hr.staff import schemas
from app.utils.deps import get_db

from fastapi import APIRouter, Depends

designation_router = APIRouter()


@designation_router.get("/designations", response_model=List[schemas.DesignationSchema], tags=["designations"])
def list_designations(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    designations = actions.get_all(db=db, skip=skip, limit=limit)
    return designations


@designation_router.post(
    "/designations", response_model=schemas.DesignationSchema, status_code=HTTP_201_CREATED, tags=["designations"]
)
def create_designation(*, db: Session = Depends(get_db), designation_in: schemas.DesignationCreate) -> Any:
    designation= actions.create(db=db, obj_in=designation_in)
    return designation


@designation_router.put(
    "/designations/{id}",
    response_model=schemas.DesignationSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["designations"],
)
def update_designation(
    *, db: Session = Depends(get_db), id: UUID4, designation_in: schemas.DesignationUpdate,
) -> Any:
    designation= actions.get(db=db, id=id)
    if not designation:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Designationnot found")
    designation= actions.update(db=db, db_obj=designation, obj_in=designation_in)
    return designation


@designation_router.get(
    "/designations/{id}",
    response_model=schemas.DesignationSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["designations"],
)
def get_designation(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    designation= actions.get(db=db, id=id)
    if not designation:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="designationnot found")
    return designation


@designation_router.delete(
    "/designations/{id}",
    response_model=schemas.DesignationSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["designations"],
)
def delete_designation(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    designation= actions.get(db=db, id=id)
    if not designation:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="designationnot found")
    designation= actions.remove(db=db, id=id)
    return designation