import logging
from pathlib import Path


log = logging.getLogger(__name__)


#GET LANGUAGE 

def _get_language_from_file() -> str:
  """
  Read the language preference from file.
  Defaults to 'en'
  """
  config_file = Path(__file__).resolve().parents[2] / "config" / "language.cfg"

  try:
    if config_file.is_file():  # safer than exists()
      lang = config_file.read_text(encoding="utf-8").strip()

      if lang in ("en", "fr"):
        return lang

  except OSError as e:  # catch only file system errors
    log.error("Failed to read language preference: %s", e)
  return "en"

  
def _get_language_from_db():
  pass
  

#SET LANGUAGE 

def _set_language_to_file(language: str | None = None) -> str:
  """
  Save the selected language to a config file.
  Defaults to 'en'
  """
  #redesigned. Older version on github

  from pathlib import Path

  if language not in ("en", "fr"):
    return "en"

  config_file = Path(__file__).resolve().parents[2] / "config" / "language.cfg"
  try:
    config_file.parent.mkdir(parents=True, exist_ok=True)
    config_file.write_text(language, encoding="utf-8")
    return language
  except OSError as e:
    log.error("Failed to save language preference: %s", e)
    return "en"

def _set_language_to_db():
  pass
  