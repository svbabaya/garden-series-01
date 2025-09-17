from core.config import settings
from fastapi import APIRouter

public_api_router = APIRouter(
    prefix=settings.prefix.public_api_prefix,
    tags=[settings.prefix.public_api_prefix],
    responses={404: {"description": "Not found"}},
    deprecated=False,
)

admin_api_router = APIRouter(
    prefix=settings.prefix.admin_api_prefix,
    tags=[settings.prefix.admin_api_prefix],
    responses={404: {"description": "Not found"}},
    deprecated=False,
)
