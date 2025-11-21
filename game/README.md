Turn-based adventure game playable in terminal & web. Player navigates floors, fights enemies, collects items, and faces random events.

✅ Core Features

Player: HP, attack, speed, floor, coins

Equipment: Weapons, helmets, chests, boots, wings (stats additive & multiplicative)

Inventory: Auto-equip if slot empty; stacking supported

Events:

Lucky: heal, loot, coins, floor up

Unlucky: summon enemies, poison, floor down


Combat Engine: Turn-based fights, escape logic, auto floor progression

Randomization: Weighted item drops, event outcomes

• Current Challenges

Code complexity: modules highly interdependent, some long functions (random_item_event)

Incomplete/fragile logic: poison loops, some unlucky events, partial enemy loot handling

Validation gaps: optional enemy args, edge cases not fully guarded

Documentation: inconsistent docstrings and comments

• Next Steps

Refactor events: separate lucky/unlucky, weights, cooldowns

Introduce Monster class + structured enemy lists

Improve player/equipment validation & base stats preservation

Enhance logging & debugging for event outcomes and combat

Standardize docs + type hints + unit tests

Web & terminal interface refinement

• Current state

State: playable, major mechanics in place

Focus: glue systems together, fix edge cases, polish events & combat

