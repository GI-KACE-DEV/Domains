from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.utils.deps import get_db

from app.domains.hr.staff.models import Staff

from app.domains.hr.leave.models.leave_type import LeaveType
from app.domains.hr.leave.schemas.leave_type import ( LeaveTypeSchema, 
    LeaveTypeUpdate, LeaveTypeCreate, HTTPError)
from  app.domains.hr.leave.services.leave_type import leave_type_actions as leave_types

leave_type_router = APIRouter()



@leave_type_router.get("/leave_types", response_model=List[LeaveTypeSchema], tags=["leave_types"])
def list_leave_types(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _leave_types = leave_types.get_all(db=db, skip=skip, limit=limit)
    return _leave_types


@leave_type_router.post(
    "/leave_types", response_model=LeaveTypeSchema, status_code=HTTP_201_CREATED, tags=["leave_types"]
)
def create_leave_type(*, db: Session = Depends(get_db), leave_type_in: LeaveTypeCreate) -> Any:
    
    #related objects constraint
    #staff = db.query(Staff).filter(Staff.id == leave_type.staff_id).first()
   # leave_type = db.query(LeaveType).filter(LeaveType.id == leave_type.leave_type_id).first()
    #if not staff or not leave_type:
    #    raise HTTPException(status_code=404, detail="Staff or leave type not found")
    
    leave_type = leave_types.create(db=db, obj_in=leave_type_in)
    return leave_type


@leave_type_router.put(
    "/leave_types/{id}",
    response_model=LeaveTypeSchema,
    responses={HTTP_404_NOT_FOUND: {"model": HTTPError}},
    tags=["leave_types"],
)
def update_leave_type(
    *, db: Session = Depends(get_db), id: UUID4, leave_type_in: LeaveTypeUpdate,
) -> Any:
    leave_type = leave_types.get(db=db, id=id)
    if not leave_type:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="leave_type not found")
    leave_type = leave_types.update(db=db, db_obj=leave_type, obj_in=leave_type_in)
    return leave_type


@leave_type_router.get(
    "/leave_types/{id}",
    response_model=LeaveTypeSchema,
    responses={HTTP_404_NOT_FOUND: {"model": HTTPError}},
    tags=["leave_types"],
)
def get_leave_type(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    leave_type = leave_types.get(db=db, id=id)
    if not leave_type:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="leave_type not found")
    return leave_type


@leave_type_router.delete(
    "/leave_types/{id}",
    response_model=LeaveTypeSchema,
    responses={HTTP_404_NOT_FOUND: {"model": HTTPError}},
    tags=["leave_types"],
)
def delete_leave_type(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    leave_type = leave_types.get(db=db, id=id)
    if not leave_type:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="leave_type not found")
    leave_type = leave_types.remove(db=db, id=id)
    return leave_type