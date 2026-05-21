class Resource:
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value
        pass

    def __mult__(self, other:float):
        self.value *= other

    def __add__(self, other:float):
        self.value += other