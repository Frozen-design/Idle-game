class ResourceManager:
    def __init__(self) -> None:
        # {resource name: {cost: [{name: "__name__", quantity: #}], "produces": [{"name": "", "quantity": #}], quantity: #}}
        self.money = 0
        self.materials = {"wood": 0}
        self.crafts = {"ducks": {"cost": {"material": "wood", "amount": 1}, "value": 10, "quantity": 0}}
        self.producers = {"loggers": {"cost": 10, "produces": {"material": "wood", "amount": 1}, "quantity": 0}}
        self.crafters = {"duck smiths": {"cost": 10, "produces": {"craft": "ducks", "amount": 1}, "quantity": 0}}
        pass

    # -----------------
    # Money functions -
    # -----------------
    def add_money(self, amount):
        self.money += amount

    def money_check(self, amount:int) -> bool:
        return self.money >= amount and amount > 0
    
    # --------------------
    # Material functions -
    # --------------------
    def add_material(self, material:str, amount:int):
        self.materials[material] += amount
    
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

    def add_craft(self, craft:str, amount:int):
        cost = self.crafts[craft]["cost"]
        material, m_amount = (cost["material"], cost["amount"] * amount)
        if self.material_check(material, m_amount):
            self.materials[material] -= m_amount

    def sell_craft(self, craft:str, amount:int):
        if self.can_sell(craft, amount):
            value = self.crafts[craft]["value"]
            self.money += value * amount
            self.crafts[craft]["quantity"] += amount

    # ------------------
    # Worker functions -
    # ------------------
    def can_buy(self, worker:str, amount:int) -> bool:
        cost = self.crafters[worker]["cost"] * amount
        return self.money_check(cost)
    
    def buy_worker(self, worker:str, amount:int):
        if self.can_buy(worker, amount):
            cost = self.crafters[worker]["cost"]
            self.money -= cost * amount
            if worker in self.crafters.keys():
                self.crafters[worker]["quantity"] += amount
            elif worker in self.producers.keys():
                self.producers[worker]["quantity"] += amount


if __name__ == "__main__":
    rs_manager = ResourceManager()