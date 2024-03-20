
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.common.services.practice_area import practice_area_actions as actions
from app.domains.hr.staff import schemas
from app.utils.deps import get_db

from fastapi import APIRouter, Depends

practice_area_router = APIRouter()


@practice_area_router.get("/practice_areas", response_model=List[schemas.PracticeAreaSchema], tags=["practice_areas"])
def list_practice_areas(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    practice_areas = actions.get_all(db=db, skip=skip, limit=limit)
    return practice_areas


@practice_area_router.post(
    "/practice_areas", response_model=schemas.PracticeAreaSchema, status_code=HTTP_201_CREATED, tags=["practice_areas"]
)
def create_practice_area(*, db: Session = Depends(get_db), practice_area_in: schemas.PracticeAreaCreate) -> Any:
    practice_area= actions.create(db=db, obj_in=practice_area_in)
    return practice_area


@practice_area_router.put(
    "/practice_areas/{id}",
    response_model=schemas.PracticeAreaSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["practice_areas"],
)
def update_practice_area(
    *, db: Session = Depends(get_db), id: UUID4, practice_area_in: schemas.PracticeAreaUpdate,
) -> Any:
    practice_area= actions.get(db=db, id=id)
    if not practice_area:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="practice_areanot found")
    practice_area= actions.update(db=db, db_obj=practice_area, obj_in=practice_area_in)
    return practice_area


@practice_area_router.get(
    "/practice_areas/{id}",
    response_model=schemas.PracticeAreaSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["practice_areas"],
)
def get_practice_area(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    practice_area= actions.get(db=db, id=id)
    if not practice_area:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="practice_area not found")
    return practice_area


@practice_area_router.delete(
    "/practice_areas/{id}",
    response_model=schemas.PracticeAreaSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["practice_areas"],
)
def delete_practice_area(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    practice_area= actions.get(db=db, id=id)
    if not practice_area:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="practice_areanot found")
    practice_area= actions.remove(db=db, id=id)
    return practice_area