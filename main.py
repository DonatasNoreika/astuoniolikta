import logging
import asmenys

# logging.basicConfig(filename="main.log",
#                     level=logging.DEBUG, encoding="UTF-8",
#                     format="%(asctime)s %(levelname)s %(message)s")

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler(filename="main.log", encoding="UTF-8")
formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logger.setLevel(level=logging.DEBUG)

def dalyba(a, b):
    rezultatas = a / b
    logging.info(f"Paleista funkcija {dalyba.__name__}, sudėti skaičiai {a} ir {b}, rezultatas = {rezultatas}")
    return rezultatas

padalinom = dalyba(10, 5)
