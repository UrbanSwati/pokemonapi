import json

from app.core.pokemon import get_stats


def test_should_get_pokemon_stats():
    expected = {'hp': 45, 'attack': 49, 'defense': 49, 'special-attack': 65, 'speed': 45}
    with open('./test/mock/json/pokemon.json', 'r') as json_file:
        pokemon_data = json.load(json_file)
    results = get_stats(pokemon_data)

    assert expected == results