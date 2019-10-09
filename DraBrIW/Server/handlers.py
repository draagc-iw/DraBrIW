from .jsonders import UserEncoder, UserDecoder, DrinkDecoder
from DraBrIW.App.Storage import DrinkService, UserService
import json

us = UserService()
ds = DrinkService()


def user_get():
    return stringify(us.get_all(), UserEncoder), 200


def user_put(body):
    # print(json.loads(body, cls=UserDecoder))
    return json.dumps({"status": "ok"}).encode('utf-8')


def user_post(body):
    try:
        decoded = json.loads(body, cls=UserDecoder)
    except KeyError:
        return stringify({"error": "Bad request - read endpoint documentation"}), 400

    if isinstance(decoded, list):
        for item in decoded:
            us.add(item)
    else:
        us.add(decoded)
    return stringify({"status": "ok"}), 201


def drinks_get():
    return stringify(ds.get_all(), UserEncoder), 200


def drinks_post(body):
    try:
        decoded = json.loads(body, cls=DrinkDecoder)
    except KeyError:
        return stringify({"error": "Bad request - read endpoint documentation"}), 400

    if isinstance(decoded, list):
        for item in decoded:
            ds.add(item)
    else:
        ds.add(decoded)
    return stringify({"status": "ok"}), 201


def stringify(data, encoder_cls=None):
    return json.dumps(data, cls=encoder_cls).encode('utf-8')
