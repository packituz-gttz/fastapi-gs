import os.path

from fastapi import FastAPI
from content import utils

app = FastAPI()


import os

@app.get("/")
async def root():
    files = os.listdir('./content/repo/')
    return {
        "files": files,
    }



@app.get("/posts")
async def get_posts():
    return utils.message()


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8081)
