import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import cultivo_routers


app = FastAPI()
app.include_router(cultivo_routers.router)

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # quién puede hacer peticiones
    allow_credentials=True,
    allow_methods=["*"],             # permite todos los métodos: GET, POST, PUT, DELETE
    allow_headers=["*"],             # permite todas las cabeceras
)