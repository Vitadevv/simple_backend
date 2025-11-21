from time import time
from typing import Any

_stats = dict[str, tuple[float, Any]] = {} #id, unix time
default_alive_time = 120   #2 minutes is enough for now

#TODO 
