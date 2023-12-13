from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()
client = MongoClient('mongodb+srv://user0123:Q1Dj8l4WmgLfLagK@cluster0.wyyqioj.mongodb.net/')

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
    
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # docs = client.notes.notes.find_one({})
    docs = client.notes.notes.find({})
    # print([doc for doc in docs])
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc['_id'],
            "note": doc['note']
        })
    return templates.TemplateResponse("index.html", {"request": request, newDocs: newDocs})