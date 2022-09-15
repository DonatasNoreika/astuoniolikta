from math import sqrt
import logging

logging.basicConfig(filename='uzduotis1.log', encoding='UTF-8',
                    level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')


def suma(*skaiciai):
    res = sum(skaiciai)
    logging.info(f'Funkcija {suma.__name__} įvykdyta, skaičių {skaiciai} suma lygi {res}')
    return res


def saknis(skaicius):
    try:
        res = sqrt(skaicius)
        logging.info(f'Funkcija {saknis.__name__} įvykdyta, skaičiaus {skaicius} šaknis lygi {res}')
        return res
    except TypeError:
        logging.exception(f'Funkcija {saknis.__name__} neįvykdyta, paduotas ne skaičius')


def simboliu_kiekis(sakinys):
    res = len(sakinys)
    logging.info(f'Funkcija {simboliu_kiekis.__name__} įvykdyta, sakinio {sakinys} ilgis lygus {res}')
    return res


def dalyba(x, y):
    try:
        res = x / y
        logging.info(f'Funkcija {dalyba.__name__} įvykdyta, {x} / {y} = {res}')
        return res
    except ZeroDivisionError:
        logging.exception(f'Funkcija {dalyba.__name__} neįvykdyta, dalyba iš nulio negalima')


suma(8, 6, 4, 6)
saknis(5)
simboliu_kiekis("Donatas Noreika")
print(dalyba(20, 0))
