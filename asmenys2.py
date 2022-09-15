import logging

logging.basicConfig(filename='asmenys.log', encoding="UTF-8",
                    level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class Asmuo:

    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        logging.info(f"Sukurtas darbuotojas: {self.vardas} {self.pavarde}")

tadas = Asmuo("Tomas", "Kucinskas")
rokas = Asmuo("Rokas", "Radzevicius")