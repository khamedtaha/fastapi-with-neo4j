from fastapi import FastAPI

from myneo4j.functions import create_profile, read_profiles
from myneo4j.config import driver

from models import Profile



app = FastAPI()


@app.get("/")
async def root():
   return {"message": "Hello from FastAPI + Neo4j"}



@app.post("/profiles/")
async def create_profile_endpoint(p: Profile): # p is representing the Profile model
   with driver.session() as session:
      session.execute_write(create_profile, name=p.name, age=p.age, email=p.email)
   return {"message": "Profile created successfully"}

@app.get("/profiles/" ,  response_model=list[Profile])
async def read_profiles_endpoint():
   with driver.session() as session:
      profiles = session.execute_read(read_profiles)
   return {"profiles": profiles}

