from Book import *
class PhoneBook(Book):

  #creates a phone book object
  def __init__(self, edition = 0, dict = {'Pizza Hut': 5159641174}):
    #calls Book __init__, the author is left to the default value     of nothing ('')
    super().__init__("Phone Book " + str(edition) + " edition")
    self.edition = edition
    self.people = dict

  #makes a phone book from an already created book
  def __init__(self, book, edition, dict):
    self.title = book.title
    self.author = book.author
    self.edition = edition
    self.people = dict
    
  #returns string visualization of a phone book
  def __str__(self):
    return self.title + ' with ' + str(len(self.people)) + ' entries.'

  #if 2 phone books have the same edition and same entries; return       true. Otherwise returns false
  def __eq__(self, other):
    if self.edition == other.edition and self.people == other.people:
      return True
    return False

  #returns true if the name is in the phone books dictionary,         otherwise returns false
  def __contains__(self, name):
    if (name in self.people):
      return True
    return False

  #returns phone number correlated with a entry of a phone book
  def findNumber(self, name):
    for key in self.people:
      if key == name:
        return self.people[key]
  
  #adds a person/business name and number to the phone book and       increments the edition     
  def addEntry(self, name, number):
    self.people[name] = number
    self.edition += 1 #any change should result in new edition

  #changes the number of a person/business that was already in the     phone book and increments edition
  def updateNumber(self, name, number):
    self.people[name] = number
    self.edition += 1 #new edition
  
  