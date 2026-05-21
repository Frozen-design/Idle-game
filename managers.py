from resources import Resource

class Bank:
    def __init__(self) -> None:
        self.money = 0
        pass

class Purchasable:
    def __init__(self) -> None:
        pass

    def get_upgrade_cost(self, function):
        return (self.level ** 1.1) * 10 # cost scaling function

    def apply_to_level(self, function):
        return function(self.level)
    
    def level_up(self, number_of_levels):
        self.level += number_of_levels


class Spawner(Purchasable):
    def __init__(self, name) -> None:
        self.name = name
        self.level = 0

    def get_base_value(self):
        return self.level * 1
    
    def produce_resource(self):
        return Resource(self.name, self.get_base_value())

class Upgrader(Purchasable):
    def __init__(self) -> None:
        self.level = 0
        pass
    
    def get_resource_multiplier(self):
        return 1 + self.level * 0.5 # resource multiplier
    
    

class Seller(Bank):
    def __init__(self) -> None:
        pass

    def sell_resource(self, resource:Resource):
        self.money += resource.value
        pass

class Pipeline:
    def __init__(self) -> None:
        self.spawner:Spawner | None = None
        self.upgraders: list[Upgrader] = []
        self.seller = Seller()
        pass

