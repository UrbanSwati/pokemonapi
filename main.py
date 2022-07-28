from fastapi import FastAPI

from app.router import pokemon, health

app = FastAPI(
    title="Pokemon API",
    contact={"name": "Developer", "email": "williesdk@gmail.com"},
    description="Your cool Pokemon API made easy, thanks to https://pokeapi.co/api/v2/",
    version="1.0.0",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0",
    },
)

API_V1 = "/api/v1"

app.include_router(health.router, prefix=API_V1, tags=["Pokemon"])
app.include_router(pokemon.router, prefix=API_V1, tags=["Pokemon"])
