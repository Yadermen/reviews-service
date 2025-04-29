from fastapi import APIRouter
from src.api.reviews import router as reviews_router
from src.api.items import router as items_router

main_router = APIRouter()
main_router.include_router(items_router)

main_router.include_router(reviews_router)
