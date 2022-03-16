class Updateable():
    def updateQuality(self):
        self.reduceSellIn()
        self.changeQuality()

class Item(Updateable):
    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality
    
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sellIn, self.quality)

    def getSelling(self):
        return self.sellIn

    def getQuality(self):
        return self.quality

    def reduceSellIn(self):
        self.sellIn -= 1
    
    def setQuality(self, newQuality):
        if newQuality > 0:
            self.quality = newQuality
        else:
            self.quality = 0
        if newQuality > 50:
            self.quality = 50
    def toJSON(self):
        return {"name":self.name, "sell_in":self.sellIn, "quality":self.quality}

class AgedBrie(Item):
    
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)

    def changeQuality(self):
        qualityModified = 1
        if self.sellIn < 0:
            qualityModified += 1
        self.setQuality(self.getQuality() + qualityModified)
        
class BackStage(Item):
    def __init__(self, name, quality, sellIn):
        super().__init__(name, quality, sellIn)
    
    def changeQuality(self):
        qualityModified = 1
        if self.sellIn < 0:
            qualityModified = -self.getQuality() 
        elif self.sellIn < 5:
            qualityModified = 3
        elif self.sellIn < 10:
            qualityModified = 2
        else:
            pass
        self.setQuality(self.getQuality() + qualityModified)

class Conjured(Item):
    def __init__(self, name, quality, sellIn):
        super().__init__(name, quality, sellIn)
    
    def changeQuality(self):
        qualityModified = -2
        if self.sellIn < 0:
            qualityModified = -4 
        self.setQuality(self.getQuality() + qualityModified)

class NormalItem(Item):

    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)
    
    def changeQuality(self):
        qualityModified = -1
        if self.sellIn < 0:
            qualityModified = -2 
        self.setQuality(self.getQuality() + qualityModified)
    

class Sulfuras(Item):  
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)
        
    def updateQuality(self):
        self.quality = 80
        self.sellIn = 0