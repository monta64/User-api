from fastapi import FastAPI
from app.api.routes import router as api_router
from app.core.config import settings
from app.core.database import create_db_and_tables
app = FastAPI(
    title="Chatbot API",
    description="API to interact with a pretrained chatbot model.",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
app.include_router(api_router, prefix=settings.API_V1_STR)
