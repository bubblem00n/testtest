import pytest
import requests
import json
import allure

from utils.main_page.api import get_active_items, get_cart_url, get_item, add_cart_url, search_items 
from configs import base_url

get_item_url = base_url + "/web/client/moderated-offers"
get_item_catalog = base_url + "/web/client/catalog/moderated-offers"
offers_url = base_url + "/web/client/recommend/offers/v2"


def url_generator(slug):
    return f'{get_item_url}/{slug}'

def url_reviews(id):
    return f'{get_item_url}/{id}/reviews'  

def url_delivery(id):
    return f'{get_item_catalog}/{id}/delivery-time-estimation/duplicate'



def test_get_active_items():
    global offer_id, slug, condition_id
    
    response = get_active_items()
    
    assert response.status_code == 200
    
    response = response.json()
    assert len(response) > 0

    first_item = response[0]["offers"][0]
    
    offer_id = first_item["moderated_offer_id"]
    slug = first_item["slug"]
    condition_id = first_item["condition"]["id"]
    
    
    offers = response[0]["offers"]
    
    for offer in offers:
        assert "offer_id" in offer, "Ожидали поле offer_id в offer"
        assert "name" in offer, "Ожидали поле name в offer"
        assert "price" in offer, "Ожидали поле price в offer"
        assert "partner" in offer, "Ожидали поле partner в offer"
        assert offer["price"] > 0
        if "old_price" in offer:
            offer["old_price"] >= offer["price"], "old_price меньше чем price"


def test_item():
    link = url_generator(slug)
    response = requests.get(url=link)
    
    assert response.status_code == 200
    
    response = response.json()
    assert len(response) > 0
    
    item = response["moderated_offer"]
    assert "name" in item, "Ожидали поле name в moderated_offer"
    assert item["price"] >= 0, "price меньше, либо равна 0"
    assert len(item["images"]) > 0, "В продукте нет картинок"
    assert item["discount"] <= 0, "discount больше нуля"
    if item["discount"] < 0:
        item["price"] < item["old_price"], "old_price меньше чем price"

  

def test_reviews():
    link = url_reviews(offer_id)
    reviews = requests.get(url=link)
    
    reviews = reviews.json()
    if reviews["meta"]["total"] > 0:
        assert len(reviews["offer_reviews"]) != 0
    
    
def test_offers():
    body={
        "user_id":"befd73c3-3a92-4e58-a94b-1ac48707174c",
        "from_app":"WebAndMobile",
        "from_layer":"main_page",
        "product_ids":None,
        "limit":10
        }
    
    response = requests.post(url=offers_url, json=body)
    
    assert response.status_code == 200
    
    response = response.json()
    offers = response["offers"]
    
    for offer in offers:
        assert "name" in offer["partner"], "Ожидали поле name в partner"
        assert "rating" in offer["partner"], "Ожидали поле rating в partner"
        
        assert "duration" in offer["condition"], "Ожидали поле duration в condition"
        assert "commission" in offer["condition"], "Ожидали поле commission в condition"
    

def test_delivery():
    link = url_delivery(offer_id)
    
    response = requests.get(url=link)

    assert response.status_code == 200

    response = response.json()

    assert "moderated_offer_id" in response
    assert "delivery_time" in response
    assert "days_to_deliver" in response

    assert response["days_to_deliver"] >= 0

    