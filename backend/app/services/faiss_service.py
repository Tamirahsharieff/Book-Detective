import faiss
import numpy as np

from backend.app.services.embedding_service import (
    generate_book_embeddings,
    model
)


def build_faiss_index():
    """Create a FAISS index from book embeddings."""

    books, embeddings = generate_book_embeddings()

    embeddings = np.asarray(
        embeddings,
        dtype=np.float32
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    return books, index


def search_books(query, books, index, top_k=5):
    """Find books that best match the user's description."""

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    query_embedding = np.asarray(
        query_embedding,
        dtype=np.float32
    )

    scores, indices = index.search(
        query_embedding,
        min(top_k, len(books))
    )

    results = []

    for score, book_index in zip(scores[0], indices[0]):

        results.append({
            "book": books[int(book_index)],
            "similarity_score": float(score)
        })

    return results