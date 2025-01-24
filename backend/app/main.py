from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import assets, vulnerabilities
from app.core.database import engine
from app.models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Security Asset Dashboard API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(assets.router, prefix="/api/v1", tags=["assets"])
app.include_router(vulnerabilities.router, prefix="/api/v1", tags=["vulnerabilities"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Security Asset Dashboard API"}
