from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_all_plants():
    return [{"template": "plants.html"}]


@router.get("/{category_id}")
async def get_category(category_id: int):
    return [{"template": "category.html"}]


@router.get("/{category_id}/{plant_id}")
async def get_plant(category_id: int, plant_id: int):
    return [{"template": "plant.html"}]
