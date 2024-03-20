from fastapi import APIRouter
from .action import action_router
from .lead import lead_router
from .client import client_router
from .consultation import consultation_router


crm_router  = APIRouter()

crm_router.include_router(lead_router)
crm_router.include_router(client_router)
crm_router.include_router(consultation_router)
crm_router.include_router(action_router)
