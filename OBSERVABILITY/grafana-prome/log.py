import logging
import logging.handlers
import random
import time
import sys

# Create logger
logger = logging.getLogger("SampleAppLogger")
logger.setLevel(logging.DEBUG)

# Create handler (console handler here)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter(
    '%(asctime)s %(name)s: %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

handler.setFormatter(formatter)
logger.addHandler(handler)

messages = [
    "User login successful",
    "User logout",
    "Database connection established",
    "Database query executed",
    "API request processed",
    "File uploaded successfully",
    "Permission denied for resource",
    "Service restarted",
    "Cache cleared",
    "Background job completed"
]

levels = [
    logging.INFO,
    logging.WARNING,
    logging.ERROR,
    logging.DEBUG
]

def random_log():
    level = random.choice(levels)
    msg = random.choice(messages)
    logger.log(level, msg)

try:
    while True:
        random_log()
        time.sleep(random.uniform(0.2, 1.5))
except KeyboardInterrupt:
    print("\nStopped")

