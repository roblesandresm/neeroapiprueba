from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.product import Product as ProductModel
from schemas.product import ProductSchema
from config.database import engine, session
from typing import List

router = APIRouter(
    prefix="/api/products",
    tags=["products"]
)

@router.get("/", response_model=list[ProductSchema])
def get_products() -> List[ProductSchema]:
    db = session()
    result = db.query(ProductModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# endpoint get a product
@router.get("/{id}", tags=["products"], response_model=ProductSchema)
def get_product(id: int = Path(ge=1)) -> ProductSchema:
    db = session()
    result = db.query(ProductModel).filter(ProductModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "product not found"})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

# endpoint create a product
@router.post("/", tags=["products"], response_model=dict, status_code=201)
async def create_products(product: ProductSchema) -> dict:
    # crear una sesion para conectarme a la base de datos
    db = session()
    new_product = ProductModel(**product.dict())
    db.add(new_product)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "product register with success"})

# update a product
@router.put("/{id}", tags=["products"], response_model=dict, status_code=200)
def update_movie(id: int, product: ProductSchema) -> dict:
    db = session()
    result = db.query(ProductModel).filter(ProductModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "product not found"})
    result.name = product.name
    result.image = product.image
    result.tipo = product.tipo
    result.state = product.state
    # seve data
    db.commit()
    return JSONResponse(status_code=200, content={"message": "product update with success"})

# delete product
@router.delete("/{id}", tags=["products"], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    db = session()
    result = db.query(ProductModel).filter(ProductModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "product not found"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "product delete with success"})