from fastapi import FastAPI

app = FastAPI(
    title="Book Detective",
    description="An AI-powered book discovery application",
    version="1.0.0"
)


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