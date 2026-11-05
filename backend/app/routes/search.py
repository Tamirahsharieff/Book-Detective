
from fastapi import APIRouter
from backend.app.models.search import BookSearchRequest

router = APIRouter()


@router.post("/preview")
def preview_search(request: BookSearchRequest):

    return {
        "message": "Search request received successfully!",
        "total_clues": len(request.clues),
        "max_results": request.max_results,
        "clues": request.model_dump()["clues"]
    }