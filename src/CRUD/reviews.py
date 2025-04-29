from  sqlalchemy import select
from src.models import ReviewModel
from src.database import  new_async_session
from src.schemas import ReviewSchema

class AsyncCRUD:
    @staticmethod
    async def insert_reviews(review: ReviewSchema):
        async with new_async_session() as session:
            new_review = ReviewModel(rating=review.rating, item_id=review.item_id, comment=review.comment)
            session.add(new_review)
            await session.commit()
            return new_review

    @staticmethod
    async def select_reviews_by_item(item_id: int):
        async with new_async_session() as session:
            query = select(ReviewModel).filter_by(item_id=item_id)
            result = await session.execute(query)
            reviews = result.scalars().all()
            return reviews

    @staticmethod
    async def select_reviews_by_id(review_id: int):
        async with new_async_session() as session:
            query = select(ReviewModel).filter_by(id=review_id)
            result = await session.execute(query)
            reviews = result.scalars().one_or_none()
            return reviews

    @staticmethod
    async def update_reviews(review_id: int, new_review: ReviewSchema):
        async with new_async_session() as session:
            old_review = await session.get(ReviewModel, review_id)
            if old_review:
                old_review.item_id = new_review.item_id
                old_review.comment = new_review.comment
                old_review.rating = new_review.rating
                await session.commit()

    @staticmethod
    async def delete_reviews(review_id: int):
        async with new_async_session() as session:
            review = await session.get(ReviewModel, review_id)
            if review:
                await session.delete(review)
                await session.commit()