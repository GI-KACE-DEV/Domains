from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.utils.deps import get_db
from app.domains.hr.leave.models.leave import Leave
from app.domains.hr.leave.schemas.leave import ( LeaveSchema, 
    LeaveUpdate, LeaveCreate, HTTPError)
from  app.domains.hr.leave.services.leave import leave_actions as leaves

leave_router = APIRouter()


@leave_router.get("/leaves", response_model=List[LeaveSchema], tags=["leaves"])
def list_leaves(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _leaves = leaves.get_all(db=db, skip=skip, limit=limit)
    return _leaves


@leave_router.post(
    "/leaves", response_model=LeaveSchema, status_code=HTTP_201_CREATED, tags=["leaves"]
)
def create_leave(*, db: Session = Depends(get_db), leave_in: LeaveCreate) -> Any:
    
    #related objects constraint
    staff = db.query(Staff).filter(Staff.id == leave.staff_id).first()
    leave = db.query(Leave).filter(Leave.id == leave.leave_id).first()
    if not staff or not leave:
        raise HTTPException(status_code=404, detail="Staff or leave type not found")
    
    leave = leaves.create(db=db, obj_in=leave_in)
    return leave


@leave_router.put(
    "/leaves/{id}",
    response_model=LeaveSchema,
    responses={HTTP_404_NOT_FOUND: {"model": HTTPError}},
    tags=["leaves"],
)
def update_leave(
    *, db: Session = Depends(get_db), id: UUID4, leave_in: LeaveUpdate,
) -> Any:
    leave = leaves.get(db=db, id=id)
    if not leave:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="leave not found")
    leave = leaves.update(db=db, db_obj=leave, obj_in=leave_in)
    return leave


@leave_router.get(
    "/leaves/{id}",
    response_model=LeaveSchema,
    responses={HTTP_404_NOT_FOUND: {"model": HTTPError}},
    tags=["leaves"],
)
def get_leave(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    leave = leaves.get(db=db, id=id)
    if not leave:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="leave not found")
    return leave


@leave_router.delete(
    "/leaves/{id}",
    response_model=LeaveSchema,
    responses={HTTP_404_NOT_FOUND: {"model": HTTPError}},
    tags=["leaves"],
)
def delete_leave(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    leave = leaves.get(db=db, id=id)
    if not leave:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="leave not found")
    leave = leaves.remove(db=db, id=id)
    return leave