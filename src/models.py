from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import  ForeignKey, String
from src.database import Base
import enum

class RatingEnum(enum.Enum):
    NO_RATING = 0
    DISLIKE = 1
    LIKE = 5


class ItemModel(Base):
    __tablename__ = "items"

    id:  Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()


class ReviewModel(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[RatingEnum]
    comment: Mapped[str] = mapped_column(String(256),nullable=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"))
