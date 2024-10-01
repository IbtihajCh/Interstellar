import json

# Initialize the game state with everything in it
game_state = {
    "current_room" : "Admin",
    "inventory" : [],
    "game_over" : False,
    "tasks": {
        "Cafe": {"status": "incomplete",
                  "description": "", 
                  "item":"CafeKey"},

        "Electrical": {"status": "incomplete",
                       "description": "\nTask: You need a ToolBox to repair Electricity", 
                       "item":"ToolBox"},

        "Engine": {"status": "incomplete", 
                   "description": "\nTask: You need a PowerCore to repair the engines", 
                   "item":"PowerCore"},

        "O2": {"status":"incomplete", 
               "description": "\nTask: You need a LaserGun to kill the Alien", 
               "item":"LaserGun"},

        "Navigation": {"status": "incomplete", 
                       "description": "\nTask: You need to complete the word. Hints are in different rooms", 
                       "word":"Imposter"},
    },

    "items": {
        "CafeKey" : {"description": "\nA key for the cafe. You can use it to unlock the door to the cafe."},
        "PowerCore" : {"description": "\nA power core that can be used to repair the engines."},
        "ToolBox" : {"description": "\nA toolbox that can be used to fix the electrical system."},
        "LaserGun" : {"description": "\nA laser gun that can be used to kill the alien."},
        "FirstAidKit" : {"description":"\nA first aid kit that can be used to heal yourself."},
        "Torch" : {"description":"\nA torch that can be used to see when electricity malfunctions."},
        "firstAid" : {"description":"\nA first aid kit that can be used to heal yourself."}
    },

    "npc" : {
    "Crewmate" : {
        "dialogue" : "\nI've been watching everyone closely... something isn't right. Someone on this ship isn't who they say they are. I think we're dealing with... an impostor. Be careful who you trust.",
    },
    "Alien" : {
        "dialogue" : "\nGrrr... human... you shouldn't be here. This ship is mine now. You'll never escape... \n Rrraaahhhr! You think you can defeat me? I am the master of this ship!\nHssss... you're just a tiny little human. I'll crush you like the insignificant insect you are.",
    },
    "AIAssistant" : {
        "dialogue" : "\nHello, Captain. Navigation systems are compromised. You'll need to solve the puzzle to restore the ship's course. Be careful: failure could be disastrous.",
    }
},

    "rooms" : {
        "Admin": {
            "description": "\nThe nerve center of the ship, filled with blinking consoles, star charts, and system diagnostics. A key for the Café lies on the floor. The ship feels eerily quiet as warnings flash about engine malfunctions. The soft glow of distant stars outside the main viewport gives a sense of isolation.'",
            "exits": {"north": "Hallway", "south":"O2"},
            "items": [],
            "locked": False,
            "task_req" : ""
        },

        "Hallway" : {
            "description" : "\nA long corridor, dimly lit, with flickering lights casting eerie shadows. The hum of the ship’s systems echoes throughout, though now it feels a little strained. The doors lead to various parts of the ship. You feel a growing sense of urgency.",
            "exits": {"north": "Cafe", "south":"Admin", "east":"Engine", "west":"Storage"},
            "items": [],
            "locked": False,
            "task_req" : ""
        },
        "Cafe" : {
            "description" : "\nOnce a lively hub for the crew, this room is now deserted. Tables are overturned, and a half-empty mug sits abandoned. A vending machine hums softly in the corner, though it looks broken. The Café key you picked up earlier opens the door, and inside, you spot a torch, which might come in handy in case of emergencies—like the lights going out.",
            "exits": {"north": "Electrical", "south":"Hallway"},           
            "items": ["Torch"],
            "locked": True,
            "task_req" : "\nThis room is locked. You need a CafeKey to unlock it."
        },
        "Engine" : {
            "description" : "\nThis room houses the beating heart of the ship. The engines rumble with an irregular rhythm, and steam hisses from cracked pipes. Something is definitely wrong here. Tools and scattered debris suggest someone was trying to make a repair but abandoned the effort. The ship won't function without this getting fixed. The power core is missing and needs to be retrieved.",
            "exits": {"west":"Hallway"},
            "items": ["CafeKey"],
            "locked": False,
            "task_req" : ""
        },
        "Storage" : {
            "description" : "\nA cramped room with rows of metal shelves stacked high with crates and supplies. The hum of machines and the stale smell of metal fills the air. The Power Core is stored here, along with other vital supplies for ship repairs. You also spot a toolbox on one of the shelves, which may come in handy later.",
            "exits": {"east":"Hallway", "west":"Navigation"},            
            "items": ["PowerCore", "ToolBox"],
            "locked": False,
            "task_req" : ""
        },
        "Electrical" : {
            "description" : "\nThis small room is filled with exposed wires and flickering monitors. The smell of burnt circuits and the occasional spark from damaged equipment makes this a hazardous environment. You’ll need the toolbox from the Storage Room to fix the ship’s power supply. Be careful—this room is the key to restoring the lights and continuing the mission.",
            "exits": {"south":"Cafe"},            
            "items": ["LaserGun"],
            "locked": True,
            "task_req" : "\nThere is no light in this room. You might need a torch to fix it."
        },
        "Navigation" : {
            "description" : "\nA quiet, dimly lit room with a large console displaying the ship’s trajectory and various star charts. A malfunctioning navigational system blinks urgently, displaying coordinates that don’t make sense. To proceed, you'll need to solve a puzzle involving the star charts to realign the ship's course and unlock further data about your mission’s destination.",
            "exits": {"east":"Storage"},
            "items": [],
            "locked": True,
            "task_req" : "\nHave u completed your tasks? No? Bro what u doing go complete them first"
        },
        "O2" : {
            "description" : "\nA small, vital room filled with oxygen tanks and air-purification systems. The hiss of leaking gas fills the air, but something feels off. You can see faint signs of tampering. You notice the air thinning—this could get dangerous quickly. The room seems to have been disturbed recently.",
            "exits": {"north": "Admin", "east":"MedBay"},
            "items": [],
            "locked": True,
            "task_req" : "\nUh Oh! It seems like Electrical isn't fixed. Fix Electrical first!"
        },
        "MedBay" : {
            "description" : "\nA sterile white room with medical beds and equipment neatly arranged. The faint smell of antiseptic lingers. It seems untouched by the chaos, but you feel a wave of unease. You know you may need this room if things turn worse.",
            "exits": {"west":"O2"},            
            "items": ["FirstAid"],
            "locked": False,
            "task_req" : "\nSeems like you are injured from Alien fight. Use first aid to heal yourself."
        }
    } 
    
}

#Saves Game
def save_game():
    with open("game_state.json", "w") as f:
        json.dump(game_state, f)
    print("\nGame Saved Successfully!")



#Loads Game
def load_game():
    global game_state
    try:
        with open("game_state.json", "r") as f:
            game_state = json.load(f)
        print("\nGame Loaded Successfully!")

    except FileNotFoundError:
        print("\nNo saved game found. Starting a new game.")




#Quits Game
def quit_game():
    save_game()
    print("\nThank you for playing!")
    exit()
    


#Help Function to display available commands
def help():
    commands = {
        "move": "Usage: move [direction]\nMove in a direction (north, south, east, or west) to explore different rooms.\n",
        "take": "Usage: Take [item]\nPick up an item from the current room and add it to your inventory.\n",
        "drop": "Usage: drop [item]\nDrop an item from your inventory into the current room.\n",
        "inventory": "Usage: inventory\nCheck your current inventory to see what items you are carrying.\n",
        "use": "Usage: use [item]\nUse an item from your inventory to perform specific tasks in the current room.\n",
        "examine": "Usage: examine [item]\nGet a detailed description of an item in the current room or your inventory.\n",
        "look": "Usage: look\nGet a description of the current room and see what items or NPCs are present.\n",
        "interact": "Usage: interact\nTalk to NPCs (Non-Player Characters) in the current room to gather information.\n",
        "puzzle": "Usage: puzzle\nInitiate the puzzle task in the Navigation room to progress towards victory.\n",
        "task": "Usage: task\nGet a description of the current task in the current room.\n",
        "save": "Usage: save\nSave the current state of the game so you can resume later.\n",
        "load": "Usage: load\nLoad a previously saved game state to continue playing.\n",
        "quit": "Usage: quit\nSave the game and exit.\n",
        "help": "Usage: help\nShow a list of all available commands and their usage.\n",
    }

    print("Available commands:\n")
    for command, description in commands.items():
        print(f"{command}: {description}")




#prints room description
def show_room_description(room):
    print(f"\nYou are in {room}.")
    print(game_state["rooms"][room]["description"])
    exits = game_state["rooms"][room]["exits"]
    


#moves the character from one room to other
def move(direction):
    current_room = game_state["current_room"]
    exits = game_state["rooms"][current_room]["exits"]

    if direction in exits:
        next_room = exits[direction]
        if game_state["rooms"][next_room]["locked"]:
            print(game_state["rooms"][next_room]["task_req"])
        else:
            game_state["current_room"] = next_room
            show_room_description(game_state["current_room"])
            if game_state["current_room"] in game_state["tasks"]:
                if game_state["tasks"][game_state["current_room"]]["status"] == "incomplete":
                    task()
                else:
                    print("Everything looks Good!")
    else:
        print("Oops! You hit a wall. Please try another direction.")




#Reset Game for replay
def reset_game_state():
    global game_state
    game_state = {
    "current_room" : "Admin",
    "inventory" : ["CafeKey","FirstAid","Torch","LaserGun","ToolBox","PowerCore"],
    "tasks": {
        "Cafe": {"status": "incomplete",
                  "description": "", 
                  "item":"CafeKey"},

        "Electrical": {"status": "incomplete",
                       "description": "\nTask: You need a ToolBox to repair Electricity", 
                       "item":"ToolBox"},

        "Engine": {"status": "incomplete", 
                   "description": "\nTask: You need a PowerCore to repair the engines", 
                   "item":"PowerCore"},

        "O2": {"status":"incomplete", 
               "description": "\nTask: You need a LaserGun to kill the Alien", 
               "item":"LaserGun"},

        "Navigation": {"status": "incomplete", 
                       "description": "\nTask: You need to complete the word. Hints are in different rooms", 
                       "word":"Imposter"},
    },

    "items": {
        "CafeKey" : {"description": "\nA key for the cafe. You can use it to unlock the door to the cafe."},
        "PowerCore" : {"description": "\nA power core that can be used to repair the engines."},
        "ToolBox" : {"description": "\nA toolbox that can be used to fix the electrical system."},
        "LaserGun" : {"description": "\nA laser gun that can be used to kill the alien."},
        "FirstAidKit" : {"description":"\nA first aid kit that can be used to heal yourself."},
        "Torch" : {"description":"\nA torch that can be used to see when electricity malfunctions."},
        "firstAid" : {"description":"\nA first aid kit that can be used to heal yourself."}
    },

    "npc" : {
    "Crewmate" : {
        "dialogue" : "\nI've been watching everyone closely... something isn't right. Someone on this ship isn't who they say they are. I think we're dealing with... an impostor. Be careful who you trust.",
    },
    "Alien" : {
        "dialogue" : "\nGrrr... human... you shouldn't be here. This ship is mine now. You'll never escape... \n Rrraaahhhr! You think you can defeat me? I am the master of this ship!\nHssss... you're just a tiny little human. I'll crush you like the insignificant insect you are.",
    },
    "AIAssistant" : {
        "dialogue" : "\nHello, Captain. Navigation systems are compromised. You'll need to solve the puzzle to restore the ship's course. Be careful: failure could be disastrous.",
    }
},

    "rooms" : {
        "Admin": {
            "description": "\nThe nerve center of the ship, filled with blinking consoles, star charts, and system diagnostics. A key for the Café lies on the floor. The ship feels eerily quiet as warnings flash about engine malfunctions. The soft glow of distant stars outside the main viewport gives a sense of isolation.'",
            "exits": {"north": "Hallway", "south":"O2"},
            "items": [],
            "locked": False,
            "task_req" : ""
        },

        "Hallway" : {
            "description" : "\nA long corridor, dimly lit, with flickering lights casting eerie shadows. The hum of the ship’s systems echoes throughout, though now it feels a little strained. The doors lead to various parts of the ship. You feel a growing sense of urgency.",
            "exits": {"north": "Cafe", "south":"Admin", "east":"Engine", "west":"Storage"},
            "items": [],
            "locked": False,
            "task_req" : ""
        },
        "Cafe" : {
            "description" : "\nOnce a lively hub for the crew, this room is now deserted. Tables are overturned, and a half-empty mug sits abandoned. A vending machine hums softly in the corner, though it looks broken. The Café key you picked up earlier opens the door, and inside, you spot a torch, which might come in handy in case of emergencies—like the lights going out.",
            "exits": {"north": "Electrical", "south":"Hallway"},           
            "items": ["Torch"],
            "locked": True,
            "task_req" : "\nThis room is locked. You need a CafeKey to unlock it."
        },
        "Engine" : {
            "description" : "\nThis room houses the beating heart of the ship. The engines rumble with an irregular rhythm, and steam hisses from cracked pipes. Something is definitely wrong here. Tools and scattered debris suggest someone was trying to make a repair but abandoned the effort. The ship won't function without this getting fixed. The power core is missing and needs to be retrieved.",
            "exits": {"west":"Hallway"},
            "items": ["CafeKey"],
            "locked": False,
            "task_req" : ""
        },
        "Storage" : {
            "description" : "\nA cramped room with rows of metal shelves stacked high with crates and supplies. The hum of machines and the stale smell of metal fills the air. The Power Core is stored here, along with other vital supplies for ship repairs. You also spot a toolbox on one of the shelves, which may come in handy later.",
            "exits": {"east":"Hallway", "west":"Navigation"},            
            "items": ["PowerCore", "ToolBox"],
            "locked": False,
            "task_req" : ""
        },
        "Electrical" : {
            "description" : "\nThis small room is filled with exposed wires and flickering monitors. The smell of burnt circuits and the occasional spark from damaged equipment makes this a hazardous environment. You’ll need the toolbox from the Storage Room to fix the ship’s power supply. Be careful—this room is the key to restoring the lights and continuing the mission.",
            "exits": {"south":"Cafe"},            
            "items": ["LaserGun"],
            "locked": True,
            "task_req" : "\nThere is no light in this room. You might need a torch to fix it."
        },
        "Navigation" : {
            "description" : "\nA quiet, dimly lit room with a large console displaying the ship’s trajectory and various star charts. A malfunctioning navigational system blinks urgently, displaying coordinates that don’t make sense. To proceed, you'll need to solve a puzzle involving the star charts to realign the ship's course and unlock further data about your mission’s destination.",
            "exits": {"east":"Storage"},
            "items": [],
            "locked": True,
            "task_req" : "\nHave u completed your tasks? No? Bro what u doing go complete them first"
        },
        "O2" : {
            "description" : "\nA small, vital room filled with oxygen tanks and air-purification systems. The hiss of leaking gas fills the air, but something feels off. You can see faint signs of tampering. You notice the air thinning—this could get dangerous quickly. The room seems to have been disturbed recently.",
            "exits": {"north": "Admin", "east":"MedBay"},
            "items": [],
            "locked": True,
            "task_req" : "\nUh Oh! It seems like Electrical isn't fixed. Fix Electrical first!"
        },
        "MedBay" : {
            "description" : "\nA sterile white room with medical beds and equipment neatly arranged. The faint smell of antiseptic lingers. It seems untouched by the chaos, but you feel a wave of unease. You know you may need this room if things turn worse.",
            "exits": {"west":"O2"},            
            "items": ["FirstAid"],
            "locked": False,
            "task_req" : "\nSeems like you are injured from Alien fight. Use first aid to heal yourself."
        }
    } 
    
}
    


#Displays items and exits and description of the room

def look(room=None):
    print(game_state["rooms"][room]["description"])
    print("\nExits: ")
    for exit, exit_room in game_state["rooms"][room]["exits"].items():
        print(f"-{exit}: {exit_room}")
    if game_state["rooms"][room]["items"]:
        print("\nItems available: " + ", ".join(game_state["rooms"][room]["items"]))
    if room == "Admin":
        print("\nThere is a Crewmate here. They look worried.")
    elif room == "O2":
        print("\nAn Alien is lurking around, making strange noises.")
    elif room == "Navigation":
        print("\nThe AI Assistant is here, monitoring the ship’s systems.")




#prints the map of the whole game
def map():
    print("\n                         Electrical          ")
    print ("\n                             ||          ")
    print("\n                          Cafe Room       ")
    print("\n                             ||          ")
    print("\nNavigation --- Storage --- Hallway --- Engine Room ")
    print("\n                             ||          ")
    print("\n                            Admin       ")
    print ("\n                             ||          ")
    print("\n                            O2 --- Medbay ")





# Function to display tasks for the current room
def task():
    room = game_state["current_room"]

    if room in game_state["tasks"]:  
        if game_state["tasks"][room]["status"] == "incomplete":
            print(game_state["tasks"][room]["description"])  
        else:
            print("There is no task here.")  
    else:
        print("There are no tasks here.") 




#picks item up and move into inventory
def pick_up_item(item):
    current_room = game_state["current_room"]
    for i in game_state["rooms"][current_room]["items"]:
        if i.lower() == item.lower():
            game_state["inventory"].append(i)
            game_state["rooms"][current_room]["items"].remove(i)
            print(f"{i} was added to your inventory.")
            return
    print(f"There is no {item} here.")




#drop items in whichever room u are
def drop_item(item):
    current_room = game_state["current_room"]
    item_name_lower = item.lower()

    if item_name_lower in [item.lower() for item in game_state["inventory"]]:
        item_to_drop = next(item for item in game_state["inventory"] if item.lower() == item_name_lower)
        game_state["inventory"].remove(item_to_drop)
        game_state["rooms"][current_room]["items"].append(item_to_drop)
        print(f"You dropped {item_to_drop}.")
    else:
        print(f"\nYou don't have {item}.")




#To use certain items to perform certain tasks
def use_item(item):
    item = item.lower()
    current_room = game_state["current_room"]
    if item in [i.lower() for i in game_state["inventory"]]:
        if item == "cafekey" and current_room == "Hallway" and game_state["rooms"]["Cafe"]["locked"]:
            game_state["rooms"]["Cafe"]["locked"] = False
            game_state["inventory"] = [i for i in game_state["inventory"] if i.lower() != item]
            print("\nYou used the CafeKey to unlock the Cafe.")

        elif item == "powercore" and current_room == "Engine" and game_state["tasks"]["Engine"]["status"] == "incomplete":
            game_state["tasks"]["Engine"]["status"] = "complete"
            game_state["inventory"] = [i for i in game_state["inventory"] if i.lower() != item]
            print("\nYou used the PowerCore to repair the engines. Engines are up and running.")

        elif item == "toolbox" and current_room == "Electrical" and game_state["tasks"]["Electrical"]["status"] == "incomplete":
            game_state["tasks"]["Electrical"]["status"] = "complete"
            game_state["inventory"] = [i for i in game_state["inventory"] if i.lower() != item]
            game_state["rooms"]["O2"]["locked"] = False
            print("\nFinally lights are restored!")

        elif item == "torch" and current_room == "Cafe" and game_state["rooms"]["Electrical"]["locked"]:
            game_state["rooms"]["Electrical"]["locked"] = False
            game_state["inventory"] = [i for i in game_state["inventory"] if i.lower() != item]
            print("\nAhh finally we can see something in the Electrical")

        elif item == "lasergun" and current_room == "O2" and game_state["tasks"]["O2"]["status"] == "incomplete":
            game_state["tasks"]["O2"]["status"] = "complete"
            game_state["inventory"] = [i for i in game_state["inventory"] if i.lower() != item]
            print("\nYou killed the Alien! Now go to the MedBay to tend to your wounds.")

        elif item == "firstaid":
            print("\nNow since you are already healed up. I guess it's time to fix the Navigation.")
            game_state["inventory"] = [i for i in game_state["inventory"] if i.lower() != item]
            game_state["rooms"]["Navigation"]["locked"] = False

        else:
            print("\nYou can't use that item.")
    else:
        print("\nSilly you! Using an item you don't even possess")




#To examine certain items
def examine(item):
    
    item = item.lower()  
    current_room = game_state["current_room"]
    if item in [i.lower() for i in game_state["rooms"][current_room]["items"]]:
        for key in game_state["items"]:
            if key.lower() == item:
                print(game_state["items"][key]["description"])
                return
    elif item in [i.lower() for i in game_state["inventory"]]:
        for key in game_state["items"]:
            if key.lower() == item:
                print(game_state["items"][key]["description"])
                return
    else:
        print(f"\nThere is no {item} here.")




#Displays Inventory
def show_inventory():
    
    if game_state["inventory"]:
        print("Inventory: " + ", ".join(game_state["inventory"]))
    else:
        print("\nYour inventory is empty.")




#Interact with NPCs
def interact_npc():
    current_room = game_state["current_room"]
    
    if current_room == "Admin":
        print(f'\nYou talk to the Crewmate:\n"{game_state["npc"]["Crewmate"]["dialogue"]}"')
    elif current_room == "O2":
        print(f'\nYou encounter the Alien:\n"{game_state["npc"]["Alien"]["dialogue"]}"')
    elif current_room == "Navigation":
        print(f'\nThe AI Assistant speaks:\n"{game_state["npc"]["AIAssistant"]["dialogue"]}"')
    else:
        print("There is no one to interact here.")




#Final word Guessing puzzle
def puzzle():
   
    print("\nIf you think you know the word, type 'answer' to submit it.")

    while True:
        command = input("\nWhat would you like to do? ").lower().split()

        if command[0] == "answer":
            answer = input("\nEnter your answer: ")
            check_puzzle_answer(answer)
            if game_state["game_over"]:
                break
        elif command[0] == "hint":
            print("\nHere's a hint: the word is hidden in plain sight.")
        else:
            print("Invalid command. Try 'answer' or 'hint'.")




#checks the answer of the puzzle
def check_puzzle_answer(answer):
    if answer.lower() == "imposter":
        print("\nAll Tasks are completed Successfully. \nYou have completed the game!")
        print("\n Now the ship is on the correct course to reach the Earth.")
        game_state["game_over"] = True
    else:
        print("\nSorry, that's not the correct answer. Try again!")




#To replay the game
def replay_game():
    while True:
        user_input = input("Do you want to play again? (yes/no): ").strip().lower()
        if user_input in ["yes", "y"]:
            reset_game_state()  # Reset the game state
            play_game()    # Start the game again
            break  # Exit the loop after restarting the game
        elif user_input in ["no", "n"]:
            print("Thanks for playing!")
            break  # Exit the loop and end the program
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")




#Main Game function that is handling the whole game
def play_game():
    print("Welcome to Interstellar!")
    show_room_description(game_state["current_room"])

    while True:
        command = input("\nWhat would you like to do?: ").lower().split()

        if command[0] == "move":
            if len(command) > 1:
                move(command[1])
            else:
                print("I guess there are 4 directions only named (north, south, east, west).")
        
        elif command[0] == "pick":
            if len(command) > 1:
                pick_up_item(" ".join(command[1:]))
            else:
                print("Please specify an item to pick up.")

        elif command[0] == "use":
            if len(command) > 1:
                use_item(" ".join(command[1:]))
            else:
                print("Please specify an item to use.")

        elif command[0] == "drop":
            if len(command)>1:
                drop_item(" ".join(command[1:]))
            else:
                print("Please specify an item to drop.")
        
        elif command[0] == "inventory":
            show_inventory()
        
        elif command[0] == "look":
            look(game_state["current_room"])

        elif command[0] == "examine":
            if len(command) > 1:
                examine(" ".join(command[1:]))
            else:
                print("Please specify an item to examine.")

        elif command[0] == "interact":
            if len(command) > 1:
                interact_npc()
            else:
                print("Please specify an NPC to interact with.")

        elif command [0] == "map":
            map()

        elif command [0] == "task":
            task()

        elif command [0] == "replay":
            replay_game()
        
        elif command[0] == "save":
            save_game()
            continue

        elif command[0] == "load":
            load_game()
            show_room_description(game_state["current_room"])
            continue

        elif command[0] == "puzzle":
            puzzle()
        
        elif command[0] == "help":
            help()

        elif command[0] == "quit":
            quit_game()
            break
        
        else:
            print("Invalid command. Use 'help' for a list of commands.")



play_game()
