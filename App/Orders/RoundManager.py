from App import Round, OrderManager

class RoundManager:
    def __init__(self, drinks, extras):
        self.round = None
        self.order_manager = OrderManager(drinks, extras)
        self.drinks = drinks
        self.extras = extras

    def new_round(self, initiator):
        self.round = Round(initiator)

    def new_order(self):
        self.order_manager.new_order()

    def add_to_order(self, choice: int):
        return self.order_manager.add_by_index(choice)





