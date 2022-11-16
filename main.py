from fastapi import FastAPI, Body
from fastapi.responses import FileResponse

app = FastAPI()

@app.post('/hello')
def sayHello(data=Body()):
    name = data['name']
    surname = data['surname']
    return {'message': 'Hello ' + str(name) + ' ' + str(surname)}

@app.get('/', response_class=FileResponse)
def main():
    return 'site.html'
