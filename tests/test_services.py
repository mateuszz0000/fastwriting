import pytest
from unittest.mock import patch
from tests.fixtures.redis import redis_instance, redis_with_game
from tests.fixtures.db import session, db
from src.services import new_game_in_redis, create_level


@pytest.mark.asyncio
async def test_create_new_game(redis_instance):
    await new_game_in_redis("test_username")

    game_obj = await redis_instance.hgetall(f"{hash('test_username')}_test_username", encoding='utf-8')

    assert game_obj
    assert game_obj['started']
    # TODO: more tests if game hash will be bigger


@pytest.mark.asyncio
@patch('src.database.base.SessionLocal')
@patch('src.database.operations.query_random_words')
async def test_create_first_level(mock_session, redis_with_game):
    # TODO: FINISH IT
    await create_level(mock_session, "test_game", stage=1)
    level_obj = await redis_with_game.hgetall("test_game", encoding='utf-8')

    assert level_obj['stage'] == 1
    assert level_obj['timeout'] == 120
    assert len(level_obj['words']) == 60