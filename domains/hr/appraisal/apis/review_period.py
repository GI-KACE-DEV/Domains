from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.hr.appraisal.schemas import review_period as schemas
from app.utils.deps import get_db
from app.domains.hr.appraisal.services import review_period_actions as actions


review_period_router = APIRouter(prefix="")


@review_period_router.get("/review_periods", response_model=List[schemas.ReviewPeriodSchema], tags=["review_periods"])
def list_review_periods(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    review_periods = actions.get_all(db=db, skip=skip, limit=limit)
    return review_periods


@review_period_router.post(
    "/review_periods", response_model=schemas.ReviewPeriodSchema, status_code=HTTP_201_CREATED, tags=["review_periods"]
)
def create_review_period(*, db: Session = Depends(get_db), review_period_in: schemas.ReviewPeriodCreate) -> Any:
    review_period = actions.create(db=db, obj_in=review_period_in)
    return review_period


@review_period_router.put(
    "/review_periods/{id}",
    response_model=schemas.ReviewPeriodSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["review_periods"],
)
def update_review_period(
    *, db: Session = Depends(get_db), id: UUID4, review_period_in: schemas.ReviewPeriodUpdate,
) -> Any:
    review_period = actions.get(db=db, id=id)
    if not review_period:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="review_period not found")
    review_period = actions.update(db=db, db_obj=review_period, obj_in=review_period_in)
    return review_period


@review_period_router.get(
    "/review_periods/{id}",
    response_model=schemas.ReviewPeriodSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["review_periods"],
)
def get_review_period(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    review_period = actions.get(db=db, id=id)
    if not review_period:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="review_period not found")
    return review_period


@review_period_router.delete(
    "/review_periods/{id}",
    response_model=schemas.ReviewPeriodSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["review_periods"],
)
def delete_review_period(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    review_period = actions.get(db=db, id=id)
    if not review_period:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="review_period not found")
    review_period = actions.remove(db=db, id=id)
    return review_period