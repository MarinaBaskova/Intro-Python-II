from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Items
item = {
    'glasses': Item('glasses', 'To see what is in the end'),
    'lamp': Item('lamp', 'Give you the light to see the path'),
    'map': Item('map', 'Help you navigate'),
    'box': Item('box', 'To hold your treasures'),
    'ax': Item('ax', 'In case you want the gold')
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Put items in the rooms
room['outside'].add_item(item['lamp'])
room['foyer'].add_item(item['box'])
room['overlook'].add_item(item['map'])
room['narrow'].add_item(item['ax'])
room['treasure'].add_item(item['glasses'])

# Make a new player object that is currently in the 'outside' room.
player1 = Player("Player1", room["outside"])

# print(f'Player Name: {player1.name}, Current room: {player1.current_room.name} and Room Description: {player1.current_room.description}')
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
room["outside"].get_current_direction()

while True:
    cardinal_direction = ["n", "s", "e", "w"]
    user_input = input("Enter your move:")
    user_input = user_input.split(" ")

    if(len(user_input) > 1):
        v = user_input[0].lower()
        o = user_input[1].lower()
    elif (len(user_input) == 1):
        v = user_input[0].lower()
    else:
        print("Invalid input")

    if(v == "q"):
        print("You quit the game")
        exit()
    elif (v in cardinal_direction):
        player1.move(v)
    elif (v == "take"):
        if o in [item.name for item in player1.current_room.items]:
            player1.get_item(o)
        else:
            print("Wrong item")
    elif (v == "drop"):
        player1.drop_item(o)
    elif (v == "i"):
        player1.print_inventory()
    else:
        print("Invalid input")
