from fastapi import APIRouter, Request, Depends
from typing import Annotated
from utils.templates import templates

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
