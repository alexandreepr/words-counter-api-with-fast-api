from fastapi import APIRouter

from .words_counter import router as words_counter_router

router = APIRouter(prefix="/v1")
router.include_router(words_counter_router)