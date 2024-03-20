from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.hr.appraisal.schemas import contact as schemas
from app.utils.deps import get_db
from  app.domains.crm.services.contact import contact_actions as actions


contact_router = APIRouter()


@contact_router.get("/contacts", response_model=List[schemas.ReviewPeriodSchema], tags=["contacts"])
def list_contacts(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    contacts = actions.get_all(db=db, skip=skip, limit=limit)
    return contacts


@contact_router.post(
    "/contacts", response_model=schemas.ReviewPeriodSchema, status_code=HTTP_201_CREATED, tags=["contacts"]
)
def create_contact(*, db: Session = Depends(get_db), contact_in: schemas.ReviewPeriodCreate) -> Any:
    contact = actions.create(db=db, obj_in=contact_in)
    return contact


@contact_router.put(
    "/contacts/{id}",
    response_model=schemas.ReviewPeriodSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["contacts"],
)
def update_contact(
    *, db: Session = Depends(get_db), id: UUID4, contact_in: schemas.ReviewPeriodUpdate,
) -> Any:
    contact = actions.get(db=db, id=id)
    if not contact:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="contact not found")
    contact = actions.update(db=db, db_obj=contact, obj_in=contact_in)
    return contact


@contact_router.get(
    "/contacts/{id}",
    response_model=schemas.ReviewPeriodSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["contacts"],
)
def get_contact(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    contact = actions.get(db=db, id=id)
    if not contact:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="contact not found")
    return contact


@contact_router.delete(
    "/contacts/{id}",
    response_model=schemas.ReviewPeriodSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["contacts"],
)
def delete_contact(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    contact = actions.get(db=db, id=id)
    if not contact:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="contact not found")
    contact = actions.remove(db=db, id=id)
    return contact