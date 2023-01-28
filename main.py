from fastapi import FastAPI
import uvicorn
from routes import user, product, briefcase
from config.database import engine, Base, Session

app = FastAPI(title="Api POS", version="0.0.1")

Base.metadata.create_all(bind=engine)
db = Session()
db.close()

# register of routes
app.include_router(user.router)
app.include_router(product.router)
app.include_router(briefcase.router)

@app.get("/")
async def root():
    return {"message": "Welcome ApiRest"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)