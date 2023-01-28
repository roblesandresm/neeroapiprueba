from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Api POS", version="0.0.1")

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)