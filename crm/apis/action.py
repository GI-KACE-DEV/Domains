from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.crm.schemas import action as schemas
from app.utils.deps import get_db
from  app.domains.common.services.action import action_actions as actions


action_router = APIRouter()


@action_router.get("/actions", response_model=List[schemas.ActionSchema], tags=["actions"])
def list_actions(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _actions = actions.get_all(db=db, skip=skip, limit=limit)
    return _actions


@action_router.post(
    "/actions", response_model=schemas.ActionSchema, status_code=HTTP_201_CREATED, tags=["actions"]
)
def create_action(*, db: Session = Depends(get_db), action_in: schemas.ActionCreate) -> Any:
    action = actions.create(db=db, obj_in=action_in)
    return action


@action_router.put(
    "/actions/{id}",
    response_model=schemas.ActionSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["actions"],
)
def update_action(
    *, db: Session = Depends(get_db), id: UUID4, action_in: schemas.ActionUpdate,
) -> Any:
    action = actions.action.get(db=db, id=id)
    if not action:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="action not found")
    action = actions.update(db=db, db_obj=action, obj_in=action_in)
    return action


@action_router.get(
    "/actions/{id}",
    response_model=schemas.ActionSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["actions"],
)
def get_action(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    action = actions.get(db=db, id=id)
    if not action:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="action not found")
    return action


@action_router.delete(
    "/actions/{id}",
    response_model=schemas.ActionSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["actions"],
)
def delete_action(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    action = actions.get(db=db, id=id)
    if not action:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="action not found")
    action = actions.remove(db=db, id=id)
    return action