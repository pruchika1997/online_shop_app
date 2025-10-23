from fastapi import APIRouter
from app.schemas.order import Order
from app.models.order import OrderModel

router = APIRouter()

orders_db: list[OrderModel] = []

@router.post("/", response_model=Order)
def create_order(order: Order):
    orders_db.append(OrderModel(**order.dict()))
    return order

@router.get("/", response_model=list[Order])
def list_orders():
    return orders_db
