from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.establecimient import Establecimient as EstablecimientModel
from schemas.establecimient import EstablecimientSchema
from config.database import session
from typing import List

router = APIRouter(
    prefix="/api/establecimients",
    tags=["establecimients"]
)

# get establecimients
@router.get("/", response_model=list[EstablecimientSchema])
def get_establecimients() -> List[EstablecimientSchema]:
    db = session()
    result = db.query(EstablecimientModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# get an establecimient 
@router.get("/{id}", response_model=EstablecimientSchema)
def get_establecimient(id: int = Path(ge=1))-> EstablecimientSchema:
    db = session()
    result = db.query(EstablecimientModel).filter(EstablecimientModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "establecimient not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# create establecimients
@router.post("/", tags=["establecimients"], response_model=dict, status_code=201)
def create_establecimients(establecimient: EstablecimientSchema):
    # crear una sesion para conectarme a la base de datos
    db = session()
    new_establecimient = EstablecimientModel(**establecimient.dict())
    db.add(new_establecimient)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Se ha registro el establecimiento"})

@router.put("/{id}", tags=["establecimients"], response_model=dict, status_code=200)
def update_establecimient(id: int, establecimient: EstablecimientSchema) -> dict:
    db = session()
    result = db.query(EstablecimientModel).filter(EstablecimientModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "establecimient not found"})
    result.first_name = establecimient.name
    result.last_name = establecimient.ciudad
    result.dni = establecimient.briefcase_id
    result.email = establecimient.state
    # seve data
    db.commit()
    return JSONResponse(status_code=200, content={"message": "establecimient update with success"})

@router.delete("/{id}", tags=["establecimients"], response_model=dict, status_code=200)
def delete_establecimient(id: int) -> dict:
    db = session()
    result = db.query(EstablecimientModel).filter(EstablecimientModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "establecimient not found"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "establecimient delete with success"})