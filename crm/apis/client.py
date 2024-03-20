from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.crm.schemas import client as schemas
from app.utils.deps import get_db
from  app.domains.crm.services.client import client_actions as clients


client_router = APIRouter()


@client_router.get("/clients", response_model=List[schemas.ClientSchema], tags=["clients"])
def list_clients(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _clients = clients.get_all(db=db, skip=skip, limit=limit)
    return _clients


@client_router.post(
    "/clients", response_model=schemas.ClientSchema, status_code=HTTP_201_CREATED, tags=["clients"]
)
def create_client(*, db: Session = Depends(get_db), client_in: schemas.ClientCreate) -> Any:
    client = clients.create(db=db, obj_in=client_in)
    return client


@client_router.put(
    "/clients/{id}",
    response_model=schemas.ClientSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["clients"],
)
def update_client(
    *, db: Session = Depends(get_db), id: UUID4, client_in: schemas.ClientUpdate,
) -> Any:
    client = clients.get(db=db, id=id)
    if not client:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="client not found")
    client = clients.update(db=db, db_obj=client, obj_in=client_in)
    return client


@client_router.get(
    "/clients/{id}",
    response_model=schemas.ClientSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["clients"],
)
def get_client(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    client = clients.get(db=db, id=id)
    if not client:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="client not found")
    return client


@client_router.delete(
    "/clients/{id}",
    response_model=schemas.ClientSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["clients"],
)
def delete_client(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    client = clients.get(db=db, id=id)
    if not client:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="client not found")
    client = clients.remove(db=db, id=id)
    return client