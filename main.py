from fastapi import FastAPI
import uvicorn
from routes import user
from config.database import engine, Base, Session

app = FastAPI(title="Api POS", version="0.0.1")

Base.metadata.create_all(bind=engine)
db = Session()
db.close()

app.include_router(user.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)