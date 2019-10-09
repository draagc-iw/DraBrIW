import abc
from App.User import User
from App.Brews import Drink
from App.Orders import Round, RoundOrder


class BaseMapper(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def to_db(obj):
        pass

    @staticmethod
    @abc.abstractmethod
    def from_db(db_response):
        pass


class UserMapper(BaseMapper):

    @staticmethod
    def to_db(user: User):
        drink_id = user.fav_drink.id if user.fav_drink is not None else None
        print(user, drink_id)

        return user.first_name, user.last_name, drink_id

    @staticmethod
    def from_db(db_row):
        drink = Drink(db_row.drink_name, 0) if db_row.drink_name is not None else None
        return User(db_row.first_name, db_row.last_name, drink, db_row.id)


class DrinkMapper(BaseMapper):

    @staticmethod
    def to_db(obj: Drink):
        return obj.get_name()

    @staticmethod
    def from_db(db_row):
        return Drink(db_row.name, 0, id=db_row.id)


class RoundMapper(BaseMapper):
    @staticmethod
    def to_db(obj):
        pass

    @staticmethod
    def from_db(db_response: iter):
        rounds = dict()
        for row in db_response:
            user = User(row.person_first_name, row.person_last_name, uid=row.person_id)
            order = RoundOrder()
            order.add_item(row.drink_id)

            if row.round_id not in rounds.keys():
                initiator = User(row.initiator_first_name, row.initiator_last_name,
                                 uid=row.initiator_id)
                rounds[row.round_id] = Round(initiator, id=row.round_id, active=(row.round_active == 1))

            if user.first_name is not None:
                rounds[row.round_id].add(user, order)

        return list(rounds.values())
