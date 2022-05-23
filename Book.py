#this is not really needed to make the PhoneBook work, but I added it for the sake of the project and trying to get an advanced grade
class Book:
  def __init__(self, title = '', author = ''):
    self.title = title
    self.author = author
  def __str__(self):
    return self.title + ', by ' + self.author 