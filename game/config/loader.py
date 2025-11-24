import yaml
import logging
from pathlib import Path
from typing import Any


log = logging.getLogger(__name__)


"""
Many of these functions serve no practical purpose - testing only. 

PRODUCTION:
• load_config
• get_game_parameters
• get_current_language
"""


def load_config(language='en') -> dict[str, Any]:
  """
  - Load game configuration from config.yaml
  - FileNotFoundError: If config.yaml doesn't exist
  - yaml.YAMLError: If YAML is malformed
  """
  base_directory = Path(__file__).parent
  config_path = base_directory / language / "config.yaml"

  if not config_path.exists():
    log.error(f"config.yaml not found at {config_path}")
    raise FileNotFoundError(f"Configuration file not found: {config_path}")

  try:
    with open(config_path, 'r', encoding='utf-8') as file:
      config = yaml.safe_load(file)
      log.info(f"Configuration loaded successfully from {config_path}")

      # Must-have keys file SHOULD contain 
      required_keys = ['game', 'paths', 'difficulty', 'milestone_coins']
      missing = [key for key in required_keys if key not in config]
      if missing:
        raise ValueError(f"Missing required config sections: {missing}")

  except yaml.YAMLError as e:
    log.error("Failed to parse config.yaml: %s", e)
    raise

  return config
  
  
def get_current_language(user_id = None) -> str:
  import json
  from game.config.helpers import _get_language_from_file
  from game.config.helpers import _get_language_from_db
  
  """
  Works for terminals AND web (using ID)
  defaults to English automatically 
  """
  
  if user_id is None:
    #terminal
    return _get_language_from_file()
    
  if user_id:
    #web
    try:
      db_get_lang = _get_language_from_db(user_id)
      
    except (ValueError, TypeError):
      log.error(f'database connection couldn\'t be established (invalid user_id: {user_id})')
      raise RuntimeError(f"{db_get_lang} failed: user_id ({user_id}) is invalid")


def set_current_language(language: str = "en", user_id = None) -> str:
  from game.config.helpers import _set_language_to_file
  from game.config.helpers import _set_language_to_db

  if user_id is None:
    #terminal
    _set_language_to_file(language)       #fr or en
    
  if user_id:
    #web
    try:
      _set_language_to_db(language, user_id)
    except (ValueError, TypeError):
      log.error(f'database connection couldn\'t be established (invalid user_id: {user_id})')
      raise RuntimeError(f"setting language failed: user_id ({user_id}) is invalid")


def get_milestone_coins(floor: int) -> int | None:
  """
  Get base coin reward for a milestone floor.

  Args:
    floor: Current floor number

  Returns:
    Randomized coin amount if floor is milestone, None otherwise
  """
  from random import randint

  config = load_config()
  base_rewards = config['milestone_coins']['base_rewards']
  variance = config['milestone_coins']['variance']

  # Check if this floor is a milestone
  if floor not in base_rewards:
    return None

  base = base_rewards[floor]
  variance_amount = int(base * variance)
  return randint(base - variance_amount, base + variance_amount)

def get_menu(language: str = None):
  
  if language is None:
    language = get_current_language()
    
  config = load_config(language)
  return config.get("menu", {})   #fallback


def get_game_loop(language: str = None):

  if language is None:
    language = get_current_language()

  config = load_config(language)
  return config.get("game_loop", {})   #fallback