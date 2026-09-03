import pytest

from clients.api_client import Apiclient

@pytest.fixture(scope='session')
def base_url():
    return 'http://localhost:3000'

@pytest.fixture()
def api_client(base_url):
    client = Apiclient(base_url)
    yield client
    client.close()