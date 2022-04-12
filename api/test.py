from fastapi import APIRouter, HTTPException
from api.models import MovieIn,MovieOut
from typing import List
from api import db_manager
movies=APIRouter() #регистрация нового маршрута API


