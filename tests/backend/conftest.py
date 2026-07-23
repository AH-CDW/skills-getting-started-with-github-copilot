# tests/backend/conftest.py
import copy

from pytest import fixture
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture(autouse=True)
def reset_activities():
    original_state = copy.deepcopy(activities)
    activities.clear()
    activities.update(copy.deepcopy(original_state))
    yield
    activities.clear()
    activities.update(copy.deepcopy(original_state))


@pytest.fixture()
def client():
    with TestClient(app) as test_client:
        yield test_client