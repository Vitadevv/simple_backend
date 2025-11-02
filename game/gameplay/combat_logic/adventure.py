from ..entities.entities import Entity 


def take_turn(player: Entity, enemy: Entity):
"""Executes only 1 turn. Useful for debugging and may be a useful helper function"""
  if enemy.hp > 0:
  
def fight_to_death(player: Entity, enemy: Entity) -> dict:
  turns = 0
  log = []
  while player.hp > 0 and enemy.hp > 0:
    take_turn(player, enemy)
    log.extend(f"Player: )
  
    turns += 1