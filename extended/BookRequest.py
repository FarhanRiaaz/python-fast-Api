from typing import Optional
from pydantic import BaseModel,Field

class BookRequest(BaseModel):
    id: Optional[int] = Field(description='The default value is not mandatory you can skip it away',default=None)
    title: str = Field(min_length=3,max_length=9)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=10)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999,lt=2026)
    
    model_config = {
        "json_schema_extra":{
            "example":{
                "title": "A new book",
                "author": "Farhan Riaz",
                "description": "A new book to the show",
                "rating": 5,
                "published_date": 2012
            }
        }
    }
    