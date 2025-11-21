import logging


log = logging.getLogger(__name__)


#GET LANGUAGE 
def _get_language_from_file():
  from pathlib import Path
  import json
  
  preference_file = Path(__file__).parent / "user_preference.json"
  preferences = {}
  if preference_file.exists():
    try:
      preferences = json.loads(preference_file.read_text(encoding='utf-8'))
      return preferences.get("language", "en")
    except json.JSONDecodeError:
      return "en"
  return "en"
  
  
def _get_language_from_db():
  pass
  

#SET LANGUAGE 
def _set_language_to_file(language: str):
  from pathlib import Path
  import json
  preference_file = Path(__file__).parent / "user_preference.json"
  preferences = {}
  if preference_file.exists():
    try:
      preferences = json.loads(preference_file.read_text(encoding='utf-8'))
    except json.JSONDecodeError:
      log.error(f"couldn't decode preference_file, falling back to None")
      preferences = {}
   
  preferences["language"] = language 
  
  try:
    preference_file.write_text(json.dumps(preferences, indent=2), encoding="utf-8")
    log.info(f"language {language} has been set and written to file")
  except IOError as e:
    log.error(f"Failed to write preference file: {e}")
    raise
  
def _set_language_to_db():
  pass
  