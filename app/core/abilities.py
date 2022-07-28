from typing import List

from app.models.pokemon import Ability


def extract_abilities_of_pokemon(
    abilities: dict, lang_code: str = "en"
) -> List[Ability]:
    return [
        filter_ability_effect_by_language(ability, lang_code) for ability in abilities
    ]


def extract_language_text_from_ability(
    ability: dict, field: str, lang_code: str, key: str, default_value: str = ""
):
    fields_found = list(
        filter(lambda ab: ab["language"]["name"] == lang_code, ability.get(field, []))
    )
    if len(fields_found) == 1:
        return fields_found[0][key]
    return default_value


def filter_ability_effect_by_language(ability: dict, lang_code: str = "en") -> Ability:
    ability_effect_description = extract_language_text_from_ability(
        ability, "effect_entries", lang_code, "effect"
    )

    lang_ability_name = extract_language_text_from_ability(
        ability, "names", lang_code, "name", ability.get("name")
    )

    return Ability(name=lang_ability_name, effect=ability_effect_description)
