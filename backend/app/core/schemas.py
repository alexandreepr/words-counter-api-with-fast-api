from pydantic import BaseModel

class WordsCounterRequest(BaseModel):
    words_string: str

