from enum import Enum
  
class Hand(bytes, Enum):
    def __new__(cls, value, label):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.label = label
        return obj
    
    def lower_name(self):
        return self.label.lower()
    def lower_name_remove_space(self):
        return self.label.lower().replace(" ", "")
    
    BAMBOO = (1,'Bamboo')
    FIREWORK = (2,'Firework')
    GAMEPAD = (3,'Game Pad')
    ICEDCOFFEE = (4,'Iced Coffee')
    LEMONADE = (5,'Lemonade')
    PIZZA = (6,'Pizza')
    SALMON = (7,'Salmon')
    SODA = (8,'Soda')
    WATCH = (9,'Watch')
    
class Hat(bytes, Enum):
    def __new__(cls, value, label):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.label = label
        return obj
    
    def lower_name(self):
        return self.label.lower()
    def lower_name_remove_space(self):
        return self.label.lower().replace(" ", "")
    
    BASEBALLCAP = (1,'Baseball Cap')
    COWBOY = (2,'Cowboy')
    FEDORA = (3,'Fedora')
    KING = (4,'King')
    MOHICAN = (5,'Mohican')
    MORTARBOARD = (6,'Mortar Board')
    PIRATE = (7,'Pirate')
    RAINBOWAFRO = (8,'Rainbow Afro')
    RUDOLPH = (9,'Rudolph')
    SANTA = (10,'Santa')
    SKIBEANIE = (11,'Ski Beanie')
    STRAW = (12,'Straw')
    USHANKA = (13,'Ushanka')
    VIKING = (14,'Viking')
    
class Mouth(bytes, Enum):
    def __new__(cls, value, label):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.label = label
        return obj
    
    def lower_name(self):
        return self.label.lower()
    def lower_name_remove_space(self):
        return self.label.lower().replace(" ", "")
    
    BEARD = (1,'Beard')
    BLEP = (2,'Blep')
    BUBBLEGUM = (3,'Bubble Gum')
    CUBANCIGAR = (4,'Cuban Cigar')
    PIPE = (5,'Pipe')
    WATCHVIRUS = (6,'Watch Virus')
    
class Eye(bytes, Enum):
    def __new__(cls, value, label):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.label = label
        return obj
    
    def lower_name(self):
        return self.label.lower()
    def lower_name_remove_space(self):
        return self.label.lower().replace(" ", "")
    
    THREED = (1,'3d')
    DEALWITHIT = (2,'Deal With It')
    HARRYPOTTER = (3,'Harry Potter')
    JOKER = (4,'Joker')
    MONOGLASSES = (5,'Monoglasses')
    PATCH = (6,'Patch')
    SHUTTERSHADES = (7,'Shutter Shades')
    SKIGOGGLE = (8,'Ski Goggle')
    
class Bear(bytes, Enum):
    def __new__(cls, value, label):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.label = label
        return obj
    
    def lower_name(self):
        return self.label.lower()
    def lower_name_remove_space(self):
        return self.label.lower().replace(" ", "")
    
    POLAR = (0,'Polar')
    GRIZZLY = (1,'Grizzly')
    PANDA = (2,'Panda')
    
class Bg(bytes, Enum):
    def __new__(cls, value, label):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.label = label
        return obj
    
    def lower_name(self):
        return self.label.lower()
    def lower_name_remove_space(self):
        return self.label.lower().replace(" ", "")
    
    ARCTICNIGHT = (0,'Arctic Night')
    CHRISTMAS = (1,'Christmas')
    DOWNUNDER = (2,'Down Under')
    JUNIPER = (3,'Juniper')
    MINERALGREEN = (4,'Mineral Green')
    MONOGRAY = (5,'Mono Gray')
    NEWYEAR = (6,'New Year')