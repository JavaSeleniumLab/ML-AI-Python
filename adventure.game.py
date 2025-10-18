locations ={'cave', 'forest', 'castle', 'village', 'mountain', 'river', 'desert', 'swamp', 'island', 'plains'}
actions = {'explore', 'rest', 'gather', 'hunt', 'trade', 'build', 'travel', 'fight', 'craft', 'discover'}
goal = 'Find the hidden treasure'

def start_adventure():
    print("Welcome to the Adventure Game!")
    print(f"Your goal is to: {goal}")
    print("You can explore the following locations:")
    for loc in locations:
        print(f"- {loc}")
    print("You can perform the following actions:")
    for act in actions:
        print(f"- {act}")
    print("Good luck on your adventure!")

print("===================================")

def cave():
    print("You enter a dark cave. It's cold and damp.")
    print("You can explore deeper or return to the entrance.")
    action = input("What do you want to do? (explore/return): ").strip().lower()
    if action == 'explore':
        print("You find a hidden passage leading to a treasure chamber!")
    elif action == 'return':
        print("You return to the cave entrance.")
    else:
        print("Invalid action. You stand still, unsure of what to do.")
    print("===================================")

def forest():
    print("You walk into a dense forest. The trees tower above you.")
    print("You can gather resources or rest under a tree.")
    action = input("What do you want to do? (gather/rest): ").strip().lower()
    if action == 'gather':
        print("You gather some herbs and wood.")
    elif action == 'rest':
        print("You take a short nap and feel refreshed.")
    else:
        print("Invalid action. You stand still, unsure of what to do.")
    print("===================================")
def castle():
    print("You arrive at an ancient castle. It looks abandoned.")
    print("You can explore the castle or look for clues outside.")
    action = input("What do you want to do? (explore/look): ").strip().lower()
    if action == 'explore':
        print("You find old manuscripts that hint at a hidden treasure!")
    elif action == 'look':
        print("You find footprints leading to a secret garden.")
    else:
        print("Invalid action. You stand still, unsure of what to do.")
    print("===================================")
def village():
    print("You enter a small village. The villagers seem friendly.")
    print("You can trade with villagers or gather information.")
    action = input("What do you want to do? (trade/inform): ").strip().lower()
    if action == 'trade':
        print("You trade some goods and get useful supplies.")
    elif action == 'inform':
        print("You learn about a hidden treasure in the nearby cave.")
    else:
        print("Invalid action. You stand still, unsure of what to do.")
    print("===================================")
def mountain():
    print("You climb a steep mountain. The view is breathtaking.")
    print("You can rest at the peak or explore a nearby cave.")
    action = input("What do you want to do? (rest/explore): ").strip().lower()
    if action == 'rest':
        print("You rest and enjoy the view from the peak.")
    elif action == 'explore':
        print("You find a cave with ancient drawings on the walls.")
    else:
        print("Invalid action. You stand still, unsure of what to do.")
    print("===================================")
def river():
    print("You reach a flowing river. The water is clear and cool.")
    print("You can fish or build a raft to travel downstream.")
    action = input("What do you want to do? (fish/build): ").strip().lower()
    if action == 'fish':
        print("You catch some fish for your journey.")
    elif action == 'build':
        print("You build a sturdy raft and prepare to travel.")
    else:
        print("Invalid action. You stand still, unsure of what to do.")
    print("===================================")
def desert():
    print("You find yourself in a vast desert. The sun is scorching.")
    print("You can search for an oasis or rest under a rock.")
    action = input("What do you want to do? (search/rest): ").strip().lower()
    if action == 'search':
        print("You find an oasis with fresh water and palm trees.")
    elif action == 'rest':
        print("You rest in the shade and regain your strength.")
    else:
        print("Invalid action. You stand still, unsure of what to do.")
    print("===================================")
def swamp():
    print("You wade into a murky swamp. The air is thick with humidity.")
    print("You can gather herbs or look for hidden paths.")
    action = input("What do you want to do? (gather/look): ").strip().lower()
    if action == 'gather':
        print("You gather some medicinal herbs.")
    elif action == 'look':
        print("You find a hidden path leading to a dry area.")
    else:
        print("Invalid action. You stand still, unsure of what to do.")
    print("===================================")
def island():
    print("You arrive at a tropical island. The beach is beautiful.")
    print("You can explore the island or relax by the shore.")
    action = input("What do you want to do? (explore/relax): ").strip().lower()
    if action == 'explore':
        print("You find a cave with sparkling gems inside!")
    elif action == 'relax':
        print("You relax on the beach and enjoy the sound of the waves.")
    else:
        print("Invalid action. You stand still, unsure of what to do.")
    print("===================================")
def plains():
    print("You walk across open plains. The grass sways in the wind.")
    print("You can hunt for food or build a shelter.")
    action = input("What do you want to do? (hunt/build): ").strip().lower()
    if action == 'hunt':
        print("You successfully hunt a deer for food.")
    elif action == 'build':
        print("You build a sturdy shelter to protect yourself.")
    else:
        print("Invalid action. You stand still, unsure of what to do.")
    print("===================================")    
def travel_to(location):
    if location == 'cave':
        cave()
    elif location == 'forest':
        forest()
    elif location == 'castle':
        castle()
    elif location == 'village':
        village()
    elif location == 'mountain':
        mountain()
    elif location == 'river':
        river()
    elif location == 'desert':
        desert()
    elif location == 'swamp':
        swamp()
    elif location == 'island':
        island()
    elif location == 'plains':
        plains()
    else:
        print("Unknown location. Please choose a valid location.")
        print("===================================")
print("Adventure game module loaded.")
if __name__ == "__main__":
    start_adventure()
    while True:
        loc = input("Enter a location to travel to (or 'quit' to exit): ").strip().lower()
        if loc == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        travel_to(loc)