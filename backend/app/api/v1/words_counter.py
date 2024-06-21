from fastapi import APIRouter
from http.client import HTTPException

from ...core.schemas import WordsCounterRequest


router = APIRouter(tags=["words-counter"])

@router.post("/words-counter")
async def post_words_counter(request: WordsCounterRequest):
    words_string = request.words_string.strip()

    if not words_string:
        raise HTTPException(status_code=400, detail="Input string is empty or contains only whitespace.")

    words_count = len(words_string.split())

    return { "words_count": words_count }
