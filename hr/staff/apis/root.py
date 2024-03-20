from fastapi import APIRouter
from .department import department_router
from .designation import designation_router
from .practice_area import practice_area_router
from .staff import staff_router
from .sector import sector_router


staff_root_router = APIRouter()

staff_root_router.include_router(department_router)
staff_root_router.include_router(designation_router)
staff_root_router.include_router(practice_area_router)
staff_root_router.include_router(sector_router)
staff_root_router.include_router(staff_router)
