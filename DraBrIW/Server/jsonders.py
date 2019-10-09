import json
from ZDraBrIW.App.User import User
from ZDraBrIW.App.Brews import Drink


def remove_underscore_prefix(obj_dict: dict):
    return dict(map(lambda item: (item[0][1:], item[1]) if item[0].startswith("_") else item, obj_dict.items()))


class UserEncoder(json.JSONEncoder):
    def default(self, object):
        if isinstance(object, User):
            return remove_underscore_prefix(object.__dict__)
        elif isinstance(object, Drink):
            return remove_underscore_prefix(object.__dict__)
        else:
            return json.JSONEncoder.default(self, object)


class UserDecoder(json.JSONDecoder):
    def decode(self, s, **kwargs):
        data = json.loads(s)
        try:
            return self._decode_user(data)
        except TypeError:
            return list(map(lambda item: self._decode_user(item), data))

    def _decode_user(self, data):
        return User(data["first_name"], data["last_name"], Drink(data["fav_drink"]["name"], 0))


class DrinkDecoder:
    def decode(self, s, **kwargs):
        data = json.loads(s)
        try:
            return self._decode_drink(data)
        except TypeError:
            return list(map(lambda item: self._decode_drink(item), data))

    def _decode_drink(self, data):
        return Drink(data["name"], 0)
