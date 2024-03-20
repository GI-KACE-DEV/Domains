from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.crm.schemas import lead as schemas
from app.utils.deps import get_db
from  app.domains.crm.services.lead import lead_actions as leads


lead_router = APIRouter()


@lead_router.get("/leads", response_model=List[schemas.LeadSchema], tags=["leads"])
def list_leads(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _leads = leads.get_all(db=db, skip=skip, limit=limit)
    return _leads


@lead_router.post(
    "/leads", response_model=schemas.LeadSchema, status_code=HTTP_201_CREATED, tags=["leads"]
)
def create_lead(*, db: Session = Depends(get_db), lead_in: schemas.LeadCreate) -> Any:
    _lead = leads.create(db=db, obj_in=lead_in)
    return _lead


@lead_router.put(
    "/leads/{id}",
    response_model=schemas.LeadSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["leads"],
)
def update_lead(
    *, db: Session = Depends(get_db), id: UUID4, lead_in: schemas.LeadUpdate,
) -> Any:
    lead = leads.get(db=db, id=id)
    if not lead:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="lead not found")
    lead = leads.update(db=db, db_obj=lead, obj_in=lead_in)
    return lead


@lead_router.get(
    "/leads/{id}",
    response_model=schemas.LeadSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["leads"],
)
def get_lead(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    lead = leads.get(db=db, id=id)
    if not lead:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="lead not found")
    return lead


@lead_router.delete(
    "/leads/{id}",
    response_model=schemas.LeadSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["leads"],
)
def delete_lead(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    lead = leads.get(db=db, id=id)
    if not lead:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="lead not found")
    lead = leads.remove(db=db, id=id)
    return lead