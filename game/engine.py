from __future__ import annotations
from random import random, choice
import logging


log = logging.getLogger(__name__)


def game_loop(player: Player, language: str = None):  # type: ignore
  """
  Brain of the game.

  "risk": risk,
  "hint_id": hint_id,     #(mist, blood_stains, ...)
  "hint_text": hint_text  -> what is displayed in this func

  Check builder.py (create_3_paths) for better comprehension
  """

  from game.config.loader import load_config, get_current_language, get_game_loop
  from game.builder import create_3_paths, check_milestone, create_event
  from game.gameplay.entities.player import Player
  from game.menu.menu_terminal import slow_print

  if language is None:
    language = get_current_language()

  log.info(f"{player.name}'s {game_loop.__name__} initialized")

  config = load_config(language)
  cfg_gl = get_game_loop(language)

  #Start timer for this run
  player.start_timer()

  #Main loop starts
  while player.is_alive():
    floor_now = cfg_gl["floor_now"].format(player.floor)
    hp_coins_now = cfg_gl["hp_coins_now"].format(player.hp, player.coins)
    slow_print(floor_now)
    slow_print(hp_coins_now)

    #THIS IS A LIST WITH DICT!!!§
    paths_generated: list[dict] = create_3_paths(player.floor, language)

    slow_print(cfg_gl["choose_your_path"])

    #path is the key in config ("high_risk", "low_risk", ...)
    risk_levels = {

      "fr": {
      "high_risk": "Risque fort",
      "medium_risk": "Risque moyen",
      "low_risk": "Risque faible"
      },

      "en": {
      "high_risk": "High risk",
      "medium_risk": "Medium risk",
      "low_risk": "Low risk"
      }

    }

    for i, path in enumerate(paths_generated, 1):  #index moved

      #[x] - Risk: message
      risk = risk_levels[language][path["risk"]]
      text = path["hint_text"]
      _message = cfg_gl["choose_your_path_message"].format(
        i, risk, text
      )
      
      slow_print(_message)
 
    #USER INPUT
    while True:
      try:
        choice = input(cfg_gl["enter_your_choice"])
        path_index = int(choice) - 1  #convert to index

        if path_index in (0, 1, 2):  #if input is valid
          break 
        else:
          slow_print(cfg_gl["invalid_enter_number"])  #invalid
      except (ValueError, TypeError):
        slow_print(cfg_gl["invalid_input"])

    #safe assignment
    path_choice = paths[path_index]

    #PROCESSING
    

    # ---------------------------
    # CHECK DEATH
    # ---------------------------
    if not player.is_alive():
      slow_print("\nGAME OVER")
      slow_print(f"You reached floor {player.floor}")
      break

    # Progression
    player.pass_floor()
    check_milestone(player, language)

  # End timer
  player.end_timer()
  log.info(f"player {player.name} died at {player.floor}")

  slow_print("\nPress Enter to return to the main menu...")
  input()
