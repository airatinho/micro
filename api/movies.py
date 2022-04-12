from fastapi import APIRouter, HTTPException
from api.models import MovieIn,MovieOut
from typing import List
from api import db_manager
movies=APIRouter() #регистрация нового маршрута API


@movies.get("/",response_model=List[MovieOut])
async def index():
    return await db_manager.get_all_movies()

@movies.post("/",status_code=201)
async def add_movie(payload:MovieIn):
    mov=await db_manager.add_movie(payload)
    response={
        "id":mov,
        **payload.dict()
    }
    return response

@movies.put("/{id}")
async def update_movie(id:int,payload:MovieIn):
    mov=await db_manager.get_movie(id)
    if not mov:
        raise HTTPException(status_code=404,detail="Movie is not found")
    update_data = payload.dict(exclude_unset=True)
    movie_in_db=MovieIn(**mov)
    updated_movie=movie_in_db.copy(update=update_data)
    return await db_manager.update_movie(id,updated_movie)

@movies.delete("/{id}")
async def delete_movie(id:int):
    mov = await db_manager.get_movie(id)
    if not mov:
        raise HTTPException(status_code=404,detail="Movie is not found")
    return await db_manager.delete_movie(id)

