from fastapi import FastAPI
import uvicorn
from routes import user, product, briefcase, establecimient
from config.database import engine
from sqlmodel import SQLModel

app = FastAPI(title="Api POS", version="0.0.1")

SQLModel.metadata.create_all(engine)

# register of routes
app.include_router(user.router)
app.include_router(product.router)
app.include_router(briefcase.router)
app.include_router(establecimient.router)

@app.get("/")
async def root():
    return {"message": "Welcome ApiRest"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)