from domain.itemClasses import itemClasses
from domain.types import *

class ItemFactory():
    def CreateItem(Item):
        Name = Item[0]
        try:
            Class = itemClasses[Name]
        except KeyError:
            Class = itemClasses["Normal Item"]
        finally:
            return eval(Class + str(tuple(Item)))
