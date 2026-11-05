from sqlalchemy import Column, Integer, String, Text, JSON

from backend.app.database import Base


class BookDB(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)

    authors = Column(JSON, nullable=False)

    description = Column(Text, nullable=False)

    genres = Column(JSON, default=list)

    publication_year = Column(Integer, nullable=True)

    setting = Column(Text, nullable=True)

    characters = Column(JSON, default=list)

    themes = Column(JSON, default=list)

    cover_url = Column(Text, nullable=True)