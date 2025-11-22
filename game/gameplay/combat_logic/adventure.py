from game.gameplay.entities.entities import Entity
from random import random


def take_turn(player: Entity, enemy: Entity) -> dict:
  """Executes only 1 turn. Useful for debugging and may be a useful helper function."""
  report = []
  if player.is_alive() and enemy.is_alive():
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
  
  
def flee(player: Entity, enemy: Entity) -> dict:
  if player.speed > enemy.speed:
    player.floor += 1
    return {
    "message": "escaped successfully!",
    "escaped_from": enemy.name
    }
  else:
    delta = (player.speed - enemy.speed)/100 #negative result, might change later
    escape = random()+delta < 0.5
    if escape:
      player.floor += 1
      return {
      "message": "escaped successfully!",
      "escaped_from": enemy.name
      }
    res = fight_to_death(player, enemy)
    return {
    "message": "not escaped!",
    "enemy": enemy.name,
    "report": res
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
  if player.is_alive():
    player.coins += enemy.loot
  return {
  "winner": winner,
  "remaining_hp": player_remaining_hp,
  "turns": turns,
  "report": report
  }
  