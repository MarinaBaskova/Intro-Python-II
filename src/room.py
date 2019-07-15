# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_current_direction(self):
        print(f'\n-----You are in {self.name}-----\n')
        print(f'Room Description: {self.description}')
        if (len(self.items)):
            self.get_items()
        else:
            print("The room is empty")

    def get_items(self):
        str = (
            ", ".join([item.name for item in self.items]) + "\n")
        print(f'Room Inventory: {str}')
