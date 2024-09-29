game_state = {
    "current_room" : "Admin",
    "inventory" : [],
    "tasks": {
        "Cafe": {"status": "incomplete", "description": "\nTask: You need a Cafe Key to enter the cafe", "item":"CafeKey"},
        "Electrical": {"status": "incomplete", "description": "\nTask: You need a ToolBox to repair Electricity", "item":"ToolBox"},
        "Engine": {"status": "incomplete", "description": "\nTask: You need a PowerCore to repair the engines", "item":"PowerCore"},
        "O2": {"status":"incomplete", "description": "\nTask: You need a LaserGun to kill the Alien", "item":"LaserGun"},
        "Navigation": {"status": "incomplete", "description": "\nTask: You need to complete the word. Hints are in different rooms", "word":"Imposter"},
    },
    "rooms" : {
        "Admin": {
            "description": "The nerve center of the ship, filled with blinking consoles, star charts, and system diagnostics. A key for the Café lies on the floor. The ship feels eerily quiet as warnings flash about engine malfunctions. The soft glow of distant stars outside the main viewport gives a sense of isolation.'",
            "exits": {"north": "Hallway", "south":"O2"},
            "items": ["CafeKey"],
        },

        "Hallway" : {
            "description" : "A long corridor, dimly lit, with flickering lights casting eerie shadows. The hum of the ship’s systems echoes throughout, though now it feels a little strained. The doors lead to various parts of the ship. You feel a growing sense of urgency.",
            "exits": {"north": "Cafe", "south":"Admin", "east":"Engine", "west":"Storage"},
            "items": []
        },
        "Cafe" : {
            "description" : "Once a lively hub for the crew, this room is now deserted. Tables are overturned, and a half-empty mug sits abandoned. A vending machine hums softly in the corner, though it looks broken. The Café key you picked up earlier opens the door, and inside, you spot a torch, which might come in handy in case of emergencies—like the lights going out.",
            "exits": {"north": "Electrical", "south":"Hallway"},           
            "items": ["Torch"]
        },
        "Engine" : {
            "description" : "This room houses the beating heart of the ship. The engines rumble with an irregular rhythm, and steam hisses from cracked pipes. Something is definitely wrong here. Tools and scattered debris suggest someone was trying to make a repair but abandoned the effort. The ship won't function without this getting fixed. The power core is missing and needs to be retrieved.",
            "exits": {"west":"Hallway"},
            "items": []
        },
        "Storage" : {
            "description" : "A cramped room with rows of metal shelves stacked high with crates and supplies. The hum of machines and the stale smell of metal fills the air. The Power Core is stored here, along with other vital supplies for ship repairs. You also spot a toolbox on one of the shelves, which may come in handy later.",
            "exits": {"east":"Hallway", "west":"Navigation"},            
            "items": ["PowerCore", "ToolBox"]
        },
        "Electrical" : {
            "description" : "This small room is filled with exposed wires and flickering monitors. The smell of burnt circuits and the occasional spark from damaged equipment makes this a hazardous environment. You’ll need the toolbox from the Storage Room to fix the ship’s power supply. Be careful—this room is the key to restoring the lights and continuing the mission.",
            "exits": {"south":"Cafe"},            
            "items": ["LaserGun"]
        },
        "Navigation" : {
            "description" : "A quiet, dimly lit room with a large console displaying the ship’s trajectory and various star charts. A malfunctioning navigational system blinks urgently, displaying coordinates that don’t make sense. To proceed, you'll need to solve a puzzle involving the star charts to realign the ship's course and unlock further data about your mission’s destination.",
            "exits": {"east":"Storage"},
            "items": []
        },
        "O2" : {
            "description" : "A small, vital room filled with oxygen tanks and air-purification systems. The hiss of leaking gas fills the air, but something feels off. You can see faint signs of tampering. You notice the air thinning—this could get dangerous quickly. The room seems to have been disturbed recently.",
            "exits": {"north": "Admin", "east":"MedBay"},
            "items": []
        },
        "MedBay" : {
            "description" : "A sterile white room with medical beds and equipment neatly arranged. The faint smell of antiseptic lingers. It seems untouched by the chaos, but you feel a wave of unease. You know you may need this room if things turn worse.",
            "exits": {"west":"O2"},            
            "items": ["First Aid"]
        }
    } 
    
}


def show_room_description(room):
    print(f"\nYou are in {room}.")
    print(game_state["rooms"][room]["description"])
    exits = game_state["rooms"][room]["exits"]
    

def move(direction):
    current_room = game_state["current_room"]
    exits = game_state["rooms"][current_room]["exits"]
    
    if direction in exits:
        game_state["current_room"] = exits[direction]
        show_room_description(game_state["current_room"])
        
        if game_state["current_room"] in game_state["tasks"]:
            if game_state["tasks"][game_state["current_room"]]["status"] == "incomplete":
                task()
            else:
                print("Everything looks Good!")
    else:
        print("You can't go that way.")

def look(room=None):
    print(game_state["rooms"][room]["description"])
    print("\nExits: ")
    for exit, exit_room in game_state["rooms"][room]["exits"].items():
        print(f"-{exit}: {exit_room}")
    if game_state["rooms"][room]["items"]:
        print("\nItems available: " + ", ".join(game_state["rooms"][room]["items"]))

def task():
    room = game_state["current_room"]
    if game_state["tasks"][room]["status"] == "incomplete":
        print(game_state["tasks"][room]["description"])
    else:
        return

def pick_up_item(item):
    current_room = game_state["current_room"]
    for i in game_state["rooms"][current_room]["items"]:
        if i.lower() == item.lower():
            game_state["inventory"].append(i)
            game_state["rooms"][current_room]["items"].remove(i)
            print(f"You picked up {i}.")
            return
    print(f"There is no {item} here.")

def drop_item(item):
    current_room = game_state["current_room"]
    item_name_lower = item.lower()

    if item_name_lower in [item.lower() for item in game_state["inventory"]]:
        item_to_drop = next(item for item in game_state["inventory"] if item.lower() == item_name_lower)
        game_state["inventory"].remove(item_to_drop)
        game_state["rooms"][current_room]["items"].append(item_to_drop)
        print(f"You dropped {item_to_drop}.")
    else:
        print(f"You don't have {item}.")

def show_inventory():
    if game_state["inventory"]:
        print("Inventory: " + ", ".join(game_state["inventory"]))
    else:
        print("Your inventory is empty.")


def play_game():
    print("Welcome to the Spaceship Adventure!")
    show_room_description(game_state["current_room"])

    while True:
        command = input("\nWhat would you like to do?: ").lower().split()

        if command[0] == "move":
            if len(command) > 1:
                move(command[1])
            else:
                print("Please specify a direction to move (north, south, east, west).")
        
        elif command[0] == "pick":
            if len(command) > 1:
                pick_up_item(" ".join(command[1:]))
            else:
                print("Please specify an item to pick up.")

        elif command[0] == "drop":
            if len(command)>1:
                drop_item(" ".join(command[1:]))
            else:
                print("Please specify an item to drop.")
        
        elif command[0] == "inventory":
            show_inventory()
        
        elif command[0] == "look":
            look(game_state["current_room"])
        
        elif command[0] == "exit":
            print("Exiting game. Thanks for playing!")
            break
        
        else:
            print("Invalid command. Try 'move', 'pick', 'inventory', or 'exit'.")

play_game()
