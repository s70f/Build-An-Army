shop = [] # List of 5 Mercs

class Army:

    def __init__(self, money=1000, damage=0, defense=0, points=0, mercs = {}):
        self.money = money
        self.damage = damage
        self.defense = defense
        self.mercs = mercs
        self.points = points

    def add_merc(self, tier: str, name: str, cost: int, damage: int, defense: int) -> None:
        self.money -= cost
        self.damage += damage
        self.defense += defense
        self.mercs[name] = tier

class Mercs:

    def __init__(self, tier: str, name: str, cost: int, damage: int, defense: int):
        
        self.tier = tier
        self.cost = cost
        self.damage = damage
        self.defense = defense

    def buy(self, army: Army, player_coins: int) -> None:
        army.add_merc(self.tier, self.name, self.cost, self.damage, self.defense)


