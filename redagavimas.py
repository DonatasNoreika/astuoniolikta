import logging

logging.basicConfig(filename="aritmetika.log", encoding="UTF-8", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def dalyba(a, b):
    rezultatas = a / b
    logging.info(f"Paleista funkcija {dalyba.__name__}, sudėti skaičiai {a} ir {b}, rezultatas = {rezultatas}")
    return rezultatas

dalyba(10, 5)

# INFO:root:Paleista funkcija dalyba, sudėti skaičiai 10 ir 5, rezultatas = 2.0

