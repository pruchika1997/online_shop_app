# Shop App

This is a scalable FastAPI project for an e-commerce platform.

## Run the app
```bash
uvicorn app.main:app --reload

## generate first migration
```bash
alembic revision --autogenerate -m "initial migration"
