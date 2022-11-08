from fastapi import APIRouter

from .endpoints import api

api_router = APIRouter()
api_router.include_router(api.router, prefix="/foodData", tags=["FoodData"])
