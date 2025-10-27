# ---- Base Image ----
    FROM python:3.11-slim

    # ---- Set Workdir ----
    WORKDIR /app
    
    # ---- Copy Requirements ----
    COPY requirements.txt .
    
    # ---- Install Dependencies ----
    RUN pip install --no-cache-dir -r requirements.txt
    
    # ---- Copy App Files ----
    COPY . .
    
    # ---- Expose Port ----
    EXPOSE 8000
    
    # ---- Start Command ----
    CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
    