from .api import plants as api_plants  # , admin as api_admin, auth as api_auth
from .web import plants as web_plants  # , admin as web_admin, auth as web_auth

__all__ = [
    "api_plants",
    # 'api_admin',
    # 'api_auth',
    "web_plants",
    # 'web_admin',
    # 'web_auth'
]
