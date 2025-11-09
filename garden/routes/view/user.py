from fastapi import APIRouter, Request
from utils.templates import templates

from utils.translation import translation_service, get_user_language

router = APIRouter()

@router.get("/category", name="category")
async def category(request: Request):
    return templates.TemplateResponse(
        name="user/category.html",
        context={"request": request}
    )

@router.get("/plant", name="plant")
async def plant(request: Request):
    return templates.TemplateResponse(
        name="user/plant.html",
        context={"request": request}
    )

@router.get("/history", name="history")
async def history(request: Request):
    return templates.TemplateResponse(
        name="user/history.html",
        context={"request": request}
    )

@router.get("/communication", name="communication")
async def communication(request: Request):
    return templates.TemplateResponse(
        name="user/communication.html",
        context={"request": request}
    )

@router.get("/search", name="search")
async def about(request: Request):
    return templates.TemplateResponse(
        name="user/search.html",
        context={"request": request}
    )

@router.get("/art", name="art")
async def about(request: Request):
    return templates.TemplateResponse(
        name="user/art.html",
        context={"request": request}
    )

@router.get("/ideas", name="ideas")
async def about(request: Request):
    return templates.TemplateResponse(
        name="user/ideas.html",
        context={"request": request}
    )

@router.get("/details", name="details")
async def about(request: Request):
    return templates.TemplateResponse(
        name="user/details.html",
        context={"request": request}
    )
