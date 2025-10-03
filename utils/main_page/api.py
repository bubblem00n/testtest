import requests
from configs import base_url



def get_active_items():
    response = requests.get(url=f"{base_url}/web/client/events/active")
    return response


def get_item(item_slug: str):
    response = requests.get(url=f"{base_url}/web/client/moderated-offers/{item_slug}")
    return response


def search_items(item_name: str):
    body = {
        "query": item_name
    }

    response = requests.post(url=f"{base_url}/web/client/search/full-text", json=body)
    return response

def get_cart_url(cookie=None):
    if cookie is None:
        response = requests.get(url=f"{base_url}/web/client/cart/view-cart/duplicate")
    else:
        header = {
            'Cookie': f"cart={cookie};"
        }

        response = requests.get(url=f"{base_url}/web/client/cart/view-cart/duplicate", headers=header)

    return response


def add_cart_url(cookie:str, offer_id:str, condition_id:str, quantity=1):
    header = {
        'Cookie': f"cart={cookie};"
    }

    body = {
        "moderated_offer_id": offer_id,
        "condition_id":condition_id,
        "quantity":1
    }

    response = requests.post(
        url=f"{base_url}/web/client/cart/moderated-items", 
        headers=header, 
        json=body
    )
    
    return response

