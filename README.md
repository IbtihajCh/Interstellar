# 🚀 Interstellar — Text-Based Adventure Game

> *Navigate the stars, save the crew, and uncover the mysteries aboard your spaceship.*

---

## Overview

**Interstellar** is a text-based adventure game that immerses players in a sci-fi environment aboard a spaceship. Players explore different rooms, interact with characters, complete tasks, and solve a final puzzle to save the ship.

---

## Features

- 🗺️ **Exploration** — Navigate through multiple rooms with unique descriptions and items.
- 🤖 **NPC Interaction** — Engage with non-player characters to gather information and advance the story.
- 🎒 **Inventory Management** — Collect, use, and drop items to solve puzzles and complete tasks.
- ⚡ **Dynamic Gameplay** — Make choices that affect your progress and interactions within the game.

---

## Installation

### Prerequisites
- Python 3.x installed on your system

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/interstellar.git
   cd interstellar
   ```

2. **Run the game:**
   ```bash
   python game.py
   ```

---

## Gameplay

### Objective

Your main goal in **Interstellar** is to successfully navigate the spaceship, complete various tasks, and ultimately solve the final puzzle to save the crew and the ship.

### Navigating the Game

- Players begin in the **Admin room** and can move to other rooms using the `move` command followed by the room name.
  ```
  move O2
  ```
- Each room contains unique elements that can be explored, including items and NPCs.

### Interacting with Characters

- Characters (NPCs) can provide essential information or tasks. Use the `interact` command followed by the character's name.
  ```
  interact crewmate
  ```

### Collecting and Using Items

- Pick up items using the `pick up` command:
  ```
  pick up firstaid
  ```
- Use collected items to complete tasks, unlock new areas, or aid in interactions:
  ```
  use firstaid
  ```

---

## Commands

| Command | Description |
|---|---|
| `move [room]` | Move to a specified room (e.g., `move O2`) |
| `look` | Describe the current room, including exits and items available |
| `interact [NPC]` | Engage with a specified NPC (e.g., `interact crewmate`) |
| `pick up [item]` | Collect an item from the current room (e.g., `pick up firstaid`) |
| `use [item]` | Use an item from your inventory (e.g., `use firstaid`) |
| `drop [item]` | Drop an item from your inventory (e.g., `drop firstaid`) |
| `inventory` | Show the items currently in your inventory |
| `examine [item]` | Get a detailed description of a specific item (e.g., `examine toolbox`) |
| `task` | Check for any tasks that need completion in the current room |
| `map` | Display a visual map of the spaceship layout |
| `help` | Display a list of available commands |
| `quit` | Exit the game |

---

## Game Structure

The game uses a `game_state` dictionary containing the following key components:

| Component | Description |
|---|---|
| **Rooms** | Each room is defined by its description, exits, items, and lock status |
| **Items** | Descriptions and functionalities for each collectible item |
| **Tasks** | Status of tasks that need to be completed in various rooms |
| **NPCs** | Characters available for interaction and their dialogue |

### Sample Room Structure

```python
"rooms": {
    "Admin": {
        "description": "A control room filled with screens and consoles.",
        "exits": {"south": "O2"},
        "items": [],
        "locked": False,
        "task_req": "Talk to the crewmate for information."
    }
}
```

---

## Tasks and Progression

- Each room may have associated **tasks** that players must complete to unlock further areas or to progress in the story.
- Tasks can vary from:
  - Interacting with NPCs
  - Collecting specific items
  - Solving puzzles

---

## License

This project is open source. Feel free to fork, modify, and share!
