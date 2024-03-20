from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import date, datetime
from fastapi import HTTPException
from app.domains.common.models.practice_area import PracticeArea
from app.domains.common.models.sector import Sector

from app.crud.base import CRUDBase
from app.db.base_class import UUID
from .. import models
from ..schemas import (
    StaffCreate, StaffUpdate
)
from app.crud.base import ModelType, CreateSchemaType, UpdateSchemaType
from sqlalchemy.orm import Session
import sys


class CRUDStaff(CRUDBase[models.Staff, StaffCreate, StaffUpdate]):

    def _create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        sector_ids = obj_in_data.pop("sector_ids", [])
        practice_area_ids = obj_in_data.pop("practice_area_ids", [])

        db_obj = self.model(**obj_in_data)

        try:
            if practice_area_ids:
                practice_areas = db.query(PracticeArea).filter(
                    PracticeArea.id.in_(practice_area_ids)).all()
                if practice_areas:
                    db_obj.practice_areas.extend(practice_areas)
                    db.add(db_obj)

            if sector_ids:
                sectors = db.query(PracticeArea).filter(
                    Sector.id.in_(sector_ids)).all()
                if sectors:
                    db_obj.sectors.extend(sectors)

            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj

        except Exception:
            # log exception for debug
            # raise api excetion
            raise HTTPException(
                status_code=4000, detail="Error will creating staff")

    async def add_sectors(self, staff_id: UUID, db: Session, sector_ids: List[UUID]):
        staff = await self.read_by_id(staff_id, db)
        sectors = db.query(Sector).filter(Sector.id.in_([1, 2]))
        if not (staff or sectors):
            raise HTTPException(
                status_code=400, details="No valid staff or sectors found")
        try:
            for sector in sectors:
                if not sector in staff.sectors:
                    staff.sectors.append(sector)

            db.add(staff)
            db.commit()
            db.refresh(staff)
            return staff

        except:
            db.rollback()
            print("{}".format(sys.exc_info()))
            raise HTTPException(
                status_code=500, detail="Error while adding sectors")

    def remove_sectors(self, staff_id: UUID, db: Session, sector_ids: List[UUID]):
        # staff = self.read_by_id(id, db)
        staff = self.model
        sectors = db.query(Sector).filter(Sector.id.in_(sector_ids)).all()
        if not (staff or sectors):
            raise HTTPException(
                status_code=400, detail="No valid sectors found")
        try:
            for sector in sectors:
                if sector in staff.sectors:
                    staff.sectors.remove(sector)
                    staff.secto

            db.add(staff)
            db.commit()
            db.refresh(staff)
            return staff
        except:
            db.rollback()
            print("{}".format(sys.exc_info()))
            raise HTTPException(
                status_code=500, detail="Error while removing sectors")


staff_actions = CRUDStaff(models.Staff)
