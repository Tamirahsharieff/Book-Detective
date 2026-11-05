import re
from sqlalchemy.orm import Session

from backend.app.models.book_db import BookDB
from backend.app.models.clue import BookClue


def get_words(text):
    """Convert text into lowercase words."""
    return set(re.findall(r"\b[a-zA-Z]{3,}\b", text.lower()))


def search_books(
    db: Session,
    clues: list[BookClue],
    max_results: int = 5
):
    books = db.query(BookDB).all()

    results = []

    field_mapping = {
        "scene": ["description", "themes"],
        "character": ["characters"],
        "setting": ["setting"],
        "object": ["description", "themes", "genres"],
        "mood": ["themes", "genres", "description"],
        "quote": ["description"],
        "cover_detail": ["title", "description"],
        "other": ["description", "themes"]
    }

    confidence_weights = {
        "certain": 1.0,
        "vague": 0.7,
        "possibly_misremembered": 0.4
    }

    for book in books:
        total_score = 0
        total_weight = 0
        matching_clues = []

        for clue in clues:
            clue_words = get_words(clue.description)

            if not clue_words:
                continue

            searchable_text = []

            for field in field_mapping[clue.clue_type]:
                value = getattr(book, field, None)

                if isinstance(value, list):
                    searchable_text.extend(str(item) for item in value)
                elif value:
                    searchable_text.append(str(value))

            book_words = get_words(" ".join(searchable_text))

            matched_words = clue_words.intersection(book_words)

            match_score = len(matched_words) / len(clue_words)

            weight = confidence_weights[clue.confidence]

            total_score += match_score * weight
            total_weight += weight

            if matched_words:
                matching_clues.append({
                    "clue": clue.description,
                    "matched_words": sorted(matched_words)
                })

        if total_weight > 0:
            final_score = (total_score / total_weight) * 100

            if final_score > 0:
                results.append({
                    "book_id": book.id,
                    "title": book.title,
                    "authors": book.authors,
                    "description": book.description,
                    "similarity_score": round(final_score, 2),
                    "matching_evidence": matching_clues
                })

    results.sort(
        key=lambda item: item["similarity_score"],
        reverse=True
    )

    return results[:max_results]