from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

class AssetType(str, Enum):
    SERVER = "server"
    DATABASE = "database"
    SECURITY_TOOL = "security_tool"
    OTHER = "other"

class VulnerabilityBase(BaseModel):
    severity: str
    description: str
    status: str

class VulnerabilityCreate(VulnerabilityBase):
    pass

class Vulnerability(VulnerabilityBase):
    id: int
    asset_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class AssetBase(BaseModel):
    name: str
    type: AssetType
    description: Optional[str] = None
    status: Optional[str] = None
    ip_address: Optional[str] = None

class AssetCreate(AssetBase):
    pass

class Asset(AssetBase):
    id: int
    created_at: datetime
    updated_at: datetime
    vulnerabilities: List[Vulnerability] = []

    class Config:
        from_attributes = True
