from fastapi import APIRouter
from models.note import Note
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from config.db import client
from schema.note import Note_Entity, NotesEntity
from typing import Annotated

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
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict['important'] = True if formDict.get('important') == "on" else False
    note =  client.notes.notes.insert_one(formDict)

    return {"Success": True }

