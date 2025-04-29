from pydantic import BaseModel
from src.models import RatingEnum

class ReviewSchema(BaseModel):
    item_id:int
    rating: RatingEnum
    comment: str
class ItemSchema(BaseModel):
    name:str