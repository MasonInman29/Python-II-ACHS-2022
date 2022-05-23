from Chacacter import *

class RPG(Character):
  def __init__(self, name, type, benchMax, role):
    super().__init__(name, type, benchMax)
    self.role = role
    
  def __str__(self):
    return (self.type + ' ' + self.role + ' ' + self.name)