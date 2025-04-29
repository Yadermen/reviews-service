from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from src.CRUD.items import AsyncCRUD
from src.schemas import ItemSchema

router = APIRouter()


@router.get("/create-tables")
async def create_tables():
    await AsyncCRUD.create_tables()
    return {"ok": True}

@router.post("/api/items/create")
async def create_item(item:ItemSchema):
    item = await AsyncCRUD.insert_item(item)
    return {"id": item.id, "name": item.name}

@router.delete("/api/items/remove/{item_id}")
async def delete_item(item_id:int):
    await AsyncCRUD.delete_item(item_id)
    return {"ok": True}

@router.get("/api/items/{item_id}/rating")
async def get_item_rating(item_id:int):
    rating = await AsyncCRUD.get_avg_rating(item_id)
    if rating is None:
        raise HTTPException(status_code=404, detail="Rating not found")
    return {"id":item_id,"rating": rating}

