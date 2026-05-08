from resources import Resource

class Money:
    def __init__(self) -> None:
        # amount of money (currency)
        pass

class Materials:
    def __init__(self) -> None:
        # name, quantity
        pass

class Crafts:
    def __init__(self) -> None:
        # name, material, cost, quantity, value
        # crafts sell for money
        pass

class Producers:
    def __init__(self) -> None:
        # name, material produced, how often 
        pass

class Crafters:
    def __init__(self) -> None:
        # name, material crafted, how often
        pass

class ResourceManager:
    def __init__(self) -> None:
        # {resource name: {cost: [{name: "__name__", quantity: #}], "produces": [{"name": "", "quantity": #}], quantity: #}}
        self.amount = {"wood": 0, "money": 0, "loggers": 0}
        self.resources = {"wood": Resource("wood", None, 0, "wood", 1, 0), "loggers": Resource("loggers", "money", 10, "wood", 1, 10)}
        pass

    def get_amount(self, resource):
        return self.amount[resource]
    
    def remove(self, resource, quantity):
        self.amount[resource] -= quantity

    def add(self, resource, quantity):
        self.amount[resource] += quantity

    def can_remove_resource(self, resource, quantity):
        return self.get_amount(resource) > quantity and quantity > 0

    def sell_wood(self, quantity):
        resource_name = "wood"
        resource_value = 1
        if self.can_remove_resource(resource_name, quantity):
            self.remove(resource_name, quantity)
            self.add("money", quantity * resource_value)
    
class WorkManager:
    def __init__(self, rs_manager:ResourceManager) -> None:
        self.resources = rs_manager
        # {worker name: {resource name: "__name__", quantity: #, cooldown: # of seconds}}
        self.workers = {"log cutter": {"cost": 10, "resource_name": "wood", "quantity": 0, "cooldown" : 10}}

    

    def buy_workers(self, worker_name, amount):
        cost = self.workers[worker_name]["cost"] * amount
        resource_name = "money"
        if self.resources.can_remove_resource(resource_name, cost):
            self.resources.remove(resource_name, cost)
            self.workers[worker_name]["quantity"] += amount
    

if __name__ == "__main__":
    rs_manager = ResourceManager()
    rs_manager.add("wood", 10)
    print(rs_manager.get_amount("wood"), rs_manager.get_amount("money"))
    rs_manager.sell_wood(7)
    print(rs_manager.get_amount("wood"), rs_manager.get_amount("money"))
