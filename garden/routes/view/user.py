from fastapi import APIRouter, Request, Depends
from typing import Annotated
from utils.templates import templates

router = APIRouter()

# @router.get("/plants")
# async def get_all_plants():
#     return [{"template": "selection.html"}]
#
#
# @router.get("/{category_id}")
# async def get_category(category_id: int):
#     return [{"template": "category.html"}]
#
#
# @router.get("/{category_id}/{plant_id}")
# async def get_plant(category_id: int, plant_id: int):
#     return [{"template": "plant.html"}]


@router.get("/history", name="history")
async def history(request: Request):
    return templates.TemplateResponse(
        name="user/history.html",
        context={"request": request}
    )
