from fastapi import Path,Query
import fastapi
from pydantic import BaseModel
from typing import Optional,List

router=fastapi.APIRouter()

users=[]

class User(BaseModel):
    email:str
    is_active:bool
    bio:Optional[str]



@router.get('/users',response_model=List[User])
async def get_user():
    return users

@router.post('/users')
async def create_user(user:User):
    users .append(user)
    return "sucess"

@router.get("/users/{id}")
async def get_user(id:int = Path(...,description="The ID of user to retrieve",gt=2),q:str=Query(None,max_length=5)):
    if id < 0 or id >= len(users):
        return {"error": "User not found"}
    return {"user": users[id], "query": q}



