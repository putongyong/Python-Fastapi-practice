# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_session
import asyncio
import uvicorn
from infrastructure.models.models import Site, Group
from infrastructure.models.schemas import ResponseGroup, ResponseSite, SiteCreate, GroupCreate  # Import the new schemas

app = FastAPI(title="Python technical test")

# Dependency
def get_db():
    db = get_session()
    try:
        yield db
    finally:
        db.close()

@app.post("/sites/", response_model=ResponseSite)
def create_site(site: SiteCreate, db: Session = Depends(get_db)):
    db_site = Site(**site.dict())
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site

@app.get("/sites/{site_id}", response_model=ResponseSite)
def read_site(site_id: int, db: Session = Depends(get_db)):
    db_site = db.query(Site).filter(Site.id == site_id).first()
    if db_site is None:
        raise HTTPException(status_code=404, detail="Site not found")
    return db_site

@app.post("/groups/", response_model=ResponseGroup)
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    db_group = Group(**group.dict())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

@app.get("/groups/{group_id}", response_model=ResponseGroup)
def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = db.query(Group).filter(Group.id == group_id).first()
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group

async def main():
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
