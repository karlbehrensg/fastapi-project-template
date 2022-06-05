import os
import pytest
from dotenv import load_dotenv
from config import get_settings


@pytest.fixture(scope="module")
def load_env_variables():
    load_dotenv()


@pytest.fixture(scope="session")
def config_test():
    settings = get_settings()
    settings.env_mode = "test"
    return settings
