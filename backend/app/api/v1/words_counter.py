from fastapi import APIRouter, HTTPException

from ...core.schemas import WordsCounterRequest, WordsCounterResponse
from ...core.logger import logger

router = APIRouter(tags=["words-counter"])


@router.post(
    "/words-counter",
    response_description="Object containing a key `words_count` with the number of words in the input string.",
)
async def post_words_counter(request: WordsCounterRequest) -> WordsCounterResponse:
    """
    Count the number of words in the input string.

    - **words_string**: The input string to count the number of words in.
    """
    words_string = request.words_string.strip()

    if not words_string:
        logger.error('POST /')
        raise HTTPException(
            status_code=422,
            detail="Input string is empty or contains only whitespace."
        )

    words_count = len(words_string.split())

    logger.info('POST /')

    return {"words_count": words_count}