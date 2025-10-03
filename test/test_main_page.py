# import pytest
# import requests
# import json
# import allure
# from utils.functions import attach_reqres
# from utils.main_page.api import get_active_items, get_cart_url, get_item, add_cart_url, search_items
#
#
# @allure.parent_suite("Главная страница")
# @allure.suite("Проверка добавление товара в корзину у не авторизованного пользователя")
# @allure.title("Получение товаров")
# def test_get_active_items():
#     global offer_id, slug, condition_id
#
#     with allure.step("Отправка запроса на получение товаров"):
#         response = get_active_items()
#         attach_reqres(response=response)
#
#     with allure.step("Проверка статуса ответа:"):
#         assert response.status_code == 200
#
#     response = response.json()
#     assert len(response) > 0
#
#     first_item = response[0]["offers"][0]
#
#     offer_id = first_item["moderated_offer_id"]
#     slug = first_item["slug"]
#     condition_id = first_item["condition"]["id"]
#
#     offers = response[0]["offers"]
#
#     for offer in offers:
#         assert "offer_id" in offer
#         assert "name" in offer
#         assert "price" in offer
#         assert "partner" in offer
#
#
# @allure.parent_suite("Главная страница")
# @allure.suite("Проверка добавление товара в корзину у не авторизованного пользователя")
# @allure.title("Получение session-id с куки")
# def test_get_session_id():
#     global cookie
#
#     with allure.step("Отправка запроса на получение корзины"):
#         response = get_cart_url()
#         attach_reqres(response=response)
#
#     with allure.step("Проверка статуса ответа"):
#         assert response.status_code == 200
#
#     cookie = response.cookies.get_dict()['cart']
#     assert isinstance(cookie, str), f'Тип куки на самом деле {type(cookie)}'
#
#
# @allure.parent_suite("Главная страница")
# @allure.suite("Проверка добавление товара в корзину у не авторизованного пользователя")
# @allure.title("Добавление товара в корзину")
# def test_add_item():
#
#     response = add_cart_url(cookie=cookie, offer_id=offer_id, condition_id=condition_id)
#     assert response.status_code == 200
#
#     response = response.json()
#     print(json.dumps(response, indent=4))
#
#
# # def test_card_item():
# #     response = get_cart_url(cookie=cookie)
#
# #     assert response.status_code == 200
#
# #     response = response.json()
# #     print(json.dumps(response, indent=4))
#
#
# #     item_offer_id = response["moderated_cart_items"][0]["moderated_offer_id"]
# #     assert item_offer_id == offer_id
#
# #     cart_len = len(response["moderated_cart_items"][0])
# #     print(cart_len)
#
#
# # @pytest.mark.parametrize('item', ['iPhone', 'samsung', '8716248712648712648172648127','xiaomi'])
# # def test_search(item):
# #     response = search_items(item)
#
# #     res_json = response.json()
#
# #     items_list = res_json["items"]
#
# #     print(f'{items_list}\n\n')
#
# #     assert response.status_code == 200
# #     assert len(items_list) > 0, "Ничего не нашлось"
#
#
# # def url_generator(slug):
# #     return f'{get_item}/{slug}'
#
#
# # def test_active_items():
# #     global item_slug
#
# #     response = requests.get(url=active_items_url)
#
# #     assert response.status_code == 200
#
# #     response = response.json()
#
# #     item_slug = response[0]['offers'][0]['slug']
# #     print(item_slug)
#
#
# # def test_get_item():
# #     url = url_generator(item_slug)
#
# #     response = requests.get(url=url)
#
# #     print(response.json())
#
