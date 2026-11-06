import json
from pathlib import Path
from sentence_transformers import SentenceTransformer


# Locate project root
BASE_DIR = Path(__file__).resolve().parents[3]

# Load the AI model
model = SentenceTransformer("all-MiniLM-L6-v2")


def load_books():
    """Load books from the JSON catalogue."""

    books_file = BASE_DIR / "data" / "raw" / "books.json"

    with open(books_file, "r", encoding="utf-8") as file:
        books = json.load(file)

    return books


def create_book_text(book):
    """Combine book details into searchable text."""

    return (
        f"Title: {book['title']}. "
        f"Author: {', '.join(book['authors'])}. "
        f"Description: {book['description']} "
        f"Genres: {', '.join(book['genres'])}. "
        f"Setting: {book.get('setting', '')}. "
        f"Characters: {', '.join(book.get('characters', []))}. "
        f"Themes: {', '.join(book.get('themes', []))}."
    )


def generate_book_embeddings():
    """Generate numerical embeddings for all books."""

    books = load_books()

    book_texts = [
        create_book_text(book)
        for book in books
    ]

    embeddings = model.encode(
        book_texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return books, embeddings