import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.insert(1, os.path.join(sys.path[0], '../bwx_adventure'))
from bwx_adventure.advent import *
from bwx_adventure.advent_devtools import *

game = Game("Willow Of Death")

porch = game.new_location(
  "Porch",
  "You are on a porch. It is raining. To the North is an office door to the west is a ramp.")

player = game.new_player(porch)

vestibule = game.new_location(
  "Vestibule",
  "This is a small area at the bottom of a flight of stairs. There is an office door to the west. You have an exit from where you came.")

upstairs = game.new_location(
    "Upstairs Hallway",
  "This is a hallway with a door to the east, And stairs going down.")

office = game.new_location(
  "Office",
  """A nicely organized office.
  There is a door to the north.""")

family = game.new_location(
  "Family Room",
  "This is a large room with a fridge and an open window to the north. There is also a door to the west.")

yard = game.new_location(
  "Yard",
  "This is a small yard with barbed wire all around. There is only an exit from were you came.")

step = game.new_location(
  "Stepway",
  "This is a stepway with a door to the north and west.")

computer = game.new_location(
  "Computer Lab",
  "This is a small room with tables spread out in the room.")

lindas_room = game.new_location(
  "Room Four",
  "This is a skinny but tall room. There is a whitebourd here.")

storage_room1 = game.new_location(
  "Storage Room 1",
  "This is a large room with boxes of school suplys.")

game.new_connection("Storage1door", upstairs, storage_room1, [IN, EAST], [OUT, WEST])

game.new_connection("Linda Lab", computer, lindas_room, [IN, WEST], [OUT, EAST])

game.new_connection("Lab Door", step, computer, [IN, WEST], [OUT, EAST])

game.new_connection("Vestibule Door Outside", step, vestibule, [IN, NORTH], [OUT, SOUTH])

game.new_connection("Ramp", porch, step, [IN, WEST], [OUT, EAST])

game.new_connection("Window", family, yard, [IN, NORTH], [OUT, SOUTH])

game.new_connection("Stairs", vestibule, upstairs, [IN, UP], [OUT, DOWN])

game.new_connection("Vestibule Door", porch, vestibule, [IN, NORTH], [OUT, SOUTH])

game.new_connection("Office Door", vestibule, office, [IN, WEST], [OUT, EAST])

dog = Pet("Dog Friend")
dog.set_location(porch)
dog.set_allowed_locations([porch])

yard.new_object(Drink("vial",
                          "a small vial of bright green glowing liquid",
                          Die("choking violently and collapsing onto the floor..."),
                          Object("empty vial", "an empty vial with an acrid odor")))

lindas_room.add_object("dry erase marker",
                       "small red marker")

zombie = Animal("zombie")
zombie.set_location(yard)
zombie.set_allowed_locations([yard])
game.add_actor(zombie)
zombie.add_phrase("fight zombie",
                   "you kill the zombie.")

miniz = Actor("tiny zombie")
miniz.set_location(family)
game.add_actor(miniz)
shield = vestibule.new_object("shield", "a shiny pair of armor")
knife = office.new_object("knife", "a rusty old knife")
def fight_miniz(game, thing):
    if not "shield" in game.player.inventory:
game.output("You try to stab the zombie with the knife, but it bites you.")

game.output("You turn to the undead.")

player.terminate()
    else:
game.output("Using the shield to avoid the dragon's flames you kill it with the sword.")
miniz.terminate()
miniz.add_phrase("fight zombie", fight_miniz)
game.add_actor(player)
game.add_actor(dog)
test_script = Script("test",
"""
> look
> take vial
> give dog vial
> tell dog drink vial
> look
> end
""")

player.add_script(test_script)

game.run()