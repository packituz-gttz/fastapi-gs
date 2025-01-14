import os.path

from fastapi import FastAPI

app = FastAPI()


import os

@app.get("/")
async def root():
    files = os.listdir('.')
    return {
        "files": files,
        "current_directory": os.getcwd()
    }



@app.get("/posts")
async def get_posts():
    return [{"id": 1, "title": "First Post", "content": "This is the content of the first post."}]


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8081)
