import datetime
from peewee import *
from config import db
from playhouse.shortcuts import model_to_dict

class BaseModel(Model):
    class Meta:
        database = db

class Note(BaseModel):
    # CHOICES = [('a','To-Do'), ('b','Doing'), ('Done','Done')]
    CHOICES = ['To-do','Doing','Done']
    
    title = CharField(max_length=200)
    description = TextField()
    deadline = DateField(null=True, default=datetime.date.today)
    create_at = DateTimeField(default=datetime.datetime.now)
    progress = CharField(choices = CHOICES, default='To-do')
    is_doing = BooleanField(default=True)
    
    # class Config:
    #     arbitrary_types_allowed = True
    
    @classmethod
    def get_list(cls):
        query = cls.select().order_by(cls.progress.desc(), cls.create_at.asc()).dicts()
        return list(query)
    
    @classmethod
    def get_note(cls,id):
        query = cls.select().where(cls.id == id).dicts()
        return list(query)
    
    @classmethod
    def create(cls, note: dict):
        new = cls.insert(note).execute()
        new_note = model_to_dict(cls.get_by_id(new))
        return new_note
    
    @classmethod
    def update_note(cls, id, note):
        cls.update(**note).where(cls.id == id).execute()
        newNote = model_to_dict(cls.get_by_id(id))
        return newNote
