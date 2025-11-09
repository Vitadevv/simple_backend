from random import randint, uniform, random, choice, choices
from ..entities import Entity, Player, Enemy
from .entities.entities_list import HUMANOIDS, MONSTERS
from ..equipment.items import Item, SWORDS, HELMETS, CHESTS, BOOTS, WINGS, ALL_ITEMS, ALL_ITEMS_FLAT, CATEGORY_CHANCES
from ..equipment import _apply_from_equipment
from typing import Optional 
from .combat_logic import fight_to_death


#lucky
def heal_event(player: Player):
  _amount = randint(1, 35)
  player.heal(_amount)
  return {
  "type": "heal",
  "value": _amount
}  
  
def random_item_event(player: Player):
  #ideally this needs to be refactored but too much codepasta to handle for now
  _types = list(CATEGORY_CHANCES.keys())
  _chances = list(CATEGORY_CHANCES.values())
  #respects _chances
  _select_type = choices(_types, weights=_chances, k=1)[0]
  _chosen_item = choice(list(ALL_ITEMS[_select_type].values()))
  #need to map because values ≠ keys in player.equipment
  _MAPPING = {
    "weapons": "weapon",
    "helmets": "helmet",
    "chests": "chest",
    "boots": "boots",
    "wings": "wings"
  }

  _select_type = _MAPPING[_select_type]
  
  if player.equipment[_select_type] is None:
    player.equipment[_select_type] = _chosen_item
  else:
    player.add_item(_chosen_item)
  _validate_item(player) 
  return {
    "type": "random item",
    "value": _chosen_item
    }
    
    
def floor_up_event(player: Player):
  _amount = 1
  if random() < 0.1:
    _amount = 2
  player.floor += _amount
  return {
  "type": "floor up",
  "value": _amount
  } 


def add_coins_event(player: Player):
  _amount = randint(10, 30)
  if random() < 0.5:
    _amount = randint(30, 40)
  if random() < 0.1:
    _amount = randint(40, 50)
  player.coins += _amount
  return {
  "type": "add coins",
  "value": _amount
  }


#unlucky
def summon_enemy_event(player: Player, enemy: Optional[Entity] = None):
"""
Convoluted approach. I'll merge 2 groups first, then choose an entity from the list, and initialize a battle automatically. Enemy of choice can be passed through arguments 
"""
if not enemy:
  _merged_lst = list(HUMANOIDS) + list(MONSTERS)
  _select_enemy = choice(_merged_lst)
else: 
  _select_enemy = enemy
fight_to_death(player, _select_enemy)
#fight_to_death returns already 


def poison_event(player: Player):
  _fixed_player_floor = player.floor
  while player.floor == _fixed_player_floor:
    player.hp -= 10
    if player.is_alive():
      player.attack *= uniform(0.5, 0.9)
  return {
  "type": "poison player",
  "value": None
  } 
  

def floor_down_event(player: Player):
  _amount = 1
  if random() < 0.1:
    _amount = 2
  player.floor -= _amount
  return {
  "type": "floor down",
  "value": _amount
  } 
  
