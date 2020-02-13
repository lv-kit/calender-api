from fastapi import APIRouter, HTTPException
from starlette.requests import Request

router = APIRouter()

@router.get('/', tags=['home'])
def version(request: Request):
  return { "version": "1.0.0" }
