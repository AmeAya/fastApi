from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
from fastapi.encoders import jsonable_encoder
import json

app = FastAPI()

@app.get('/app', response_class=HTMLResponse)
def searchApp(app_name):
    return app_name

@app.get('/', response_class=FileResponse)
def main():
    return 'site.html'
