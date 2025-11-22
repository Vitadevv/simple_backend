from __future__ import annotations
from random import choice, choices, randint
import logging


log = logging.getLogger(__name__)


def create_player(name: str, language = None) -> Player: # type: ignore
  """
  IMPORTANT: language selection actually happens when a player is initialized.
  - Language CAN be passed manually or by loading with get_current_language() 
  """

  from game.gameplay.entities.player import Player
  from game.config.loader import load_config, get_current_language

  #if it's not passed as argument 
  if language is None:
    language = get_current_language()
    log.info(f'{name} has been created with {language} language used from previous session')
    
  #getting it from loader.py  
  else:
    log.info(f'{name} has been created with {language} language')
    
  try:
    config = load_config(language)
  except (ValueError, TypeError, FileNotFoundError):
    log.error(f"invalid language configuration: {language} received")
    raise
  
  #load_config returns a dictionary. Here, the "game"
  #chunk is needed for general settings (e.g., stats)
  game_settings = config["game"]
    
    #player is created here using config params
  player = Player(
    name = name,
    hp = game_settings["starting_hp"],
    attack = game_settings["starting_attack"],
    speed = game_settings["starting_speed"]
  )
      
  log.info(f'{name} has been initialized with:\n{player.hp} health;\n{player.attack} attack;\n{player.speed} speed')
    
  return player


def create_3_paths(floor: int, language: str = None) -> list[dict]:
  """
  Generates 3 paths for player to choose from (config["game"] has it all).
  Returns a list WITH DICTIONARIES 
  """

  from game.gameplay.entities.player import Player
  from game.config.loader import load_config, get_current_language

  if language is None:
    language = get_current_language()
    
  config = load_config(language)
  paths = []
  
  #picking from a re-defined list to avoid complexity 
  for risk in ["high_risk", "medium_risk", "low_risk"]:
    hints = config["paths"][risk]["hints"]
    #hints.keys() because internally yaml is converted into python object of type dictionary 
    hint_id = choice(list(hints.keys()))
    hint_text = hints[hint_id]["text"]
        
    paths.append({
    "risk": risk,
    "hint_id": hint_id,
    "hint_text": hint_text
    })
  
  log.info(f"paths generared for floor {floor}: {paths}")
  return paths
  
  
def check_milestone(player: Player, language: str = None): # type: ignore
  from game.gameplay.entities.player import Player
  from game.config.loader import load_config, get_current_language
  #stop immediately if floor isn't dividable by 10 
  if player.floor % 10 != 0:
    return
 
  if language is None:
    language = get_current_language()
  
  config = load_config(language)
  coins = config["milestone_coins"]["base_rewards"]
  randomness = config["milestone_coins"]["variance"]

  #previous check guarantees it's a milestone 
  
  base_amount = coins[player.floor]
  variance_amount = int(randomness*base_amount)
  finalized_amount = randint(
  (base_amount-variance_amount),
  (base_amount+variance_amount)
  )

  player.coins += finalized_amount
  log.info(f"{player.name} just received {finalized_amount} coins")


def create_event(player: Player, chosen_path: dict, language: str = None): # type: ignore
  """
  Handles all events for both environments and keeps the facade simple and approachable. Events need to be added here if new are implemented 
  IMPORTANT: create_3_paths() has to be called SEPARATELY 
  """

  from game.gameplay.entities.player import Player
  from game.config.loader import load_config, get_current_language

  from game.gameplay.events.events import (
  floor_down_event, poison_event, summon_enemy_event, heal_event, random_item_event, floor_up_event, add_coins_event
  )
  
  if language is None:
    language = get_current_language()
    
  #extracting event probabilities  
  config = load_config(language)
  risk = chosen_path["risk"]
  probabilities = config["paths"][risk]["base_probabilities"]
  
  #finalized_event line allows weights
  events = list(probabilities.keys())
  chances = list(probabilities.values())
  finalized_event = choices(events, weights=chances, k=1)[0]
      
  if finalized_event == "enemy":
    return summon_enemy_event(player)
  elif finalized_event == "poison":
    return poison_event(player)
  elif finalized_event == "floor_down":
    return floor_down_event(player)
  elif finalized_event == "heal":
    return heal_event(player)
  elif finalized_event == "item":
    return random_item_event(player)
  elif finalized_event == "coins":
    return add_coins_event(player)
  elif finalized_event == "floor_up":    #low-risk only
    return floor_up_event(player)