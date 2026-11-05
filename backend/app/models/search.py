from pydantic import BaseModel, Field
from typing import List

from backend.app.models.clue import BookClue


class BookSearchRequest(BaseModel):

    clues: List[BookClue] = Field(
        min_length=1,
        max_length=20
    )

    max_results: int = Field(
        default=5,
        ge=1,
        le=20
    )