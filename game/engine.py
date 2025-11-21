import logging
from random import random, choice
from gameplay.entities.player import Player
from builder import create_3_paths, check_milestone, create_event
from config.loader import load_config, get_current_language


log = logging.getLogger(__name__)


def game_loop(player: Player, language: str = None):
  """
  This module links all pieces to create a game loop.
  accepts player and their language.
  Works for both web and terminal 
  """
  if language is None:
    language = get_current_language()
  
  log.info(f"{player.name}'s {game_loop.__name__} is initialized")

  player.start_timer()
  
  while player.is_alive():
    log.info(f"{player.name} is currently at {player.floor}. HP: {player.hp}")
    
    paths = create_3_paths(player.floor, language)
    
    # TODO: Display paths and get player choice (menu will do this)
    
    path_number = 0     #up to 3
    path_choice = paths[path_number]
    
    res = create_event(player, path_choice, language)
    log.info(f"{player.name} executed {res}")
    
    player.pass_floor()
    check_milestone(player, language)
    
  player.end_timer()
  log.info(f"player {player.name} died at {player.floor}")