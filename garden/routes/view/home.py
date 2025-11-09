from fastapi import APIRouter, Request, Response, Depends
from typing import Annotated
from utils.templates import templates
import crud

from models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession

from utils.translation import translation_service, get_user_language

router = APIRouter()

@router.get("/", name="home")
async def home(
    request: Request,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    language = get_user_language(request)
    translations = translation_service.get_all_translations(language)
    message = await crud.get_current_message(session=session)
    return templates.TemplateResponse(
        request=request,
        name="user/home.html",
        context={
            "message": message,
            "translations": translations,
            "current_language": language,
        },
    )

@router.get("/switch/{language}")
async def switch_language(language: str, response: Response, request: Request):
    supported_languages = ["en", "ru"]
    if language not in supported_languages:
        language = "en"

    response.set_cookie(
        key="language",
        value=language,
        max_age=365 * 24 * 60 * 60,
        httponly=True
    )

    referer = request.headers.get("referer", "/")
    response.headers["Location"] = referer
    response.status_code = 302
    return response
