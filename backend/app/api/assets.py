from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.database import get_db
from app.models import models
from app.schemas import schemas
from sqlalchemy import or_

router = APIRouter()

@router.post("/assets/", response_model=schemas.Asset)
def create_asset(asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    db_asset = models.Asset(**asset.model_dump())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

@router.get("/assets/", response_model=List[schemas.Asset])
def get_assets(
    skip: int = 0,
    limit: int = 100,
    search: Optional[str] = None,
    asset_type: Optional[str] = None,
    sort_order: Optional[str] = "desc",
    db: Session = Depends(get_db)
):
    query = db.query(models.Asset)
    
    if search:
        query = query.filter(
            or_(
                models.Asset.name.ilike(f"%{search}%"),
                models.Asset.description.ilike(f"%{search}%")
            )
        )
    
    if asset_type and asset_type != "all":
        query = query.filter(models.Asset.type == asset_type)
    
    if sort_order == "asc":
        query = query.order_by(models.Asset.created_at.asc())
    else:
        query = query.order_by(models.Asset.created_at.desc())
    
    return query.offset(skip).limit(limit).all()

@router.get("/assets/{asset_id}", response_model=schemas.Asset)
def get_asset(asset_id: int, db: Session = Depends(get_db)):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset

@router.put("/assets/{asset_id}", response_model=schemas.Asset)
def update_asset(asset_id: int, asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    
    for key, value in asset.model_dump().items():
        setattr(db_asset, key, value)
    
    db.commit()
    db.refresh(db_asset)
    return db_asset

@router.delete("/assets/{asset_id}")
def delete_asset(asset_id: int, db: Session = Depends(get_db)):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    
    db.delete(db_asset)
    db.commit()
    return {"message": "Asset deleted successfully"}
