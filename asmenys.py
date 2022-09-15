import logging

# logging.basicConfig(filename='asmenys.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler(filename="asmenys.log", encoding="UTF-8")
formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.setLevel(level=logging.DEBUG)

class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        logger.info(f"Asmuo {self.vardas} {self.pavarde} buvo sukurtas")

tadas = Asmuo("Tomas", "Kucinskas")
rokas = Asmuo("Rokas", "Radzevicius")