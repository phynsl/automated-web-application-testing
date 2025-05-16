import pytest
from containers.browser_container import ChromeContainer
from containers.postgres_container import PostgresTestContainer
from containers.mock_api_container import MockApiContainer

@pytest.fixture(scope="session")
def browser():
    chrome = ChromeContainer()
    driver = chrome.start()
    yield driver
    chrome.stop()

@pytest.fixture(scope="session")
def db_connection():
    db = PostgresTestContainer()
    connection = db.start()
    yield connection
    db.stop()

@pytest.fixture(scope="session")
def mock_api():
    mock = MockApiContainer()
    url = mock.start()
    yield url
    mock.stop()
