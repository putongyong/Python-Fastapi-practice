from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_session
import asyncio
import uvicorn
from infrastructure.models.models import Site, Group
from infrastructure.models.schemas import ResponseGroup, ResponseSite, SiteCreate, GroupCreate

app = FastAPI(title="Python FastAPI Practice")

# Dependency
def get_db():
    db = get_session()
    try:
        yield db
    finally:
        db.close()

# Site CRUD
@app.post("/sites/create/", response_model=ResponseSite, tags=["Site CRUD"])
def create_site(site: SiteCreate, db: Session = Depends(get_db)):
    db_site = Site(**site.dict())
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site

@app.get("/sites/read/{site_id}", response_model=ResponseSite, tags=["Site CRUD"])
def read_site(site_id: int, db: Session = Depends(get_db)):
    db_site = db.query(Site).filter(Site.id == site_id).first()
    if db_site is None:
        raise HTTPException(status_code=404, detail="Site not found")
    return db_site

@app.put("/sites/update/{site_id}", response_model=ResponseSite, tags=["Site CRUD"])
def update_site(site_id: int, site: SiteCreate, db: Session = Depends(get_db)):
    db_site = db.query(Site).filter(Site.id == site_id).first()
    if db_site is None:
        raise HTTPException(status_code=404, detail="Site not found")
    for key, value in site.dict().items():
        setattr(db_site, key, value)
    db.commit()
    db.refresh(db_site)
    return db_site

@app.delete("/sites/delete/{site_id}", response_model=ResponseSite, tags=["Site CRUD"])
def delete_site(site_id: int, db: Session = Depends(get_db)):
    db_site = db.query(Site).filter(Site.id == site_id).first()
    if db_site is None:
        raise HTTPException(status_code=404, detail="Site not found")
    db.delete(db_site)
    db.commit()
    return db_site
    
# Group CRUD
@app.post("/groups/create/", response_model=ResponseGroup, tags=["Group CRUD"])
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    db_group = Group(**group.dict())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

@app.get("/groups/read/{group_id}", response_model=ResponseGroup, tags=["Group CRUD"])
def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = db.query(Group).filter(Group.id == group_id).first()
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group

@app.put("/groups/update/{group_id}", response_model=ResponseGroup, tags=["Group CRUD"])
def update_group(group_id: int, group: GroupCreate, db: Session = Depends(get_db)):
    db_group = db.query(Group).filter(Group.id == group_id).first()
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    for key, value in group.dict().items():
        setattr(db_group, key, value)
    db.commit()
    db.refresh(db_group)
    return db_group

@app.delete("/groups/delete/{group_id}", response_model=ResponseGroup, tags=["Group CRUD"])
def delete_group(group_id: int, db: Session = Depends(get_db)):
    db_group = db.query(Group).filter(Group.id == group_id).first()
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    db.delete(db_group)
    db.commit()
    return db_group

async def main():
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
