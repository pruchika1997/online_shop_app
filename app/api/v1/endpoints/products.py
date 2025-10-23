from fastapi import APIRouter
from app.schemas.product import Product
from app.models.product import ProductModel

router = APIRouter()

products_db: list[ProductModel] = []

@router.post("/", response_model=Product)
def create_product(product: Product):
    products_db.append(ProductModel(**product.dict()))
    return product

@router.get("/", response_model=list[Product])
def list_products():
    return products_db
