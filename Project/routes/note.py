from fastapi import APIRouter
from models.note import Note
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from config.db import client
from schema.note import Note_Entity, NotesEntity

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/")
async def read_item(request: Request):
    docs = client.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc['_id'],
            "title": doc['title'],
            "desc": doc['desc'],
            "important": doc['important'],
        })
    print(newDocs)
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})
    
@note.post('/')
def add_note(note: Note):
    inserted_note = client.notes.notes.insert_one(dict(note))
    return Note_Entity(inserted_note)

@note.post('/')
async def create_item(request: Request):
    form = await request.form()
    print(form)
    formDict = dict(form)
    formDict['important'] = True if formDict['important'] == "on" else False
    note = client.notes.notes.insert_one(form)

    return {"Success": True }

