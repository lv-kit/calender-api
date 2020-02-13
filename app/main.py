from fastapi import FastAPI
from .routers import home

app = FastAPI(
  title = 'calender api',
  description = 'calender api',
  version = '1.0.0'
)

app.include_router(home.router)
