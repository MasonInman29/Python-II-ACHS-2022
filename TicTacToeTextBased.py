#Mason Inman
#Python 2 Spring 22
#Design Your Own Class Project
#
#This is my own work. I did not cheat.
from PhoneBook import *

def main():
  #using __str__ and __init__
  pb = PhoneBook(2022)
  pb2 = PhoneBook(2022)
  pb3 = PhoneBook(2022, {'Pizza Hut': 5159641174, 'Ankeny Schools' : 5159641174, 'White House':2024561111, 'Example':1112223333})
  print(pb)
  print(pb2, '\n')

  #testing .updateNumber
  pb2.updateNumber('Pizza Hut', 5150001111)
  print('Phonebook updated.')
  print(pb2)

  #testing .findNumer
  print('\nWhats Pizza Huts number you ask?')
  print('Pizza Huts number is', str(pb.findNumber('Pizza Hut')))

  #testing __eq__
  print('\nCurrent Phone Books')
  print('1: ', pb)
  print('2: ',pb2)
  print('3: ',pb3)
  print('\nComparison Results:')
  print('(1 and 2) same name and dict different edition:', pb == pb2)
  
  pb3Again = PhoneBook(2022, {'Pizza Hut': 5159641174, 'Ankeny Schools' : 5159641174, 'White House':2024561111, 'Example':1112223333})
  print ('(3 and pb same as 3) same dict and edition:', pb3 == pb3Again)
  pb2.edition = 2021 #will be incremented with .addEntry to 2022
  pb2.people = pb.people
  pb2.addEntry('Comparison test', 2223334444)
  print('*2 has been updated to:', pb2)
  print('1 and 2 are identical but 2 has an extra entry, they should not be the same.\n Are they the same?', pb == pb2)


  #tests __contains__ method
  print('\nIs pizza hut in the phone book?', 'Pizza Hut' in pb)

  #super class testing
  print('\nBook Class:')
  book = Book('Python 101', 'Python Tutor')
  print(book)
main()
