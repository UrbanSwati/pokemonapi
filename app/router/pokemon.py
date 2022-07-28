import asyncio
from typing import List

import aiohttp
from fastapi import APIRouter, status
from pydantic import HttpUrl

from app.core.abilities import extract_abilities_of_pokemon
from app.core.pokemon import get_stats, extract_pokemon_model
from app.models.pokemon import Pokemon
from app.util import fetch

router = APIRouter()


@router.get("/pokemon", response_model=List[Pokemon], status_code=status.HTTP_200_OK)
async def get_all_pokemons(offset: int = 0, limit: int = 20, lang: str = "en"):
    async with aiohttp.ClientSession() as session:
        response = await fetch(
            session, f"https://pokeapi.co/api/v2/pokemon/?offset={offset}&limit={limit}"
        )
        pokemon_url_list = list(
            map(lambda res: res.get("url"), response.get("results", []))
        )
        raw_pokemon_data = await asyncio.gather(
            *[fetch(session, url) for url in pokemon_url_list], return_exceptions=False
        )

        pokemons = await asyncio.gather(
            *[
                extract_pokemon_model(raw_pokemon, session, lang)
                for raw_pokemon in raw_pokemon_data
            ],
            return_exceptions=False,
        )
    return pokemons
