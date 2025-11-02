from __future__ import annotations 
from ..errors import EquipmentError 
from .entities import Entity
from ..player_equipment import equip_item
from ..item import Item


class Player(Entity):
  def __init__(self, name: str):
    super().__init__(name = name, hp = 200, attack = 10, speed = 10)     
    self.inventory: dict[Item, int] = {}
    self.equipment: dict[str, Item | None] = 
    {
    "weapon": None,
    "helmet": None,
    "chest": None,
    "boots": None,
    "wings": None
    }
    
  def add_item(self, item: Item, quantity: int) -> None:
    self.inventory[item] = self.inventory.get(item, 0) + quantity 
    
  def remove_item(self, item: Item, quantity: int = 1) -> None:
    current: int = self.inventory.get(item, 0)
    if quantity > current: 
      raise EquipmentError(f"Not enough {item} to remove. You currently have {current} of {item}, {quantity} requested.")
    new_quantity = current - quantity 
    if new_quantity < 1:
      del self.inventory[item]
    else:
      self.inventory[item] = new_quantity
   
  def equip(self, slot: str, item: Item):
    return equip_item(self, slot, item)
    
  