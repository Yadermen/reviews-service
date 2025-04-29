from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from src.CRUD.reviews import AsyncCRUD
from src.schemas import ReviewSchema

router = APIRouter()

@router.post("/api/reviews/create")
async def create_review(review:ReviewSchema):
    review = await AsyncCRUD.insert_reviews(review)
    return {"id": review.id, "rating": review.rating, "item_id": review.item_id, "comment":review.comment}

@router.get("/api/reviews/view/{review_id}")
async def get_review_by_id(review_id:int):
    review = await AsyncCRUD.select_reviews_by_id(review_id)
    if review is None:
        raise HTTPException(status_code=404,detail="Not Found")
    return{"review": review}

@router.put("/api/reviews/update/{review_id}")
async def update_review(review_id:int, new_review:ReviewSchema):
    await AsyncCRUD.update_reviews(review_id=review_id, new_review=new_review)
    return{"ok":True}

@router.delete("/api/reviews/remove/{review_id}")
async def delete_review(review_id:int):
    await AsyncCRUD.delete_reviews(review_id=review_id)
    return {"ok": True}
@router.get("/api/items/{item_id}/reviews")
async def get_item_reviews(item_id:int):
    reviews = await AsyncCRUD.select_reviews_by_item(item_id)
    if not reviews:
        raise HTTPException(status_code=404,detail= "Not Found")
    return{"id":item_id, "reviews": reviews}