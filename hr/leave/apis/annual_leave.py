from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session
from app.utils.deps import get_db

from app.domains.hr.staff.models import Staff
from app.domains.hr.leave.models.annual_leave import LeaveType
from app.domains.hr.leave.schemas.annual_leave import ( AnnualLeaveSchema, 
    AnnualLeaveUpdate, AnnualLeaveCreate, HTTPError)

from  app.domains.hr.leave.services.annual_leave import annual_leave_actions as annual_leaves


annual_leave_router = APIRouter()

@annual_leave_router.get("/annual_leaves", response_model=List[AnnualLeaveSchema], tags=["annual_leaves"])
def list_annual_leaves(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _annual_leaves = annual_leaves.get_all(db=db, skip=skip, limit=limit)
    return _annual_leaves


@annual_leave_router.post(
    "/annual_leaves", response_model=AnnualLeaveSchema, status_code=HTTP_201_CREATED, tags=["annual_leaves"]
)
def create_annual_leave(*, db: Session = Depends(get_db), annual_leave_in: AnnualLeaveCreate) -> Any:
    
    #related objects constraint
    staff = db.query(Staff).filter(Staff.id == annual_leave.staff_id).first()
    annual_leave = db.query(LeaveType).filter(LeaveType.id == annual_leave.annual_leave_id).first()
    if not staff or not annual_leave:
        raise HTTPException(status_code=404, detail="Staff or leave type not found")
    
    annual_leave = annual_leaves.create(db=db, obj_in=annual_leave_in)
    return annual_leave


@annual_leave_router.put(
    "/annual_leaves/{id}",
    response_model=AnnualLeaveSchema,
    responses={HTTP_404_NOT_FOUND: {"model": HTTPError}},
    tags=["annual_leaves"],
)
def update_annual_leave(
    *, db: Session = Depends(get_db), id: UUID4, annual_leave_in: AnnualLeaveUpdate,
) -> Any:
    annual_leave = annual_leaves.get(db=db, id=id)
    if not annual_leave:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="annual_leave not found")
    annual_leave = annual_leaves.update(db=db, db_obj=annual_leave, obj_in=annual_leave_in)
    return annual_leave


@annual_leave_router.get(
    "/annual_leaves/{id}",
    response_model=AnnualLeaveSchema,
    responses={HTTP_404_NOT_FOUND: {"model": HTTPError}},
    tags=["annual_leaves"],
)
def get_annual_leave(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    annual_leave = annual_leaves.get(db=db, id=id)
    if not annual_leave:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="annual_leave not found")
    return annual_leave


@annual_leave_router.delete(
    "/annual_leaves/{id}",
    response_model=AnnualLeaveSchema,
    responses={HTTP_404_NOT_FOUND: {"model": HTTPError}},
    tags=["annual_leaves"],
)
def delete_annual_leave(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    annual_leave = annual_leaves.get(db=db, id=id)
    if not annual_leave:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="annual_leave not found")
    annual_leave = annual_leaves.remove(db=db, id=id)
    return annual_leave