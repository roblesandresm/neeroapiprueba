from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.user import UserSchema
from models.user import UserModel
from config.database import engine, Session
from typing import List

router = APIRouter(
    prefix="/api/users",
    tags=["users"]
)

# endpoint get all users
@router.get("/")
async def get_users() -> List[UserSchema]:
    db = Session()
    result = db.query(UserModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# endpoint get an user
@router.get("/{id}", tags=["users"], response_model=UserSchema)
def get_user(id: int = Path(ge=1)) -> UserSchema:
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "user not found"})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

# endpoint create user
@router.post("/", tags=["users"], response_model=dict, status_code=201)
async def create_users(user: UserSchema) -> dict:
    # crear una sesion para conectarme a la base de datos
    db = Session()
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    #users.append(jsonable_encoder(user))
    return JSONResponse(status_code=201, content={"message": "Se ha registro el usuario"})

# update a user
@router.put("/{id}", tags=["users"], response_model=dict, status_code=200)
def update_movie(id: int, user: UserSchema) -> dict:
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "user not found"})
    result.first_name = user.first_name
    result.last_name = user.last_name
    result.dni = user.dni
    result.email = user.email
    result.password = user.password
    result.state = user.state
    # seve data
    db.commit()
    return JSONResponse(status_code=200, content={"message": "user update with success"})

# delete user
@router.delete("/{id}", tags=["users"], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "user not found"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "user delete with success"})

