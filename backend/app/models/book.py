from pydantic import BaseModel, Field
from typing import Optional


class Book(BaseModel):

    title: str = Field(
        min_length=1,
        max_length=200
    )

    authors: list[str]

    description: str = Field(
        min_length=10,
        max_length=2000
    )

    genres: list[str] = Field(default_factory=list)

    publication_year: Optional[int] = None

    setting: Optional[str] = None

    characters: list[str] = Field(default_factory=list)

    themes: list[str] = Field(default_factory=list)

    cover_url: Optional[str] = None