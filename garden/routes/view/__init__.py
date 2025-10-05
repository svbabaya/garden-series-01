from .home import router as home_router
from .user import router as user_router

# from .admin import router as admin_router

__all__ = (
    "home_router",
    "user_router",
    # "admin_router",
)
