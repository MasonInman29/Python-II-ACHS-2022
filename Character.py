class Character:
  
  def __init__(self, name = '', type = '', benchMax = 0):
    self.name = name
    self.type = type
    self.benchMax = benchMax
    
  def __str__(self):
    return (str(self.type) + ' ' + str(self.name))
    
  def __eq__(self, other):
    return self.type == other.type
    
  def goToGym(self):
    self.benchMax += 45
    
  def restDay(self):
    self.benchMax -= 25
    
  def midLifeCrisis(self):
    self.benchMax = 0