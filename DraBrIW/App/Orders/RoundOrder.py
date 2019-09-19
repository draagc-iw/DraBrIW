from DraBrIW.App.Orders import Order


class RoundOrder(Order):
    def __init__(self):
        super(RoundOrder, self).__init__()

    def __str__(self):
        output = str()

        for drink, count in self._order_items.items():
            output += f"{drink.get_with_name()}\n\t\t{count}x\t£{drink.get_cost()}\n"

        output += f"Total: {self.total}"
        return f"\n{output}\n"
