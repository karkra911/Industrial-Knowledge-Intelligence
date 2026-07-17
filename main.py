from fastapi import FastAPI
from routes import router

app = FastAPI(title="Industrial Knowledge Intelligence")

app.include_router(router)

@app.get("/")
def home():
    return {
        "project": "Industrial Knowledge Intelligence",
        "status": "running"
    }
