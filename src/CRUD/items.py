from  sqlalchemy import select
from src.models import ReviewModel, ItemModel, RatingEnum
from src.database import Base, async_engine, new_async_session
from src.schemas import  ItemSchema


class AsyncCRUD:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


    @staticmethod
    async def insert_item(item:ItemSchema):
        async with new_async_session() as session:
            new_item = ItemModel(name=item.name)
            session.add(new_item)
            await session.commit()
            return new_item
    @staticmethod
    async def delete_item(item_id:int):
        async with new_async_session() as session:
            item = await session.get(ItemModel, item_id)
            if item:
                await session.delete(item)
                await session.commit()
    @staticmethod
    async def get_avg_rating(item_id):
        async with new_async_session() as session:
            stmt = select(ReviewModel.rating).filter(
                ReviewModel.item_id == item_id,
                ReviewModel.rating != RatingEnum.NO_RATING
            )
            result = await session.execute(stmt)
            ratings = [r.value for r in result.scalars().all()]
            if not ratings:
               return float(0)
            count_fives = ratings.count(5)
            percent = (count_fives / len(ratings)) * 100.0
            print(f"{percent=}")
            return round(percent, 2)