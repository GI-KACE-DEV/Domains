from fastapi import APIRouter, Depends
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session

from app.domains.officemanager.schemas import visits as schemas
from app.utils.deps import get_db
from app.domains.officemanager.services.visits import office_area_actions as office_areas
from app.domains.officemanager.services.visits import visit_status_actions as visit_statuses
from app.domains.officemanager.services.visits import visit_category_actions as visit_categories
from app.domains.officemanager.services.visits import expected_visitor_actions as expected_visitors
from app.domains.officemanager.services.visits import visit_entry_actions as visit_entries
from app.domains.officemanager.services.visits import visitor_actions as visitors


# Office Area
visit_router = APIRouter(prefix="/visits")


@visit_router.get("/office_areas", response_model=List[schemas.OfficeAreaSchema], tags=["office_areas"])
def list_office_areas(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _office_areas = office_areas.get_all(db=db, skip=skip, limit=limit)
    return _office_areas


@visit_router.post(
    "/office_areas", response_model=schemas.OfficeAreaSchema, status_code=HTTP_201_CREATED, tags=["office_areas"]
)
def create_office_area(*, db: Session = Depends(get_db), office_area_in: schemas.OfficeAreaCreate) -> Any:
    _office_area = office_areas.create(db=db, obj_in=office_area_in)
    return _office_area


@visit_router.put(
    "/office_areas/{id}",
    response_model=schemas.OfficeAreaSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["office_areas"],
)
def update_office_area(
    *, db: Session = Depends(get_db), id: UUID4, office_area_in: schemas.OfficeAreaUpdate,
) -> Any:
    _office_area = office_areas.    get(db=db, id=id)
    if not _office_area:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="office_area not found")
    _office_area = office_areas.update(db=db, db_obj=_office_area, obj_in=office_area_in)
    return _office_area


@visit_router.get(
    "/office_areas/{id}",
    response_model=schemas.OfficeAreaSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["office_areas"],
)
def get_office_area(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _office_area = office_areas.get(db=db, id=id)
    if not _office_area:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="office_area not found")
    return _office_area


@visit_router.delete(
    "/office_areas/{id}",
    response_model=schemas.OfficeAreaSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["office_areas"],
)
def delete_office_area(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _office_area = office_areas.get(db=db, id=id)
    if not _office_area:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="office_area not found")
    _office_area = office_areas.remove(db=db, id=id)
    return _office_area


# Visit Status

@visit_router.get("/visit_statuses", response_model=List[schemas.VisitStatusSchema], tags=["visit_statuses"])
def list_visit_statuses(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _visit_statuses = visit_statuses.get_all(db=db, skip=skip, limit=limit)
    return _visit_statuses


@visit_router.post(
    "/visit_statuses", response_model=schemas.VisitStatusSchema, status_code=HTTP_201_CREATED, tags=["visit_statuses"]
)
def create_visit_status(*, db: Session = Depends(get_db), visit_status_in: schemas.VisitStatusCreate) -> Any:
    _visit_status = visit_statuses.create(db=db, obj_in=visit_status_in)
    return _visit_status


@visit_router.put(
    "/visit_statuses/{id}",
    response_model=schemas.VisitStatusSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visit_statuses"],
)
def update_visit_status(
    *, db: Session = Depends(get_db), id: UUID4, visit_status_in: schemas.VisitStatusUpdate,
) -> Any:
    _visit_status = visit_statuses.get(db=db, id=id)
    if not _visit_status:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visit_status not found")
    _visit_status = visit_statuses.update(db=db, db_obj=_visit_status, obj_in=visit_status_in)
    return _visit_status


@visit_router.get(
    "/visit_statuses/{id}",
    response_model=schemas.VisitStatusSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visit_statuses"],
)
def get_visit_status(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _visit_status = visit_statuses.get(db=db, id=id)
    if not _visit_status:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visit_status not found")
    return _visit_status


@visit_router.delete(
    "/visit_statuses/{id}",
    response_model=schemas.VisitStatusSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visit_statuses"],
)
def delete_visit_status(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _visit_status = visit_statuses.get(db=db, id=id)
    if not _visit_status:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visit_status not found")
    visit_status = visit_statuses.remove(db=db, id=id)
    return visit_status


# Visit Category
@visit_router.get("/visit_categories", response_model=List[schemas.VisitCategorySchema], tags=["visit_categories"])
def list_visit_categories(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _visit_categories = visit_categories.get_all(db=db, skip=skip, limit=limit)
    return _visit_categories


@visit_router.post(
    "/visit_categories", response_model=schemas.VisitCategorySchema, status_code=HTTP_201_CREATED, tags=["visit_categories"]
)
def create_visit_category(*, db: Session = Depends(get_db), visit_category_in: schemas.VisitCategoryCreate) -> Any:
    _visit_category = visit_categories.create(db=db, obj_in=visit_category_in)
    return _visit_category


@visit_router.put(
    "/visit_categories/{id}",
    response_model=schemas.VisitCategorySchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visit_categories"],
)
def update_visit_category(
    *, db: Session = Depends(get_db), id: UUID4, visit_category_in: schemas.VisitCategoryUpdate,
) -> Any:
    _visit_category = visit_category.get(db=db, id=id)
    if not visit_category:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visit_category not found")
    _visit_category = visit_categories.update(db=db, db_obj=_visit_category, obj_in=visit_category_in)
    return _visit_category


@visit_router.get(
    "/visit_categories/{id}",
    response_model=schemas.VisitCategorySchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visit_categories"],
)
def get_visit_category(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _visit_category = visit_categories.get(db=db, id=id)
    if not _visit_category:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visit_category not found")
    return _visit_category


@visit_router.delete(
    "/visit_categories/{id}",
    response_model=schemas.VisitCategorySchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visit_categories"],
)
def delete_visit_category(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _visit_category = visit_categories.get(db=db, id=id)
    if not _visit_category:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visit_category not found")
    _visit_category = visit_categories.remove(db=db, id=id)
    return _visit_category


# Expected Visitor
@visit_router.get("/expected_visitors", response_model=List[schemas.ExpectedVisitorSchema], tags=["expected_visitors"])
def list_expected_visitors(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _expected_visitors = expected_visitors.get_all(db=db, skip=skip, limit=limit)
    return _expected_visitors


@visit_router.post(
    "/expected_visitors", response_model=schemas.ExpectedVisitorSchema, status_code=HTTP_201_CREATED, tags=["expected_visitors"]
)
def create_expected_visitor(*, db: Session = Depends(get_db), expected_visitor_in: schemas.ExpectedVisitorCreate) -> Any:
    _expected_visitor = expected_visitors.create(db=db, obj_in=expected_visitor_in)
    return _expected_visitor


@visit_router.put(
    "/expected_visitors/{id}",
    response_model=schemas.ExpectedVisitorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["expected_visitors"],
)
def update_expected_visitor(
    *, db: Session = Depends(get_db), id: UUID4, expected_visitor_in: schemas.ExpectedVisitorUpdate,
) -> Any:
    _expected_visitor = expected_visitors.get(db=db, id=id)
    if not _expected_visitor:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="expected_visitor not found")
    _expected_visitor = expected_visitors.update(db=db, db_obj=_expected_visitor, obj_in=expected_visitor_in)
    return _expected_visitor


@visit_router.get(
    "/expected_visitors/{id}",
    response_model=schemas.ExpectedVisitorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["expected_visitors"],
)
def get_expected_visitor(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _expected_visitor = expected_visitors.get(db=db, id=id)
    if not _expected_visitor:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="expected_visitor not found")
    return _expected_visitor


@visit_router.delete(
    "/expected_visitors/{id}",
    response_model=schemas.ExpectedVisitorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["expected_visitors"],
)
def delete_expected_visitor(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _expected_visitor = expected_visitors.get(db=db, id=id)
    if not _expected_visitor:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="expected_visitor not found")
    _expected_visitor = expected_visitors.remove(db=db, id=id)
    return _expected_visitor


# Visit Entry
@visit_router.get("/visit_entries", response_model=List[schemas.VisitEntrySchema], tags=["visit_entries"])
def list_visit_entries(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _visit_entries = visit_entries.get_all(db=db, skip=skip, limit=limit)
    return _visit_entries


@visit_router.post(
    "/visit_entries", response_model=schemas.VisitEntrySchema, status_code=HTTP_201_CREATED, tags=["visit_entries"]
)
def create_visit_entry(*, db: Session = Depends(get_db), visit_entry_in: schemas.VisitEntryCreate) -> Any:
    _visit_entry = visit_entries.create(db=db, obj_in=visit_entry_in)
    return _visit_entry


@visit_router.put(
    "/visit_entries/{id}",
    response_model=schemas.VisitEntrySchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visit_entries"],
)
def update_visit_entry(
    *, db: Session = Depends(get_db), id: UUID4, visit_entry_in: schemas.VisitEntryUpdate,
) -> Any:
    _visit_entry = visit_entry.get(db=db, id=id)
    if not _visit_entry:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visit_entry not found")
    _visit_entry = visit_entries.update(db=db, db_obj=visit_entry, obj_in=visit_entry_in)
    return _visit_entry


@visit_router.get(
    "/visit_entries/{id}",
    response_model=schemas.VisitEntrySchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visit_entries"],
)
def get_visit_entry(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _visit_entry = visit_entries.get(db=db, id=id)
    if not _visit_entry:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visit_entry not found")
    return _visit_entry


@visit_router.delete(
    "/visit_entries/{id}",
    response_model=schemas.VisitEntrySchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visit_entries"],
)
def delete_visit_entry(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _visit_entry = visit_entries.get(db=db, id=id)
    if not _visit_entry:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visit_entry not found")
    _visit_entry = visit_entries.remove(db=db, id=id)
    return _visit_entry


#Visitor


# Visitor
@visit_router.get("/visitors", response_model=List[schemas.VisitorSchema], tags=["visitors"])
def list_visitors(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _visitors = visitors.get_all(db=db, skip=skip, limit=limit)
    return _visitors


@visit_router.post(
    "/visitors", response_model=schemas.VisitorSchema, status_code=HTTP_201_CREATED, tags=["visitors"]
)
def create_visitor(*, db: Session = Depends(get_db), visitor_in: schemas.VisitorCreate) -> Any:
    _visitor = visitors.create(db=db, obj_in=visitor_in)
    return _visitor


@visit_router.put(
    "/visitors/{id}",
    response_model=schemas.VisitorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visitors"],
)
def update_visitor(
    *, db: Session = Depends(get_db), id: UUID4, visitor_in: schemas.VisitorUpdate,
) -> Any:
    _visitor = visitor.get(db=db, id=id)
    if not _visitor:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visitor not found")
    _visitor = visitors.update(db=db, db_obj=visitor, obj_in=visitor_in)
    return _visitor


@visit_router.get(
    "/visitors/{id}",
    response_model=schemas.VisitorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visitors"],
)
def get_visitor(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _visitor = visitors.get(db=db, id=id)
    if not _visitor:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visitor not found")
    return _visitor


@visit_router.delete(
    "/visitors/{id}",
    response_model=schemas.VisitorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visitors"],
)
def delete_visitor(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _visitor = visitors.get(db=db, id=id)
    if not _visitor:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visitor not found")
    _visitor = visitors.remove(db=db, id=id)
    return _visitor


#Visitor



# Visitor
@visit_router.get("/visitors", response_model=List[schemas.VisitorSchema], tags=["visitors"])
def list_visitors(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _visitors = visitors.get_all(db=db, skip=skip, limit=limit)
    return _visitors


@visit_router.post(
    "/visitors", response_model=schemas.VisitorSchema, status_code=HTTP_201_CREATED, tags=["visitors"]
)
def create_visitor(*, db: Session = Depends(get_db), visitor_in: schemas.VisitorCreate) -> Any:
    _visitor = visitors.create(db=db, obj_in=visitor_in)
    return _visitor


@visit_router.put(
    "/visitors/{id}",
    response_model=schemas.VisitorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visitors"],
)
def update_visitor(
    *, db: Session = Depends(get_db), id: UUID4, visitor_in: schemas.VisitorUpdate,
) -> Any:
    _visitor = visitor.get(db=db, id=id)
    if not _visitor:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visitor not found")
    _visitor = visitors.update(db=db, db_obj=visitor, obj_in=visitor_in)
    return _visitor


@visit_router.get(
    "/visitors/{id}",
    response_model=schemas.VisitorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visitors"],
)
def get_visitor(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _visitor = visitors.get(db=db, id=id)
    if not _visitor:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visitor not found")
    return _visitor


@visit_router.delete(
    "/visitors/{id}",
    response_model=schemas.VisitorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visitors"],
)
def delete_visitor(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _visitor = visitors.get(db=db, id=id)
    if not _visitor:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visitor not found")
    _visitor = visitors.remove(db=db, id=id)
    return _visitor


# Visitor
@visit_router.get("/visitors", response_model=List[schemas.VisitorSchema], tags=["visitors"])
def list_visitors(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _visitors = visitors.get_all(db=db, skip=skip, limit=limit)
    return _visitors


@visit_router.post(
    "/visitors", response_model=schemas.VisitorSchema, status_code=HTTP_201_CREATED, tags=["visitors"]
)
def create_visitor(*, db: Session = Depends(get_db), visitor_in: schemas.VisitorCreate) -> Any:
    _visitor = visitors.create(db=db, obj_in=visitor_in)
    return _visitor


@visit_router.put(
    "/visitors/{id}",
    response_model=schemas.VisitorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visitors"],
)
def update_visitor(
    *, db: Session = Depends(get_db), id: UUID4, visitor_in: schemas.VisitorUpdate,
) -> Any:
    _visitor = visitor.get(db=db, id=id)
    if not _visitor:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visitor not found")
    _visitor = visitors.update(db=db, db_obj=visitor, obj_in=visitor_in)
    return _visitor


@visit_router.get(
    "/visitors/{id}",
    response_model=schemas.VisitorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visitors"],
)
def get_visitor(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _visitor = visitors.get(db=db, id=id)
    if not _visitor:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visitor not found")
    return _visitor


@visit_router.delete(
    "/visitors/{id}",
    response_model=schemas.VisitorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visitors"],
)
def delete_visitor(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _visitor = visitors.get(db=db, id=id)
    if not _visitor:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visitor not found")
    _visitor = visitors.remove(db=db, id=id)
    return _visitor


#Visitor



# Visitor
@visit_router.get("/visitors", response_model=List[schemas.VisitorSchema], tags=["visitors"])
def list_visitors(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    _visitors = visitors.get_all(db=db, skip=skip, limit=limit)
    return _visitors


@visit_router.post(
    "/visitors", response_model=schemas.VisitorSchema, status_code=HTTP_201_CREATED, tags=["visitors"]
)
def create_visitor(*, db: Session = Depends(get_db), visitor_in: schemas.VisitorCreate) -> Any:
    _visitor = visitors.create(db=db, obj_in=visitor_in)
    return _visitor


@visit_router.put(
    "/visitors/{id}",
    response_model=schemas.VisitorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visitors"],
)
def update_visitor(
    *, db: Session = Depends(get_db), id: UUID4, visitor_in: schemas.VisitorUpdate,
) -> Any:
    _visitor = visitor.get(db=db, id=id)
    if not _visitor:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visitor not found")
    _visitor = visitors.update(db=db, db_obj=visitor, obj_in=visitor_in)
    return _visitor


@visit_router.get(
    "/visitors/{id}",
    response_model=schemas.VisitorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visitors"],
)
def get_visitor(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _visitor = visitors.get(db=db, id=id)
    if not _visitor:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visitor not found")
    return _visitor


@visit_router.delete(
    "/visitors/{id}",
    response_model=schemas.VisitorSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["visitors"],
)
def delete_visitor(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    _visitor = visitors.get(db=db, id=id)
    if not _visitor:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="visitor not found")
    _visitor = visitors.remove(db=db, id=id)
    return _visitor
