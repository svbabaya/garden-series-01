from fastapi import APIRouter, Request, Depends
from typing import Annotated
from utils.templates import templates
import crud

from models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get("/", name="home")
async def home(
    request: Request,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    message = await crud.get_current_message(session=session)
    return templates.TemplateResponse(
        request=request,
        name="user/home.html",
        context={"message": message},
    )
