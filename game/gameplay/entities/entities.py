from random import uniform 
import logging 

log = logging.getLogger(__name__)

class Entity:
  def __init__(self, name: str, hp = 100, attack = 10, speed = 10):
    self.name = name
    self.hp = hp
    self.attack = attack 
    self.speed = speed
    
  def is_alive(self) -> bool:
    return self.hp > 0
  
  def take_damage(self, damage: float) -> None:
    self.hp = max(0, (self.hp - damage))
    
  def attack_target(self, target: "Entity") -> dict:
    if not isinstance(target, Entity):
      log.error(f"{self.name} tried to attack {target}")
      raise TypeError("This is not an entity that you try to attack")
      
    multiplier = uniform(0.6, 1.5)
    crit = multiplier >= 1.2
    dmg = min(round(self.attack*multiplier, 2), 50) #50 attack is max
    target.take_damage(dmg)
    crit_txt = " (CRIT DMG)" if crit else ""
    log.info(
    f"{self.name} attacked {target.name} and dealt {dmg} damage{crit_txt}. Target now has {target.hp} HP"
    )
    #this will be used with fastapi
    return {
    "attacker": self.name,
    "target": target.name,
    "damage": dmg,
    "crit": crit,
    "target_hp": target.hp
    } 
    
    
class Enemy(Entity):
  def __init__(self, name: str):
    super().__init__(name = name, hp = 80, attack = 15, speed = 15)
    
    
    