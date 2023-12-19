from pydantic import BaseModel, HttpUrl
from typing import List, Dict, Optional
from datetime import datetime

class WebPageSummary(BaseModel):
    author: Optional[str] = None
    title: str
    content: str
    datetime: Optional[datetime] = None
    tags: Optional[List[str]] = None
    url: Optional[HttpUrl] = None
