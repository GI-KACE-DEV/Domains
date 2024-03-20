from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.hr.appraisal.schemas import firm_target as schemas
from app.utils.deps import get_db
from app.domains.hr.appraisal.services import firm_target_actions as actions


firm_target_router = APIRouter(prefix="/hr")


@firm_target_router.get("/firm_targets", response_model=List[schemas.FirmTargetSchema], tags=["firm_targets"])
def list_firm_targets(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    firm_targets = actions.get_all(db=db, skip=skip, limit=limit)
    return firm_targets


@firm_target_router.post(
    "/firm_targets", response_model=schemas.FirmTargetSchema, status_code=HTTP_201_CREATED, tags=["firm_targets"]
)
def create_firm_target(*, db: Session = Depends(get_db), firm_target_in: schemas.FirmTargetCreate) -> Any:
    firm_target = actions.create(db=db, obj_in=firm_target_in)
    return firm_target


@firm_target_router.put(
    "/firm_targets/{id}",
    response_model=schemas.FirmTargetSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["firm_targets"],
)
def update_firm_target(
    *, db: Session = Depends(get_db), id: UUID4, firm_target_in: schemas.FirmTargetUpdate,
) -> Any:
    firm_target = actions.get(db=db, id=id)
    if not firm_target:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="firm_target not found")
    firm_target = actions.firm_target.update(db=db, db_obj=firm_target, obj_in=firm_target_in)
    return firm_target


@firm_target_router.get(
    "/firm_targets/{id}",
    response_model=schemas.FirmTargetSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["firm_targets"],
)
def get_firm_target(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    firm_target = actions.get(db=db, id=id)
    if not firm_target:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="firm_target not found")
    return firm_target


@firm_target_router.delete(
    "/firm_targets/{id}",
    response_model=schemas.FirmTargetSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["firm_targets"],
)
def delete_firm_target(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    firm_target = actions.firm_target.get(db=db, id=id)
    if not firm_target:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="firm_target not found")
    firm_target = actions.remove(db=db, id=id)
    return firm_target