from fastapi import FastAPI, Response
import models
import schemas
import config
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://thinh.com:90",
    "http://meomeo.thinh.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

config.db.connect()
# config.db.drop_tables([models.Note])
config.db.create_tables([models.Note])
config.db.close()

@app.get('/test')
def test():
    return {'data': 'test'}

@app.get('/notes', response_model=list[schemas.Note])
def notes():
    return models.Note.get_list()

@app.get('/notes/{id}', response_model=list[schemas.Note])
def note(id: int):
    return models.Note.get_note(id)

@app.delete('/notes/{id}')
def delete_note(id: int):
    models.Note.delete_by_id(pk=id)
    return Response(status_code=204)

@app.patch('/notes/{id}')
def update_note(id: int, note: schemas.Note):
    note = note.dict()
    return models.Note.update_note(id, note)

@app.post('/notes', response_model=schemas.Note)
def create_note(note: schemas.NoteCreate):
    return models.Note.create(note.dict())

    