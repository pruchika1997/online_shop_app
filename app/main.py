from fastapi import FastAPI
from .api.v1.endpoints import users, products, orders, auth
from app.db.session import engine, Base

app = FastAPI(title="Online Shop App")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Welcome to the Shop App API!"}


app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(products.router, prefix="/api/v1/products", tags=["Products"])
app.include_router(orders.router, prefix="/api/v1/orders", tags=["Orders"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])