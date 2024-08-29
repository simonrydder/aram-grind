import pytest

from src.lol.champion_data import ChampionData


@pytest.fixture
def aatrox_dict():
    data = {
        "version": "14.17.1",
        "id": "Aatrox",
        "key": "266",
        "name": "Aatrox",
        "title": "the Darkin Blade",
        "blurb": "Once honored defenders of Shurima against the Void, Aatrox and his brethren would eventually become an even greater threat to Runeterra, and were defeated only by cunning mortal sorcery. But after centuries of imprisonment, Aatrox was the first to find...",
        "info": {"attack": 8, "defense": 4, "magic": 3, "difficulty": 4},
        "image": {
            "full": "Aatrox.png",
            "sprite": "champion0.png",
            "group": "champion",
            "x": 0,
            "y": 0,
            "w": 48,
            "h": 48,
        },
        "tags": ["Fighter"],
        "partype": "Blood Well",
        "stats": {
            "hp": 650,
            "hpperlevel": 114,
            "mp": 0,
            "mpperlevel": 0,
            "movespeed": 345,
            "armor": 38,
            "armorperlevel": 4.8,
            "spellblock": 32,
            "spellblockperlevel": 2.05,
            "attackrange": 175,
            "hpregen": 3,
            "hpregenperlevel": 0.5,
            "mpregen": 0,
            "mpregenperlevel": 0,
            "crit": 0,
            "critperlevel": 0,
            "attackdamage": 60,
            "attackdamageperlevel": 5,
            "attackspeedperlevel": 2.5,
            "attackspeed": 0.651,
        },
    }

    yield data


@pytest.fixture
def ahri_dict():
    data = {
        "version": "14.17.1",
        "id": "Ahri",
        "key": "103",
        "name": "Ahri",
        "title": "the Nine-Tailed Fox",
        "blurb": "Innately connected to the magic of the spirit realm, Ahri is a fox-like vastaya who can manipulate her prey's emotions and consume their essence—receiving flashes of their memory and insight from each soul she consumes. Once a powerful yet wayward...",
        "info": {"attack": 3, "defense": 4, "magic": 8, "difficulty": 5},
        "image": {
            "full": "Ahri.png",
            "sprite": "champion0.png",
            "group": "champion",
            "x": 48,
            "y": 0,
            "w": 48,
            "h": 48,
        },
        "tags": ["Mage", "Assassin"],
        "partype": "Mana",
        "stats": {
            "hp": 590,
            "hpperlevel": 104,
            "mp": 418,
            "mpperlevel": 25,
            "movespeed": 330,
            "armor": 21,
            "armorperlevel": 4.7,
            "spellblock": 30,
            "spellblockperlevel": 1.3,
            "attackrange": 550,
            "hpregen": 2.5,
            "hpregenperlevel": 0.6,
            "mpregen": 8,
            "mpregenperlevel": 0.8,
            "crit": 0,
            "critperlevel": 0,
            "attackdamage": 53,
            "attackdamageperlevel": 3,
            "attackspeedperlevel": 2.2,
            "attackspeed": 0.668,
        },
    }

    yield data


@pytest.fixture
def aatrox(aatrox_dict):
    yield ChampionData(**aatrox_dict)


@pytest.fixture
def ahri(ahri_dict):
    yield ChampionData(**ahri_dict)


@pytest.fixture
def data_dict(aatrox_dict, ahri_dict):
    dct = {
        "version": "14.14.1",
        "format": "standAloneComplex",
        "type": "champion",
        "data": {"Aatrox": aatrox_dict, "Ahri": ahri_dict},
    }

    yield dct
