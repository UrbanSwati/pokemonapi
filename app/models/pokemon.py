from typing import List

from pydantic import BaseModel, HttpUrl


class Ability(BaseModel):
    name: str
    effect: str


class Pokemon(BaseModel):
    name: str
    height: int
    weight: int
    experience: int
    health: int
    attack: int
    special_attack: int
    defense: int
    speed: int
    picture_url: HttpUrl
    abilities: List[Ability] = []
