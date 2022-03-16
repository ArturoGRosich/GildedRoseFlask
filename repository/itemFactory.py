from domain.itemClasses import itemClasses
from domain.types import *

class ItemFactory():
    def CreateItem(ItemDict):
        Item = [ItemDict["name"], ItemDict["sell_in"], ItemDict["quality"]]
        Name = Item[0]
        try:
            Class = itemClasses[Name]
        except KeyError:
            print("NormalItem")
            Class = itemClasses["Normal Item"]
        finally:
            return eval(Class + str(tuple(Item)))
