import requests
import pytest




def test_homepage_is_available(api_client):
    response = api_client.get('/')
    assert response.status_code == 200,(
        f"首页状态码不符合预期：期望 200，实际 {response.status_code}"
    )

@pytest.mark.parametrize('keyword',['apple','banana'])
def test_search_products_returns_results(api_client,keyword):
    response = api_client.get(
                            "/rest/products/search",
                            params={"q":keyword},
                            )
    body = response.json()

    assert response.status_code == 200
    assert body["status"] == "success"
    assert isinstance(body["data"],list)
    assert len(body["data"])>0 ,(
    f"搜索关键词 {keyword!r} 时，预期找到商品，实际返回空列表"
)

    for product in body["data"]:
        assert isinstance(product['id'],int)
        assert isinstance(product['name'],str)
        assert isinstance(product['price'],(int,float))
        assert product['price'] >= 0, (
    f"商品 ID={product['id']} 的价格不能为负数，实际为 {product['price']}"
)
        assert keyword in product['name'].lower()


def test_search_products_returns_results_empty_list(api_client):
    response = api_client.get(
                            "/rest/products/search",
                            params={"q":"appleeeeeeeeeeeeeeeeeeeee"},
                            )
    body = response.json()

    assert response.status_code == 200
    assert body["status"] == "success"
    assert body["data"] == []