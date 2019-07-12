# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.health = 20
        self.inventory = []

    def move(self, direction):
        direction_to = f"{direction}_to"
        current_room = getattr(self.current_room, direction_to)
        #current_room = self.current_room.e_to
        if current_room:
            self.current_room = current_room
            self.current_room.get_current_direction()
        else:
            self.print_end_direction(direction)

    def print_end_direction(self, direction):
        print(
            f"End of room, change your direction.\nStop moving {direction.upper()}")

    def print_inventory(self):
        print(f"Your health is: {self.health}\n")
        if(len(self.inventory)):
            print("You are carrying:\n  " +
                  ", ".join([item.name for item in self.inventory]) + "\n")
        else:
            print("You inventory is empty")

    def get_item(self, item):
        def filter_items(element):
            if element.name == item:
                return True
            else:
                return False

        result = list(filter(filter_items, self.current_room.items))

        self.inventory.append(result[0])
        self.current_room.remove_item(result[0])

        print("You picked up:\n  " +
              ", ".join([item.name for item in self.inventory]) + "\n")

    def drop_item(self, item):
        def filter_items(element):
            if element.name == item:
                return True
            else:
                return False
        result = list(filter(filter_items, self.inventory))

        self.current_room.add_item(result[0])
        self.inventory.remove(result[0])
        self.print_inventory()
        self.current_room.get_items()
