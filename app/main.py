from fastapi import FastAPI
from app.routes import users, riesgos, proyectos, clientes

app = FastAPI(title="Risk Manager API")

app.include_router(users.router)
app.include_router(riesgos.router)
app.include_router(proyectos.router)
app.include_router(clientes.router)
