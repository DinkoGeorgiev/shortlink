from sqlalchemy import TEXT
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class LinkModel(Base):
    """Link model class"""

    __tablename__ = "links"

    id: Mapped[str] = mapped_column(primary_key=True, index=True)
    long_link: Mapped[str] = mapped_column(TEXT)
