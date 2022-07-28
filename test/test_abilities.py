from app.core.abilities import (
    filter_ability_effect_by_language,
    extract_abilities_of_pokemon,
)
from app.models.pokemon import Ability
from test.mock.abilities_details import abilities_details_mock
from test.mock.ability_detail import ability_detail_mock


def test_filter_ability_by_language():
    expected = Ability(
        name="Overgrow",
        effect="When this Pokémon has 1/3 or less of its HP remaining, "
        "its grass-type moves inflict 1.5× as much regular damage.",
    )

    results = filter_ability_effect_by_language(ability_detail_mock)
    assert expected == results


def test_filter_ability_by_given_language_code():
    expected = Ability(
        name="Notdünger",
        effect="Wenn ein Pokémon mit dieser Fähigkeit nur noch 1/3 seiner maximalen "
        "hp oder weniger hat, werden all seine grass Attacken verstärkt, "
        "so dass sie 1,5× so viel regular damage anrichten wie sonst.",
    )

    # when given different language code
    results = filter_ability_effect_by_language(ability_detail_mock, "de")

    # should return language description
    assert expected == results


def test_extract_abilities_of_pokemon():
    expected = [
        Ability(
            name="Overgrow",
            effect="When this Pokémon has 1/3 or less of its HP remaining, "
            "its grass-type moves inflict 1.5× as much regular damage.",
        ),
        Ability(
            name="Chlorophyll",
            effect="This Pokémon's Speed is doubled during strong sunlight."
            "\n\nThis bonus does not count as a stat modifier.",
        ),
    ]

    results = extract_abilities_of_pokemon(abilities_details_mock)

    assert expected == results
