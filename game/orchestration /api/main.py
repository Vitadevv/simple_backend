import logging
import time

#debug might be added later on
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s UTC | %(levelname)s | %(name)s | %(message)s"
)

logging.Formatter.converter = time.gmtime