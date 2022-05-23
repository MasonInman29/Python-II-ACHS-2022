#Mason Inman
#Python II Spring 2022
#4/4/22
#
#Dictionary Summative
#I did not cheat this is my own work.
def printUniqueVals(dict):
  uniqueVals = []
  for key in dict:
    count = 0
    for element in dict:
      if dict[key] == dict[element]:
        count += 1
    if count == 1:
      uniqueVals.append(dict[key])
  
  print("Unique Values:")
  for value in uniqueVals:
    print (value)
    
def main():
  dictionary = {'V': 'S001' , 'VI': 'S001', 'VII' : 'S005', 'VIII':'S009', 'IX' : 'S007'}
  printUniqueVals(dictionary)
  
main()