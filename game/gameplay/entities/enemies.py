from .entities import Entity
from random import randint
from typing import Optional

class Enemy(Entity):
  def __init__(self, name: str, hp: int | float, attack: int | float, speed: int | float, loot: Optional[int] = None):
    super().__init__(name = name, hp = hp, attack = attack, speed = speed)
    #this line works as intended
    self.loot: int = loot if loot is not None else 0
    
    
  def reinforce_enemy(enemy: Enemy, floor: int, language: str = None) -> Enemy:
  """
  scales difficulty of enemies as floors progress.
  Language defaults to the one that's saved in a file, if file doesn't exist - another module handles it
  """

  if language is None:
    language = get_current_language()
    
  config = load_config(language)
  
  #fallback value
  multiplier = 1.0
  
  for tier in config["difficulty"]["enemy_stat_scaling"]["tiers"]:
    if floor <= tier["floor"]:
      #updating multiplier
      multiplier = tier["multiplier"]
      break
    
  reinforced_enemy = Enemy(
  name = enemy.name,
  hp = int(enemy.hp * multiplier),
  attack = int(enemy.attack * multiplier),
  speed = int(enemy.speed * multiplier),
  loot = enemy.loot
  )
  
  log.info(f"enemy with scaled stats has been created with following stats:\nname: {reinforced_enemy.name};\nhp: {reinforced_enemy.hp};\nattack: {reinforced_enemy.attack};\nspeed: {reinforced_enemy.speed};\nloot: {reinforced_enemy.loot}")
    
  return reinforced_enemy  