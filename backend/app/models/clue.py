from pydantic import BaseModel, Field
from typing import Literal


class BookClue(BaseModel):

    clue_type: Literal[
        "scene",
        "character",
        "setting",
        "object",
        "mood",
        "quote",
        "cover_detail",
        "other"
    ]

    description: str = Field(
        min_length=3,
        max_length=500
    )

    confidence: Literal[
        "certain",
        "vague",
        "possibly_misremembered"
    ] = "vague"