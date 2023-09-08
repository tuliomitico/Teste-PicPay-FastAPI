from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from src.server import app
@pytest.fixture
def app_test():
    yield app

@pytest.fixture
def client(app_test: FastAPI):
    return TestClient(app_test)