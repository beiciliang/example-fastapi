
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote

""" Commented out since we use alembic 
# Create the table defined in the models if not exists
models.Base.metadata.create_all(bind=engine)
""" 

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Successfully deployed from CI/CD pipeline!"}


""" Test if squlalchemy is working

from sqlalchemy.orm import Session
from fastapi import Depends
from .database import get_db

@app.get("/sqlalchemy")        
def test_posts(db: Session = Depends(get_db)):
    # db.query() is actually a SQL query if you print it 
    posts = db.query(models.Post).all()
    return {"data": posts}
"""