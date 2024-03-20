from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.officemanager.schemas import dispatches as schemas
from app.utils.deps import get_db
from  app.domains.officemanager.services.dispatches import incoming_actions as incomings
from  app.domains.officemanager.services.dispatches import outgoing_actions as outgoings


dispatch_router = APIRouter(prefix="/dispatches")


@dispatch_router.get("/incomings", response_model=List[schemas.IncomingSchema], tags=["incomings"])
def list_incomings(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _incomings = incomings.get_all(db=db, skip=skip, limit=limit)
    return _incomings


@dispatch_router.post(
    "/incomings", response_model=schemas.IncomingSchema, status_code=HTTP_201_CREATED, tags=["incomings"]
)
def create_incoming(*, db: Session = Depends(get_db), incoming_in: schemas.IncomingCreate) -> Any:
    _incoming = incomings.create(db=db, obj_in=incoming_in)
    return _incoming


@dispatch_router.put(
    "/incomings/{id}",
    response_model=schemas.IncomingSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["incomings"],
)
def update_incoming(
    *, db: Session = Depends(get_db), id: UUID4, incoming_in: schemas.IncomingUpdate,
) -> Any:
    _incoming = incomings.incoming.get(db=db, id=id)
    if not _incoming:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="incoming not found")
    _incoming = incomings.update(db=db, db_obj=_incoming, obj_in=incoming_in)
    return incoming


@dispatch_router.get(
    "/incomings/{id}",
    response_model=schemas.IncomingSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["incomings"],
)
def get_incoming(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _incoming = incomings.get(db=db, id=id)
    if not _incoming:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="incoming not found")
    return incoming


@dispatch_router.delete(
    "/incomings/{id}",
    response_model=schemas.IncomingSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["incomings"],
)
def delete_incoming(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _incoming = incomings.get(db=db, id=id)
    if not _incoming:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="incoming not found")
    _incoming = _incomings.remove(db=db, id=id)
    return _incoming


# outgoings
@dispatch_router.get("/outgoings", response_model=List[schemas.OutgoingSchema], tags=["outgoings"])
def list_outgoings(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _outgoings = outgoings.get_all(db=db, skip=skip, limit=limit)
    return _outgoings


@dispatch_router.post(
    "/outgoings", response_model=schemas.OutgoingSchema, status_code=HTTP_201_CREATED, tags=["outgoings"]
)
def create_outgoing(*, db: Session = Depends(get_db), outgoing_in: schemas.OutgoingCreate) -> Any:
    _outgoing = outgoings.create(db=db, obj_in=outgoing_in)
    return _outgoing


@dispatch_router.put(
    "/outgoings/{id}",
    response_model=schemas.OutgoingSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["outgoings"],
)
def update_outgoing(
    *, db: Session = Depends(get_db), id: UUID4, outgoing_in: schemas.OutgoingUpdate,
) -> Any:
    _outgoing = outgoings.outgoing.get(db=db, id=id)
    if not _outgoing:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="outgoing not found")
    _outgoing = _outgoings.update(db=db, db_obj=outgoing, obj_in=outgoing_in)
    return _outgoing


@dispatch_router.get(
    "/outgoings/{id}",
    response_model=schemas.OutgoingSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["outgoings"],
)
def get_outgoing(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    outgoing = outgoings.get(db=db, id=id)
    if not outgoing:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="outgoing not found")
    return outgoing


@dispatch_router.delete(
    "/outgoings/{id}",
    response_model=schemas.OutgoingSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["outgoings"],
)
def delete_outgoing(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    outgoing = outgoings.get(db=db, id=id)
    if not outgoing:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="outgoing not found")
    outgoing = outgoings.remove(db=db, id=id)
    return outgoing

