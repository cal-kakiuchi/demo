from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
async def hello():
    response = {
        'message': 'Hello World!'
    }
    return response