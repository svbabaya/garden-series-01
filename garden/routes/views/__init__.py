from .plants import router as plants_router
from .index import router as index_router

# from .admin import router as admin_router
# from .auth import router as auth_router

__all__ = [
    "plants_router",
    "index_router",
    # "admin_router",
    # "auth_router"
]
