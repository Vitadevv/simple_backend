from builder import create_player
from engine.engine import game_loop
from config.loader import get_current_language, set_language, load_config, get_menu
import logging


log = logging.getLogger(__name__)

#REF
#menu:
 # title: "Dungeon Master"
#  buttons:
   # guide: "[0] - GUIDE"
  #  start_game: "[1] - START GAME"
   # stats: "[2] - STATISTICS"
   # settings: "[3] - SETTINGS"
    #exit: "[4] - EXIT"
  
  #end_game: "GAME OVER"
  #new_record: "NEW RECORD!"

def wrap_equal(func):
  def wrapper(*args, **kwargs):
    print(f'\n{"="*40}')
    res = func(*args, **kwargs)
    print(f'{"="*40}\n')
    return res
  return wrapper
  
def wrap_hyphen(func): 
  def wrapper(*args, **kwargs):
    print(f'\n{"-"*40}')
    res = func(*args, **kwargs)
    print(f'{"-"*40}\n')
    return res
  return wrapper
  
def wrap_mountain(func):
  def wrapper(*args, **kwargs):
    print(f'{"/\\"*40}')

    
@wrap_equal
  def title():
    print(config_menu["title"])  
@wrap_hyphen    
  def guide():
    print(config_menu["buttons"]["guide"])  
@wrap_hyphen    
  def start_game():
    print(config_menu["buttons"]["start_game"])      
@wrap_hyphen    
  def stats():
    print(config_menu["buttons"]["stats"])   
@wrap_hyphen    
  def settings():
    print(config_menu["buttons"]["settings"])      
@wrap_hyphen    
  def exit():
    print(config_menu["buttons"]["guide"])         
          
                
  
  
  
def menu():
  while True:
    language = get_current_language()
    config_menu = get_menu(language)