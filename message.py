from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/post/{itemid}")
async def post(itemid: str):
    arg = itemid
    return {"message": arg,
            "type": "post"}

@app.put("/put/{itemid}/{updatedValue}")
async def put(itemid: str, updatedValue: str):
    arg = itemid
    val = updatedValue
    return {"item": arg,
            "oldvalue": "Test",
            "newvalue": val}

@app.get("/getmessage")
async def root():
    return {"message": "Hello World"}