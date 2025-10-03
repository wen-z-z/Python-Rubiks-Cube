from termcolor import colored
import cubeFormat as cube_format

class Cube:
  COLORS = ['w', 'g', 'r', 'y', 'o', 'b']
  COLOR_STR_DICT = {
  'w':'white',
  'g': 'green',
  'r': 'red',
  'y': 'light_yellow',
  'o': 'light_red',
  'b':'blue'}
  ORDERED_MOVES = ['u','f','r','d','l','b']
  modes = ['debug', 'compact', 'detail']

  def __init__(self, size, mode = 'debug'):
    self.stickers = [[x]*9 for x in Cube.COLORS]
    self.size = size
    self.curr_mode = mode

  def turn(self, move, counterclockwise_rotations=1):
    '''0
    0 1:3|0 3:5|0 5:7|0 7:9
    1 -2:1|4 3:6|5 5:8|'''
    def swap_spots(*strs):
      index = 0
      place_holder = self.stickers[strs[index][0]][strs[index][2]]
      for _ in range(1,len(strs)):
        index += 1
        self.stickers[strs[index-1][0]][strs[index-1][2]] = self.stickers[strs[index][0]][strs[index][2]]
      index += 1
      self.stickers[strs[index][0]][strs[index][2]] = place_holder



    adjacent_sides = {
      'u': [2,5,4,1], #123, 567, 345, 781
      'f': [0,4,3,2],
      'r': [1,3,5,0],
      'd': [5,2,1,4],
      'l': [3,1,0,5],
      'b': [4,0,2,3]}

    sides = [self.stickers[x] for x in adjacent_sides[move]]
    rotations = (counterclockwise_rotations+4)%4

    #repeat for number of times the cube turns
    for _ in range(rotations):
      #swap the face
      f = self.stickers[Cube.ORDERED_MOVES.index(move)]
      c, e = f[7], f[8]

      for i in range(3):
        f[8-i*2] = f[8-i*2-2]
        f[7-i*2] = f[7-i*2-2]

      f[1], f[2] = c, e

      #swap the sides
      s = sides[3][-2:]
      s.append(sides[3][1])
      sides[3][-2:], sides[3][1]  = sides[0][1:3], sides[0][3]
      sides[0][1:4] = sides[1][5:8] 
      sides[1][5:8] = sides[2][3:6]
      sides[2][3:6] = s

  def __str__(self):

    str = 'Front:' + ' '*24 + '| Back:'
    frontFace = cube_format.returnStr(self.stickers[0], self.stickers[1], 
       self.stickers[2], self.curr_mode)
    backFace = cube_format.returnStr(self.stickers[3], self.stickers[5], 
       self.stickers[4], self.curr_mode+'_rev')

    backFace.reverse()
    for i in range(len(frontFace)):
      str += '\n' + frontFace[i] + '  |  ' + backFace[i]
    return str



  def reset(self):
    self.stickers = [[x]*9 for x in Cube.COLORS]
