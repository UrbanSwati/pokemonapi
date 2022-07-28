import asyncio

import aiohttp

from app.core.abilities import extract_abilities_of_pokemon
from app.models.pokemon import Pokemon
from app.util import fetch


def get_stats(pokemon: dict) -> dict:
    pokemon_stat = {}
    required_stats = ["hp", "defense", "attack", "special-attack", "speed"]
    for stat in pokemon.get("stats", []):
        stat_name = stat["stat"]["name"]
        if stat_name in required_stats:
            pokemon_stat[stat_name] = stat["base_stat"]
    return pokemon_stat


async def extract_pokemon_model(
    raw_pokemon: dict, session: aiohttp.ClientSession, lang: str
) -> Pokemon:
    pokemon_abilities = raw_pokemon.get("abilities", [])
    pokemon_abilities_urls = list(
        map(
            lambda pokemon_dict: pokemon_dict.get("ability", {}).get("url"),
            pokemon_abilities,
        )
    )
    abilities_details = await asyncio.gather(
        *[fetch(session, url) for url in pokemon_abilities_urls],
        return_exceptions=False
    )

    abilities = extract_abilities_of_pokemon(abilities_details, lang_code=lang)

    stats = get_stats(raw_pokemon)

    pokemon_dict = {
        **raw_pokemon,
        **stats,
        "experience": raw_pokemon.get("base_experience"),
        "health": stats.get("hp"),
        "special_attack": stats.get("special-attack"),
        "picture_url": raw_pokemon["sprites"]["front_default"],
    }

    pokemon_dict.pop("abilities")
    return Pokemon(**pokemon_dict, abilities=abilities)
