# from enum import Enum

# class Hand(bytes, Enum):
#     def __new__(cls, value, name):
#         obj = bytes.__new__(cls, [value])
#         obj._value = value
#         obj.name = name
#         return obj
        
#     def lower_name(self):
#         return self.name.lower()
#     def lower_name_remove_space(self):
#         return self.name.lower().replace(" ", "")
    
#     BAMBOO = (1,'Bamboo')
#     FIREWORK = (2,'Firework')
#     GAMEPAD = (3,'Game Pad')
#     ICEDCOFFEE = (4,'Iced Coffee')
#     LEMONADE = (5,'Lemonade')
#     PIZZA = (6,'Pizza')
#     SALMON = (7,'Salmon')
#     SODA = (8,'Soda')
#     WATCH = (9,'Watch')
    
    
from enum import Enum

class Skill(Enum):
    HTML = ("HTML", "Hypertext Markup Language")
    CSS = ("CSS", "Cascading Style Sheets")
    JS = ("JS", "JavaScript")

    def __init__(self, title, description):
        self.title = title
        self.description = description

    @classmethod
    def get_most_popular(cls):
        return cls.JS

    def lower_title(self):
        return self.title.lower()
    
    
    
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