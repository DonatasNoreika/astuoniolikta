import logging
import asmenys2

logging.basicConfig(filename='aritmetika.log', encoding="UTF-8",
                    level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

def dalyba(a, b):
    rezultatas = a / b
    logging.info(f"Paleista funkcija {dalyba.__name__}, sudėti skaičiai {a} ir {b}, rezultatas = {rezultatas}")
    return rezultatas

dalyba(10, 5)