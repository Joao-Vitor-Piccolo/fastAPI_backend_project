import pytest

from src.fastapi_course.app import app
from fastapi.testclient import TestClient


@pytest.fixture()
def client():
    return TestClient(app)
