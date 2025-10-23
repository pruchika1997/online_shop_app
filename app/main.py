from fastapi import FastAPI
from .api.v1.endpoints import users, products, orders

app = FastAPI(title="Online Shop App")

app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(products.router, prefix="/api/v1/products", tags=["Products"])
app.include_router(orders.router, prefix="/api/v1/orders", tags=["Orders"])