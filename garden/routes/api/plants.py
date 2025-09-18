from fastapi import APIRouter

router = APIRouter()


@router.get("/{category_id}")
async def get_category(category_id: int):
    return [{"category_id": category_id}]


@router.get("/{category_id}/{plant_id}")
async def get_plant(category_id: int, plant_id: int):
    return [{"category_id": category_id, "plant_id": plant_id}]
