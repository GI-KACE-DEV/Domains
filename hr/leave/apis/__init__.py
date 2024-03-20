from .annual_leave import annual_leave_router
from .leave_type import leave_type_router
from .leave import leave_router
from fastapi import APIRouter


leave_router_main = APIRouter()

leave_router_main.include_router(leave_type_router)
leave_router_main.include_router(annual_leave_router)
leave_router_main.include_router(leave_router)

