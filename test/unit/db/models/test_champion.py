# import pytest
# from sqlalchemy.exc import IntegrityError

# from src.db.models.champion import Champion, create_champion


# @pytest.fixture
# def aatrox():
#     yield {"name": "Aatrox"}


# @pytest.fixture
# def ahri():
#     yield {"name": "Ahri"}


# def test_create_champion(session, aatrox):
#     a = Champion(**aatrox)
#     create_champion(session, a)

#     assert a.id == 1


# def test_create_multiple_champions(session, aatrox, ahri):
#     a = Champion(**aatrox)
#     b = Champion(**ahri)

#     create_champion(session, a)
#     create_champion(session, b)

#     assert b.id == 2


# def test_name_is_unique(session, aatrox):
#     a = Champion(**aatrox)
#     b = Champion(**aatrox)

#     with pytest.raises(IntegrityError):
#         create_champion(session, a)
#         create_champion(session, b)
