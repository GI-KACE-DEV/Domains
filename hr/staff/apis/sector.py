
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.hr.staff.services.sector import sector_actions as actions
from app.domains.hr.staff import schemas
from app.utils.deps import get_db

from fastapi import APIRouter, Depends

sector_router = APIRouter()


@sector_router.get("/sectors", response_model=List[schemas.SectorSchema], tags=["sectors"])
def list_sectors(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    sectors = actions.get_all(db=db, skip=skip, limit=limit)
    return sectors


@sector_router.post(
    "/sectors", response_model=schemas.SectorSchema, status_code=HTTP_201_CREATED, tags=["sectors"]
)
def create_sector(*, db: Session = Depends(get_db), sector_in: schemas.SectorCreate) -> Any:
    sector= actions.create(db=db, obj_in=sector_in)
    return sector


@sector_router.put(
    "/sectors/{id}",
    response_model=schemas.SectorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["sectors"],
)
def update_sector(
    *, db: Session = Depends(get_db), id: UUID4, sector_in: schemas.SectorUpdate,
) -> Any:
    sector= actions.get(db=db, id=id)
    if not sector:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="sectornot found")
    sector= actions.update(db=db, db_obj=sector, obj_in=sector_in)
    return sector


@sector_router.get(
    "/sectors/{id}",
    response_model=schemas.SectorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["sectors"],
)
def get_sector(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    sector= actions.get(db=db, id=id)
    if not sector:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="sectornot found")
    return sector


@sector_router.delete(
    "/sectors/{id}",
    response_model=schemas.SectorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["sectors"],
)
def delete_sector(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    sector= actions.get(db=db, id=id)
    if not sector:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="sectornot found")
    sector= actions.remove(db=db, id=id)
    return sector