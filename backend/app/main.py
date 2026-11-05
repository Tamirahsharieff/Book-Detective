from fastapi import FastAPI
from backend.app.routes.search import router as search_router

app = FastAPI(
    title="Book Detective",
    description="An AI-powered book discovery application",
    version="1.0.0"
)
app.include_router(search_router, prefix="/search", tags=["Book Search"])


@app.get("/")
def home():
    return {
        "project": "Book Detective",
        "message": "Welcome! Find the book you can't remember.",
        "status": "Running successfully"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "Book Detective"
    }