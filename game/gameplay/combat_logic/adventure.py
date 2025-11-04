from ..entities.entities import Entity 


def take_turn(player: Entity, enemy: Entity) -> dict:
"""Executes only 1 turn. Useful for debugging and may be a useful helper function."""
  report = []
  player_hit = player.attack_target(enemy)
  report.append(player_hit)
  if enemy.is_alive():
    enemy_hit = enemy.attack_target(player)
    report.append(enemy_hit)
  return {
  "player HP": player.hp,
  "enemy HP": enemy.hp,
  "report": report
  
  }
  
def fight_to_death(player: Entity, enemy: Entity) -> dict:
  turns = 0
  report = []
  while player.is_alive() and enemy.is_alive():
    turn = take_turn(player, enemy)
    report.append(turn)
    turns += 1
  winner = player.name if player.is_alive() else enemy.name
  player_remaining_hp = player.hp if player.is_alive() else 0
  return {
  "winner": winner,
  "remaining_hp": player_remaining_hp,
  "turns": turns,
  "report": report
  }
