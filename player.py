class Player:
    def __init__(self, name):
        self.name = name
        self.money = 10000
        self.income = 3000
        self.expenses = 1500
        self.savings = 0
        self.month = 0
        self.year = 0

    def get_balance(self):
        return self.money

    def get_monthly_balance(self):
        return self.income - self.expenses

    def finish_month(player):
        player.month += 1

    def start_month(player):
        player.money += player.income
        player.money -= player.expenses
