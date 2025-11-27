# Dungeon Master: Terminal-Based Adventure Game

Turn-based dungeon crawler game playable in the terminal. Navigate through procedurally generated floors, battle enemies, collect equipment, and survive as long as possible!

![Dungeon Master](./dungeon_master.jpg)

## 🎮 Quick Start

```bash
cd c:\Users\Eleve\Desktop\simple_backend
python -m game.main
```

Select language (English/Français), create your character, and begin your adventure!

---

## ✅ Core Features

### Player System
- **Character Stats**: HP (200), Attack (10), Speed (10) - all customizable
- **Progression**: Floor advancement with natural progression (+1/turn) plus event-based floor changes
- **Inventory**: Equipment slots (weapon, helmet, chest, boots, wings) with auto-equip on pickup
- **Currency**: Coins collected from events and milestones, used for future shop system
- **Persistence**: Best run tracking (furthest floor reached, time elapsed)

### Combat System
- **Turn-Based Fights**: Player vs Enemy with speed-based turn order
- **Equipment Scaling**: Stats scale dynamically (additive + multiplicative)
- **Enemy Difficulty**: Floor-based scaling with 10 tiers (multipliers from 1.0x to 8.75x)
- **Victory/Defeat**: Proper combat outcome tracking and display

### Event System (9 Types)
| Lucky Events | Unlucky Events | Floor Events |
|--------------|----------------|--------------|
|     Heal     |  Enemy Combat  |   Floor Up   |
|  Item Drop   |     Poison     |  Floor Down  |
|    Coins     |                |              |

### Path Selection
- **3 Choices Per Turn**: High/Medium/Low risk with different event probabilities
- **Deceptive Hints**: 10% chance path hint misleads the player
- **Contextual Messages**: Hint-specific or generic event outcomes

### Milestone System
- **Milestone Floors**: 10, 20, 30, 40... 100
- **Scaled Rewards**: Coins increase exponentially (40 → 20,000 at floor 100)
- **Variance**: ±15% randomization on rewards

### Localization
- **Full English & French Support**
- **Config-Driven Text**: All UI strings in YAML (no hardcoding)
- **Language Switching**: Menu option to toggle EN/FR at any time

---

## 📁 Project Structure

```
simple_backend/
├── README.md                          # This file
├── pyproject.toml                     # Python project metadata & dependencies
├── .gitignore
│
├── game/
│   ├── main.py                        # Entry point
│   ├── engine.py                      # Core game loop orchestration
│   ├── builder.py                     # Factory: player/paths/events/milestones
│   ├── __init__.py
│   │
│   ├── config/
│   │   ├── loader.py                  # YAML config loading system
│   │   ├── helpers.py                 # Config utility functions
│   │   ├── en/config.yaml             # English UI text & game settings
│   │   └── fr/config.yaml             # French UI text & game settings
│   │
│   ├── gameplay/
│   │   ├── entities/
│   │   │   ├── entities.py            # Base Entity class (HP, combat)
│   │   │   ├── player.py              # Player class (inventory, timer)
│   │   │   ├── enemies.py             # Enemy class (scaling logic)
│   │   │   └── enemies_list.py        # Factory for 20+ enemy types
│   │   │
│   │   ├── equipment/
│   │   │   ├── player_equipment.py    # Inventory & equipment management
│   │   │   ├── errors.py              # Custom exceptions
│   │   │   └── items/
│   │   │       ├── item.py            # Item base class
│   │   │       └── items_list.py      # 50+ item definitions
│   │   │
│   │   ├── events/
│   │   │   └── events.py              # 9 event handler functions
│   │   │
│   │   └── combat_logic/
│   │       └── adventure.py           # Turn-based combat engine
│   │
│   └── menu/
│       └── menu_terminal.py           # Terminal UI & main menu
│
└── logs/
    └── game.log                       # Runtime logs
```

---

## 🎯 Game Loop Flow

```
1. Player Creation (set name, language)
2. Game Loop (while alive):
   a. Display current floor & stats
   b. Generate 3 random paths (risk-based)
   c. Player selects path
   d. Event executes (enemy/heal/poison/coins/item/floor change)
   e. Natural progression: +1 floor (unless floor_up/down occurred)
   f. Check milestone (auto-reward coins if applicable)
   g. Check death (HP ≤ 0 → end run)
3. End Run Display (best floor, time, new record check)
```

---

## 🔧 Technical Details

### Configuration System
All game settings are stored in `game/config/{en,fr}/config.yaml`:
- **Game Settings**: Starting HP/attack/speed, difficulty scaling
- **Event Messages**: All 9 event types with translations
- **Paths & Hints**: 12 unique hints across 3 risk levels
- **Risk Labels**: Localized difficulty names
- **Milestone Rewards**: 10 milestone tiers with variance

### Event Routing
Events return a structured dict:
```python
{
  "type": "enemy|poison|heal|coins|item|floor_up|floor_down|random_item|add_coins",
  "value": <event_specific_data>,
  "report": <optional_combat_report>
}
```

### Enemy Scaling
Floor-based multiplier system:
- Tier 1 (floors 1-9): 1.0x
- Tier 2 (floors 10-19): 1.1x
- Tier 10 (floors 90-99): 5.85x
- Tier 11 (floor 100): 8.75x

### Combat Mechanics
- Speed determines turn order
- Damage = Attack ± 20% variance
- Escape attempts scale with player speed
- Combat continues until one side dies

---

## ✨ Current State: **PRODUCTION READY**

### ✅ Completed
- Full game loop with event handling
- All 9 event types functional
- Natural floor progression
- Milestone detection & rewards
- Equipment system with stat scaling
- 20+ enemies with contextual loot
- Turn-based combat engine
- Full localization (EN/FR)
- Terminal UI with menu system
- Comprehensive logging

### 📋 Future Features (Planned)
- **Shop System**: Spend coins to purchase equipment upgrades
- **Persistent Coins**: Save/load progression between sessions
- **Web Interface**: REST API + web UI for gameplay
- **Advanced Events**: Debuffs, artifacts, temporary boosters
- **Difficulty Modes**: Custom scaling options
- **Leaderboards**: Global best run tracking

---

## 🚀 Installation & Setup

### Requirements
- Python 3.13+
- PyYAML (included in pyproject.toml)

### Install
```bash
# Clone or navigate to project
cd simple_backend

# Install dependencies (using pyproject.toml)
pip install -e .
```

### Run
```bash
python -m game.main
```

### Run with Logging
Logs are automatically written to `logs/game.log` with INFO level and above.

---

## 📊 Statistics

- **Total Lines of Code**: ~1,200 (core game logic)
- **Event Types**: 9 (lucky, unlucky, floor progression)
- **Enemy Types**: 20+ (humanoids + monsters)
- **Equipment Items**: 50+ (weapons, armor, accessories)
- **Unique Hints**: 12 (context-specific path descriptions)
- **Supported Languages**: 2 (English, French)

---

## 🎓 Architecture Highlights

### Design Patterns Used
- **Factory Pattern**: `create_player()`, `create_3_paths()`, `create_event()`
- **Event-Driven**: Events return structured data for flexible handling
- **Config-Driven**: Externalized all text/settings to YAML
- **Dependency Injection**: Config passed to functions requiring localization

### Code Organization
- **Separation of Concerns**: UI, logic, entities, config all separate
- **DRY Principle**: No hardcoded strings; all text in config files
- **Type Safety**: Type hints throughout (mostly) for IDE support
- **Logging**: Comprehensive INFO-level logs for debugging

---

## 📝 License & Credits

**Project**: Dungeon Master  
**Author**: Vitadevv  
**Status**: Active Development  
**Repository**: simple_backend (main branch)

