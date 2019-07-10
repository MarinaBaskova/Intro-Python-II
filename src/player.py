# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        direction_to = f"{direction}_to"
        current_room = getattr(self.current_room, direction_to)
        if current_room:
            self.current_room = current_room
        else:
            self.print_direction(direction)

    def print_direction(self, direction):
        print(
            f"End of room, change your direction. Stop moving to {direction.upper()}")

    def get_current_direction(self):
        print(f'Current room: {self.current_room.name}')
        print(f'Room Description: {self.current_room.description}')
