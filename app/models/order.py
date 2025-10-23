from pydantic import BaseModel
from typing import List

class OrderModel(BaseModel):
    id: int
    user_id: int
    product_ids: List[int]
    total_price: float
