from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.product import Product, ProductCreate
from app.models.product import Product as ProductModel
from app.db.deps import get_db
from app.core.auth import get_current_user  # ✅ import

router = APIRouter()

@router.post("/", response_model=Product)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),  # ✅ only logged-in users
):
    db_product = ProductModel(name=product.name, description=product.description, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/", response_model=list[Product])
def list_products(db: Session = Depends(get_db)):
    return db.query(ProductModel).all()
