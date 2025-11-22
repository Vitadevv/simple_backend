import logging
import time

from game.menu.menu_terminal import menu

#debug might be added later on
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s UTC | %(levelname)s | %(name)s | %(message)s"
)

logging.Formatter.converter = time.gmtime

menu()