from Character import *
#from RPG import *

def main():
  c = Character('Ted','Archer', 315)
  mason = Character()

  print(c) 
  print(mason) #prints nothing because name and type are both ''
  
  print('Comparing:', (c == mason))
  mason.name = 'Mason'
  mason.type = 'Warhammer Connoisseur'
  mason.benchMax = 200

  print('The story of', mason,'\n---------------')
  print('\n',mason, 'went to the gym and got a pr of', mason.benchMax)

  mason.goToGym()
  print('\n',mason, 'went to the gym again and benched', mason.benchMax)
  
  mason.restDay()
  print('\n','uh oh its a rest day', mason, 'feels his bench decreasing to', mason.benchMax)

  mason.midLifeCrisis()
  print('\n',mason, 'had a mid life crisis: bench max:', mason.benchMax)

  print('---------------')

  #rpg = RPG('Bran', 'Small', 'Honker', 405)
  #print(rpg)
  
main()