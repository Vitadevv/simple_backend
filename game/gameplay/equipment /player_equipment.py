from game.gameplay.entities.entities import Entity
from .errors import EquipmentError 
from .status import EquipStatus 
from datetime import datetime
from .item import Item
import logging 

log = logging.getLogger(__name__)

def _validate_slot(player: Entity, slot: str):
  if slot not in player.equipment:
    log.warning(f"{player.name} couldn't equip an item to invalid slot: {slot}")
    raise EquipmentError(f"Slot {slot} isn't valid!")
    
def _validate_item(player: Entity, item: str):
  if player.inventory.get(item, 0) < 1:
    log.warning(f"{player.name} couldn't equip {item} as it wasn't in their inventory")
    raise EquipmentError(f"There's no {item} to equip!")
    
def _apply_from_equipment(player: Entity):
  #ideally i need to validate if player is indeed an Entity 
  _attack = player.attack
  _hp = player.hp
  for item in player.equipment.values():
    if item:
      _attack = _attack * item.attack_multiply + item.attack_add
      _hp = _hp * item.hp_multiply + item.hp_add
  player.attack = _attack
  player.hp = _hp
    
def equip_item(player: Entity, slot: str, item: str) -> dict:
  _validate_slot(player, slot)   #slot first
  _validate_item(player, item) #item second 
  old_item = player.equipment[slot]
  if old_item:
    player.add_item(old_item, 1)
  player.remove_item(item, 1)
  player.equipment[slot] = item
  _apply_from_equipment(player)
  log.info(f"{player.name} equipped {item} at {slot}")
  return {
  "status": EquipStatus.EQUIPPED,
  "slot": slot,
  "equipped": item,
  "replaced": old_item
  }
  