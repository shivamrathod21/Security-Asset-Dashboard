from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models import models
from app.schemas import schemas

router = APIRouter()

@router.post("/assets/{asset_id}/vulnerabilities/", response_model=schemas.Vulnerability)
def create_vulnerability(
    asset_id: int,
    vulnerability: schemas.VulnerabilityCreate,
    db: Session = Depends(get_db)
):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    
    db_vulnerability = models.Vulnerability(**vulnerability.model_dump(), asset_id=asset_id)
    db.add(db_vulnerability)
    db.commit()
    db.refresh(db_vulnerability)
    return db_vulnerability

@router.get("/assets/{asset_id}/vulnerabilities/", response_model=List[schemas.Vulnerability])
def get_vulnerabilities(asset_id: int, db: Session = Depends(get_db)):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset.vulnerabilities

@router.get("/vulnerabilities/{vulnerability_id}", response_model=schemas.Vulnerability)
def get_vulnerability(vulnerability_id: int, db: Session = Depends(get_db)):
    db_vulnerability = db.query(models.Vulnerability).filter(models.Vulnerability.id == vulnerability_id).first()
    if db_vulnerability is None:
        raise HTTPException(status_code=404, detail="Vulnerability not found")
    return db_vulnerability

@router.put("/vulnerabilities/{vulnerability_id}", response_model=schemas.Vulnerability)
def update_vulnerability(
    vulnerability_id: int,
    vulnerability: schemas.VulnerabilityCreate,
    db: Session = Depends(get_db)
):
    db_vulnerability = db.query(models.Vulnerability).filter(models.Vulnerability.id == vulnerability_id).first()
    if db_vulnerability is None:
        raise HTTPException(status_code=404, detail="Vulnerability not found")
    
    for key, value in vulnerability.model_dump().items():
        setattr(db_vulnerability, key, value)
    
    db.commit()
    db.refresh(db_vulnerability)
    return db_vulnerability

@router.delete("/vulnerabilities/{vulnerability_id}")
def delete_vulnerability(vulnerability_id: int, db: Session = Depends(get_db)):
    db_vulnerability = db.query(models.Vulnerability).filter(models.Vulnerability.id == vulnerability_id).first()
    if db_vulnerability is None:
        raise HTTPException(status_code=404, detail="Vulnerability not found")
    
    db.delete(db_vulnerability)
    db.commit()
    return {"message": "Vulnerability deleted successfully"}
