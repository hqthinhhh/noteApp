import datetime
from pydantic import BaseModel

class Note(BaseModel):
    id: int
    title: str
    description: str
    deadline: datetime.date
    create_at: datetime.datetime
    progress: str
    is_doing: bool


class NoteCreate(BaseModel):
    title: str
    description: str
    deadline: datetime.date
    progress: str
    