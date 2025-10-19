from fastapi import APIRouter, Request, Depends
from typing import Annotated
from utils.templates import templates

router = APIRouter()

# @router.get("/plants")
# async def get_all_plants():
#
#
# @router.get("/{category_id}")
# async def get_category(category_id: int):
#
#
# @router.get("/{category_id}/{plant_id}")
# async def get_plant(category_id: int, plant_id: int):


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
