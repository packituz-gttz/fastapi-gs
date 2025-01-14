from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World 3"}

@app.get("/posts")
async def get_posts():
    return [{"id": 1, "title": "First Post", "content": "This is the content of the first post."}]