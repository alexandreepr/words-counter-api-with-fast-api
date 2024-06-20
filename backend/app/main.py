from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class WordsCounterRequest(BaseModel):
    words_string: str

@app.post("/api/v1/words-counter")
async def post_words_counter(request: WordsCounterRequest):
    words_string = request.words_string.strip()

    if not words_string:
        raise HTTPException(status_code=400, detail="Input string is empty or contains only whitespace.")

    words_count = len(words_string.split())

    return { "words_count": words_count }
