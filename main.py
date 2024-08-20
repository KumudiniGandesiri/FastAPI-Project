from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/")
def root():
    return{"message":"Hello World"}


@app.get("/posts")
def get_posts():
    return{"data":"This is youre posts"}