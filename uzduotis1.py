from math import sqrt
import logging

# logging.basicConfig(filename='uzduotis1.log', encoding='UTF-8',
#                     level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('uzduotis1.log', encoding="UTF-8")
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def suma(*skaiciai):
    res = sum(skaiciai)
    logger.info(f'Funkcija {suma.__name__} įvykdyta, skaičių {skaiciai} suma lygi {res}')
    return res


def saknis(skaicius):
    try:
        res = sqrt(skaicius)
        logger.info(f'Funkcija {saknis.__name__} įvykdyta, skaičiaus {skaicius} šaknis lygi {res}')
        return res
    except TypeError:
        logger.exception(f'Funkcija {saknis.__name__} neįvykdyta, paduotas ne skaičius')


def simboliu_kiekis(sakinys):
    res = len(sakinys)
    logger.info(f'Funkcija {simboliu_kiekis.__name__} įvykdyta, sakinio {sakinys} ilgis lygus {res}')
    return res


def dalyba(x, y):
    try:
        res = x / y
        logger.info(f'Funkcija {dalyba.__name__} įvykdyta, {x} / {y} = {res}')
        return res
    except ZeroDivisionError:
        logger.exception(f'Funkcija {dalyba.__name__} neįvykdyta, dalyba iš nulio negalima')


suma(8, 6, 4, 6)
saknis(5)
simboliu_kiekis("Donatas Noreika")
print(dalyba(20, 0))
