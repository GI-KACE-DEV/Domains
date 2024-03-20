from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.crm.schemas import consultation as schemas
from app.utils.deps import get_db
from  app.domains.crm.services.consultation import consultation_actions as consultations


consultation_router = APIRouter()


@consultation_router.get("/consultations", response_model=List[schemas.ConsultationSchema], tags=["consultations"])
def list_consultations(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _consultations = consultations.get_all(db=db, skip=skip, limit=limit)
    return _consultations


@consultation_router.post(
    "/consultations", response_model=schemas.ConsultationSchema, status_code=HTTP_201_CREATED, tags=["consultations"]
)
def create_consultation(*, db: Session = Depends(get_db), consultation_in: schemas.ConsultationCreate) -> Any:
    consultation = consultations.create(db=db, obj_in=consultation_in)
    return consultation


@consultation_router.put(
    "/consultations/{id}",
    response_model=schemas.ConsultationSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["consultations"],
)
def update_consultation(
    *, db: Session = Depends(get_db), id: UUID4, consultation_in: schemas.ConsultationUpdate,
) -> Any:
    consultation = consultations.get(db=db, id=id)
    if not consultation:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="consultation not found")
    consultation = consultations.update(db=db, db_obj=consultation, obj_in=consultation_in)
    return consultation


@consultation_router.get(
    "/consultations/{id}",
    response_model=schemas.ConsultationSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["consultations"],
)
def get_consultation(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    consultation = consultations.get(db=db, id=id)
    if not consultation:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="consultation not found")
    return consultation


@consultation_router.delete(
    "/consultations/{id}",
    response_model=schemas.ConsultationSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["consultations"],
)
def delete_consultation(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    consultation = consultations.get(db=db, id=id)
    if not consultation:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="consultation not found")
    consultation = consultations.remove(db=db, id=id)
    return consultation