class ResourceManager:
    def __init__(self) -> None:
        # {resource name: {cost: [{name: "__name__", quantity: #}], "produces": [{"name": "", "quantity": #}], quantity: #}}
        self.money = 0
        self.materials = {"wood": 0}
        self.crafts = {"ducks": {"cost": {"material": "wood", "amount": 1}, "value": 10, "quantity": 0}}
        self.producers = {"loggers": {"cost": 0, "produces": {"material": "wood", "amount": 1}, "quantity": 0}}
        self.crafters = {"duck smiths": {"cost": 10, "produces": {"craft": "ducks", "amount": 1}, "quantity": 0}}
        pass

    def get_quantity(self, rs_name) -> float | None:
        if rs_name == "money":
            value = self.money
        elif rs_name in self.materials.keys():
            value = self.materials[rs_name]
        elif rs_name in self.crafts.keys():
            value = self.crafts[rs_name]["quantity"]
        elif rs_name in self.producers.keys():
            value = self.producers[rs_name]["quantity"]
        elif rs_name in self.crafters.keys():
            value = self.crafters[rs_name]["quantity"]
        else:
            value = None

        return value
    
    def add_quantity(self, rs_name, number):
        if rs_name == "money":
            self.add_money(number)
        elif rs_name in self.materials.keys():
            self.add_material(rs_name, number)
        elif rs_name in self.crafts.keys():
            self.add_craft(rs_name, number)
        elif rs_name in self.producers.keys() or rs_name in self.crafters.keys():
            self.buy_worker(rs_name, number)

    # -----------------
    # Money functions -
    # -----------------
    def add_money(self, amount) -> bool:
        self.money += amount
        return True

    def money_check(self, amount:int) -> bool:
        return self.money >= amount and amount >= 0
    
    # --------------------
    # Material functions -
    # --------------------
    def add_material(self, material:str, amount:int) -> bool:
        self.materials[material] += amount
        return True
    
    def material_check(self, material:str, amount:int) -> bool:
        return self.materials[material] >= amount and amount > 0
    
    # -----------------
    # Craft functions -
    # -----------------
    def craft_check(self, craft:str, amount:int) -> bool:
        return self.crafts[craft]["quantity"] >= amount and amount > 0
    
    def can_craft(self, craft:str, amount:int) -> bool:
        cost = self.crafts[craft]["cost"]
        material, m_amount = (cost["material"], cost["amount"] * amount)
        return self.material_check(material, m_amount)
    
    def can_sell(self, craft:str, amount:int) -> bool:
        return self.craft_check(craft, amount)

    def add_craft(self, craft:str, amount:int) -> bool:
        cost = self.crafts[craft]["cost"]
        material, m_amount = (cost["material"], cost["amount"] * amount)
        if self.material_check(material, m_amount):
            self.materials[material] -= m_amount
            return True
        else:
            return False

    def sell_craft(self, craft:str, amount:int) -> bool:
        if self.can_sell(craft, amount):
            value = self.crafts[craft]["value"]
            self.money += value * amount
            self.crafts[craft]["quantity"] += amount
            return True
        else:
            return False

    # ------------------
    # Worker functions -
    # ------------------
    def can_buy(self, worker:str, amount:int) -> float | None:
        if worker in self.crafters.keys():
            cost = self.crafters[worker]["cost"] * amount
        elif worker in self.producers.keys():
            cost = self.producers[worker]["cost"] * amount
        else:
            return None
        if self.money_check(cost):
            return cost
        else:
            return None
    
    def buy_worker(self, worker:str, amount:int) -> bool:
        cost = self.can_buy(worker, amount)
        if cost != None:
            self.money -= cost * amount
            if worker in self.crafters.keys():
                self.crafters[worker]["quantity"] += amount
            elif worker in self.producers.keys():
                self.producers[worker]["quantity"] += amount
            else:
                return False
            return True
        else:
            return False

if __name__ == "__main__":
    selfager = ResourceManager()