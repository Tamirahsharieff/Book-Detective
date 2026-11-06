import json
from pathlib import Path

from backend.app.database import SessionLocal
from backend.app.models.book_db import BookDB


def load_books():

    # Locate the project root
    project_root = Path(__file__).resolve().parents[3]
    json_file = project_root / "data" / "raw" / "books.json"

    # Read book records from JSON
    with open(json_file, "r", encoding="utf-8") as file:
        books = json.load(file)

    print(f"Found {len(books)} books in the dataset.")

    # Create database session
    db = SessionLocal()

    try:
        inserted_count = 0

        for book_data in books:

            # Check whether the book already exists
            existing_book = db.query(BookDB).filter_by(
                title=book_data["title"]
            ).first()

            if existing_book:
                continue

            # Create a new database record
            new_book = BookDB(
                title=book_data["title"],
                authors=book_data["authors"],
                description=book_data["description"],
                genres=book_data.get("genres", []),
                publication_year=book_data.get("publication_year"),
                setting=book_data.get("setting"),
                characters=book_data.get("characters", []),
                themes=book_data.get("themes", []),
                cover_url=book_data.get("cover_url")
            )

            db.add(new_book)
            inserted_count += 1

        # Save records to PostgreSQL
        db.commit()

        print(f"Successfully inserted {inserted_count} books!")

    except Exception as error:
        db.rollback()
        print("Error loading books:", error)

    finally:
        db.close()


if __name__ == "__main__":
    load_books()