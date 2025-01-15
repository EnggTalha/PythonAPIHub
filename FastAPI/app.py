import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return('message','Hello , Talha' )

app.get('/Welcome')
def get_name(name:str):
    return {'Welcome here':f'{name}'}


if __name__ =='__main__':
    uvicorn.run(app,host='127.0,0,1',port=8000)