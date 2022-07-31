from enum import Enum


class URL_SUFFIX(Enum):
    POLITIC = "/politika/"
    WORLD = "/dunya/"
    ECONOMY = "/ekonomi/"
    MAGAZINE = "/magazin/"
    LOCAL = "/ankara/" # TODO burayı herhangi bi şehire çevirebiliyon sen seç istersen argüman alarak gönder
    TECH = "/teknoloji/"


class NewsCategories(Enum):
    POLITIC = "POLITIC"
    WORLD = "WORLD"
    ECONOMY = "ECONOMY"
    MAGAZINE = "MAGAZINE"
    LOCAL = "LOCAL"
    TECH = "TECH"
