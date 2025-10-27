from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.order import Order, OrderCreate
from app.models.order import Order as OrderModel
from app.db.deps import get_db
from app.core.auth import get_current_user  # ✅ import

router = APIRouter()

@router.post("/", response_model=Order)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    db_order = OrderModel(user_id=order.user_id, total_price=order.total_price)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/", response_model=list[Order])
def list_orders(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    return db.query(OrderModel).all()
