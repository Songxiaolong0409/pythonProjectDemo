import logging
import sys
from logging.handlers import TimedRotatingFileHandler

level = logging.DEBUG

log = logging.getLogger(__name__)
log.setLevel(level)

# handler = logging.FileHandler("test.log")
filename = sys.path[2] + "/logs/test.log"
handler = TimedRotatingFileHandler(filename)
handler.suffix = "%Y%m%d"
handler.setLevel(level)

console = logging.StreamHandler()
console.setLevel(level)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)

log.addHandler(handler)
log.addHandler(console)
