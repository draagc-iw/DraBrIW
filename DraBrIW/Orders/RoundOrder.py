from DraBrIW.Orders import Order, Round


class RoundOrder(Order):
    def __init__(self, round: Round):
        super(RoundOrder, self).__init__()
        self._round = round

    @property
    def uid(self):
        return self._round.uid

    def __str__(self):
        output = str()

        for drink, count in self._order_items.items():
            output += f"{drink.get_name()}\n\t\t{count}x\t£{drink.get_cost()}\n"

        output += f"Total: {self.total}"
        return f"\n{output}\n"
