# from src.utils.lol import get_data_url, get_latest_versions
# from src.utils.lol import Language


# def test_that_latest_version_is_14_17_1():
#     versions = ["14.17.1", "14.16.1", "13.20.3", "lolpatch_7.19"]

#     latest = get_latest_version(versions)

#     assert latest == "14.17.1"


# def test_that_latest_version_is_14_16_1():
#     versions = ["14.16.1", "13.20.3", "lolpatch_7.19"]

#     latest = get_latest_version(versions)
#     assert latest == "14.16.1"


# def test_data_url_for_version_14_16_1_language_us():
#     version = "14.16.1"
#     lang = Language.US

#     url = get_data_url(version, lang)
#     assert (
#         url
#         == "https://ddragon.leagueoflegends.com/cdn/14.16.1/data/en_US/champion.json"
#     )


# def test_data_url_for_version_14_17_1_language_us():
#     version = "14.17.1"
#     lang = Language.US

#     url = get_data_url(version, lang)

#     assert (
#         url
#         == "https://ddragon.leagueoflegends.com/cdn/14.17.1/data/en_US/champion.json"
#     )


# def test_data_url_for_language_fr():
#     version = "14.17.1"
#     lang = Language.FR

#     url = get_data_url(version, lang)

#     assert (
#         url
#         == "https://ddragon.leagueoflegends.com/cdn/14.17.1/data/fr_FR/champion.json"
#     )
