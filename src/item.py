
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        str = f"""
        \n----------------------------------
        \n{self.name}
        \n   {self.description}\n"""
        return str

    def on_take(self):
        print(f'You took {self.name}')

    def on_drop(self):
        print(f"You drop {self.name}")
