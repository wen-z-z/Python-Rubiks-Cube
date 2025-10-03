from cube import Cube
from random import randint, seed
import os
import cubeFormat as cube_format

moves = ['u','f','r','d','l','b']
curr_cube = Cube(3, 'detail')
extra_info = ''
shuffle_moves = ''
player_moves = ''

def display_cube_info():
  os.system('cls' if os.name == 'nt' else 'clear')
  print(curr_cube)
  print(extra_info)

def run():
  global extra_info, shuffle_moves, player_moves, curr_cube
  while True:
    display_cube_info()
    userInput = input('Type command: ').lower()
  
  
    if userInput == 'shuffle':
      shuffle_moves = ''
      for _ in range(40):
        curr_move = moves[randint(0,5)]
        turns = randint(1,3)
        shuffle_moves += curr_move * turns
        curr_cube.turn(curr_move, turns)
      extra_info = 'Type \'show shuffle\' to see the shuffle moves'
      continue
    
    if userInput == 'help':
      extra_info = '''Here you can use rubiks cube notation to turn the cube, axis turns are unsupported. 
There are various commands you can use. To see them, type 'commmands'. 
To quit the application use the command 'exit'.'''
      continue

    if userInput == 'commands':
      extra_info = '''shuffle: shuffles the cube
show shuffle: shows the moves that the shuffle command produced
reset: resets the cube to a solved state
show moves: shows the user inputs
exit: quits the application'''
  
    if userInput == 'show shuffle':
      extra_info = shuffle_moves
      continue
  
    if userInput == 'reset':
      curr_cube.reset()
      continue
  
    if userInput == 'show moves':
      extra_info = player_moves
      continue
    
    if userInput == 'exit' or userInput == 'quit':
      break
  
    for i in range(len(userInput)):
      #check that the move in the current index (i) is an actual cube move
      if userInput[i].lower() in moves:
        #check if the next char exists, and if its a prime (')
        if i+1 < len(userInput) and userInput[i+1] == "'":
          curr_cube.turn(userInput[i], 3)
          player_moves += userInput + "'"
        else:
          curr_cube.turn(userInput[i])
          player_moves += userInput
    extraInfo = ''
  
  #rotate_face(board[0], 3)
if __name__ == "__main__":
  run()
