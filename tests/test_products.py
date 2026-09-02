import requests
import pytest


def test_homepage_is_available(base_url):
    response = requests.get(base_url,timeout=10)
    assert response.status_code == 200

@pytest.mark.parametrize('keyword',['apple','banana'])
def test_search_products_returns_results(base_url,keyword):
    response = requests.get(f"{base_url}/rest/products/search",
                            params={"q":keyword},
                            timeout=10)
    body = response.json()

    assert response.status_code == 200
    assert body["status"] == "success"
    assert isinstance(body["data"],list)
    assert len(body["data"])>0

    for product in body["data"]:
        assert isinstance(product['id'],int)
        assert isinstance(product['name'],str)
        assert isinstance(product['price'],(int,float))
        assert product['price'] >= 0
        assert keyword in product['name'].lower()


def test_search_products_returns_results_empty_list(base_url):
    response = requests.get(f"{base_url}/rest/products/search",
                            params={"q":"appleeeeeeeeeeeeeeeeeeeee"},
                            timeout=10)
    body = response.json()

    assert response.status_code == 200
    assert body["status"] == "success"
    assert body["data"] == []