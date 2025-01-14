import os.path

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    message_file: str = 'message.txt'
    message = ''
    if os.path.exists(message_file):
        with open(message_file) as file:
            for line in file:
                message = f'{message} {line}'
    else:
        message = 'default'

    return {"message": f"Hello World {message}"}


@app.get("/posts")
async def get_posts():
    return [{"id": 1, "title": "First Post", "content": "This is the content of the first post."}]


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8081)
