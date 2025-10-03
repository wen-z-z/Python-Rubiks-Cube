from termcolor import colored

#takes in 3 faces, which are lists of size 9
#where 0 index is the center of the face and
#1-8 index are the other colors counter clockwise from the
#displayed center corner
cube = '''
⠀⠀⠀⠀⠀⠀⠀⠀ ⣤⣶⣿⣶⣶⡤ ⢀⣀⣀⣀           
⠀⠀⠀⠀ ⠤⢶⣿⣿⣶⠤⠉⣀⣤⣀⠉⠛⠿⠿⠛⠉⣤⣶⣶⣦⡤⠄ 
⠀⠤⣶⣿⣿⡶⠖ ⣀⣤⣀⠉⠙⠛⠿⠛⠉⠤⢶⣶⣶⡤⠄⠉⠁⣤⣶⣿
⣤⣤⣀⣀⠁  ⠛⠛⠿⠿⠟⠋⣤⣶⣶⣦⡤⠄⠉⠁⣤⣶⣿ ⣿⣿⣿
⣿⣿⣿⣿⣿ ⣿⣶⣶⣦⡄⢠⣤⣀⣀⠉⠁⣀⣤⣶ ⣿⣿⣿ ⣿⡿⠋
⠿⠿⣿⣿⣿ ⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿ ⣿⣿⣿ ⣿⣿⡿ ⢀⣠⣶
⣤⣤⣀⣀⠉ ⠛⠛⠿⠿⡇⢸⣿⣿⣿⣿ ⣿⣿⣿⠀⠟⠋⣀ ⣿⣿⣿
⣿⣿⣿⣿⣿ ⣶⣶⣤⣤⡀⢀⠉⠉⠛⠛ ⠋⠉⣀⠀⣶⣿⣿ ⣿⣿⠟
⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⡇⢸⣿⣿⣶⣶⠀⣾⣿⣿ ⣿⣿⡿ ⠋⣠⣴
⣀⠉⠉⠛⠛ ⠿⣿⣿⣿⡇⢸⣿⣿⣿⣿⠀⣿⣿⣿ ⠟⠋⣀ ⣿⣿⣿
⣿⣿⣿⣶⣶ ⣤⣀⣀⠉⠁⠘⠛⠿⠿⣿ ⡿⠟⠉ ⣶⣿⣿ ⣿⣿⠟
⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⡇⢰⣶⣤⣤⣀ ⣤⣾⣿ ⣿⣿⡿ ⠋⠁ 
⠛⠿⠿⣿⣿ ⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⠀⣿⣿⣿ ⡿⠛⠁   

      ⠉⠛⠿⠿⡇⢸⣿⣿⣿⣿⠀⣿⡿⠟        
⠀⠀⠀⠀⠀⠀      ⠉⠉⠛⠛⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''

cube_unformatted = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣤⣶⣶⣶⣶⡤⢀⣀⣀⣀
⠀⠀⠀⠀⠀⢤⣶⣿⣿⣿⡿⠏⣉⣥⣘⣛⡿⠿⠿⠟⣣⣴⣶⣶⣦⣤⡄
⠀⣤⣶⣿⣿⣷⡶⠂⣉⣥⣔⣛⣻⠿⠿⠟⢋⣤⣶⣶⣶⣯⣭⠙⢋⣥⣶⡆
⣶⣶⣤⣬⡉⢁⣘⡛⠛⠿⠿⠟⢋⣥⣶⣿⣶⣾⣯⠝⠛⢉⣤⣶⣾⣿⣿⡇
⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⡆⢠⣤⣬⣍⣉⡛⢉⣤⣾⡇⢸⣿⣿⢸⣿⡿⠃
⢿⣿⣿⣿⡇⢸⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⡇⢸⣿⣿⡇⢸⣿⡿⠈⣁⣤⡄
⣤⣤⣉⣉⠁⠈⠛⠿⠿⢿⠇⢸⣿⣿⣿⣿⡇⢸⣿⡿⠇⠈⣁⣤⢸⣿⣿⡇
⣿⣿⣿⣿⡇⢰⣶⣶⣦⣤⡀⢀⡉⠙⠛⠛⠃⠘⢉⣤⠀⣾⣿⣿⢸⣿⣿⠃
⢿⣿⣿⣿⡇⢸⣿⣿⣿⣿⡇⢸⣿⣿⣿⣶⠀⣾⣿⣿⠀⣿⣿⡿⠘⠋⣠⡀
⣀⣉⠉⠛⠃⠘⠿⣿⣿⣿⡇⢸⣿⣿⣿⣿⠀⣿⣿⣿⠀⠟⢋⡀⢰⣿⣿⠇
⣿⣿⣿⣿⡆⢠⣤⣤⣀⡉⠁⠘⠛⠿⠿⣿⠀⡿⠟⢉⢀⣶⣿⣿⢸⣿⣿
⢿⣿⣿⣿⡇⢸⣿⣿⣿⣿⡄⢴⣶⣤⣤⣀⠀⣤⣾⣿⢸⣿⣿⡿⠸⠛⠁
⠈⠙⠛⠿⠇⢸⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⠀⣿⣿⣿⠸⡿⠛⠁
⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠃⢸⣿⣿⣿⣿⠀⣿⡿⠟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''

def format(*items):
      color_dict = {'r': 'red',
          'o': 'light_red',
          'y': 'light_yellow',
          'g': 'green',
          'b':'blue',
          'w':None,}
      retStr = ''
      for i in range(len(items)//2):
            retStr += colored(items[i], color_dict[items[i+len(items)//2]])
      return retStr

def returnStr(face1, face2, face3, type = 'debug'):

      if type == 'debug':
            retStr = [format(' '*7, 5, ' '*7, 'w', face1[5], 'w'),
             format(' '*4, 4, ' '*5, 6, ' '*4, 'w', face1[4], 'w', face1[6], 'w'),
             format(' ', 3, ' '*5, 0, ' '*5, 7, ' ', 'w', face1[3], 'w', face1[0], 'w', face1[7], 'w'),
             format(7, ' '*3, 2, ' '*5, 8, ' '*3, 3, face2[7], 'w', face1[2], 'w', face1[8], 'w', face3[3]),
             format(' '*3, 8, ' '*3, 1, ' '*3, 2, ' '*3, 'w', face2[8], 'w', face1[1], 'w', face3[2], 'w'),
             format(6, ' '*5, 1, ' ', 1 , ' '*5, 4, face2[6], 'w', face2[1], 'w', face3[1] , 'w', face3[4]),
             format(' '*3, 0, ' '*7, 0, ' '*3, 'w', face2[0], 'w', face3[0], 'w'),
             format(5, ' '*5, 2, ' ', 8, ' '*5, 5, face2[5], 'w', face2[2], 'w', face3[8], 'w', face3[5]),
             format(' '*3, 4, ' '*7, 6, ' '*3, 'w', face2[4], 'w', face3[6], 'w'),
             format(' '*6, 3, ' ', 7, ' '*6, 'w', face2[3], 'w', face3[7], 'w')
            ]

      elif type == 'debug_rev':
            retStr = [format(' '*7, 5, ' '*7, 'w', face1[5], 'w'),
             format(' '*4, 6, ' '*5, 4, ' '*4, 'w', face1[6], 'w', face1[4], 'w'),
             format(' ', 7, ' '*5, 0, ' '*5, 3, ' ', 'w', face1[7], 'w', face1[0], 'w', face1[3], 'w'),
             format(3, ' '*3, 8, ' '*5, 2, ' '*3, 7, face2[3], 'w', face1[8], 'w', face1[2], 'w', face3[7]),
             format(' '*3, 2, ' '*3, 1, ' '*3, 8, ' '*3, 'w', face2[2], 'w', face1[1], 'w', face3[8], 'w'),
             format(4, ' '*5, 1, ' ', 1 , ' '*5, 6, face2[4], 'w', face2[1], 'w', face3[1] , 'w', face3[6]),
             format(' '*3, 0, ' '*7, 0, ' '*3, 'w', face2[0], 'w', face3[0], 'w'),
             format(5, ' '*5, 8, ' ', 2, ' '*5, 5, face2[5], 'w', face2[8], 'w', face3[2], 'w', face3[5]),
             format(' '*3, 6, ' '*7, 4, ' '*3, 'w', face2[6], 'w', face3[4], 'w'),
             format(' '*6, 7, ' ', 3, ' '*6, 'w', face2[7], 'w', face3[3], 'w')
            ]
      elif type == 'detail':
            retStr = [format(' '*9, '⣤⣶⣿⣶⣶⡤ ', '⢀⣀⣀⣀', ' '*8, 'w', face1[5], face1[6], 'w'),
                format(' '*5, '⠤⢶⣿⣿⣶⠤', '⠉', '⣀⣤⣀', '⠉⠛⠿⠿⠛⠉', '⣤⣶⣶⣦⡤⠄ ', 'w', face1[4], face1[5], face1[0], face1[6], face1[7]),
                format(' ⠤⣶⣿⣿⣶⠖ ', '⣀⣤⣀', '⠉⠙⠛⠿⠛⠉', '⠤⢶⣶⣶⡤⠄', '⠉⠁', '⣤⣶⣿', face1[3], face1[2], face1[0], face1[8],face1[7], face3[3]),
                format('⣤⣤⣀⣀', '⠁  ', '⠛⠛⠿⠿⠟⠃', '⣤⣶⣶⣦⡤⠄', '⠉⠁', '⣤⣶⣿ ', '⣿⣿⣿', face2[7], face1[3], face1[2], face1[1],  face1[8], face3[2], face3[3]),
                format('⣿⣿⣿⣿⣿ ', '⣿⣶⣶⣦⡄', '⢠⣤⣀⣀', '⠉⠁', '⣀⣤⣶ ', '⣿⣿⣿ ', '⣿⡿⠋', face2[7], face2[8], face2[1], face1[1], face3[1], face3[2], face3[3]),
                format('⠿⠿⣿⣿⣿ ', '⣿⣿⣿⣿⡇', '⢸⣿⣿⣿⣿ ', '⣿⣿⣿ ', '⣿⣿⡿ ', '⢀⣠⣶', face2[7], face2[8], face2[1], face3[1], face3[2], face3[4]),
                format('⣤⣤⣀⣀', '⠉ ', '⠛⠛⠿⠿⡇', '⢸⣿⣿⣿⣿ ', '⣿⣿⣿⠀', '⠟⠋', '⣀ ', '⣿⣿⣿', face2[6], face2[7], face2[8], face2[1], face3[1], face3[2], face3[0], face3[4]),
                format('⣿⣿⣿⣿⣿ ', '⣶⣶⣤⣤⡀', '⢀', '⠉⠉⠛⠛ ', '⠋⠉' ,'⣀ ', '⣶⣿⣿ ', '⣿⣿⠟', face2[6], face2[0], face2[2], face2[1], face3[1], face3[8], face3[0], face3[4]),
                format('⣿⣿⣿⣿⣿ ', '⣿⣿⣿⣿⡇', '⢸⣿⣿⣶⣶⠀', '⣾⣿⣿ ', '⣿⣿⡿ ', '⠋', '⣠⣴', face2[6], face2[0], face2[2], face3[8], face3[0], face3[4], face3[5]),
                format('⣀', '⠉⠉⠛⠛ ', '⠿⣿⣿⣿⡇', '⢸⣿⣿⣿⣿⠀', '⣿⣿⣿ ', '⠟⠋', '⣀ ', '⣿⣿⣿', face2[5], face2[6], face2[0], face2[2], face3[8], face3[0], face3[6], face3[5]),
                format('⣿⣿⣿⣶⣶ ', '⣤⣀⣀', '⠉⠁', '⠘⠛⠿⠿⣿ ', '⡿⠟⠉ ', '⣶⣿⣿ ', '⣿⣿⠟', face2[5], face2[4], face2[0], face2[2], face3[8], face3[6], face3[5]),
                format('⣿⣿⣿⣿⣿ ', '⣿⣿⣿⣿⡇', '⢰⣶⣤⣤⣀ ', '⣤⣾⣿ ', '⣿⣿⡿ ', '⠋⠁ ', face2[5], face2[4], face2[3], face3[7], face3[6], face3[5]),
                format('⠛⠿⠿⣿⣿ ', '⣿⣿⣿⣿⡇', '⢸⣿⣿⣿⣿⠀', '⣿⣿⣿ ', '⡿⠛⠁    ', face2[5], face2[4], face2[3], face3[7], face3[6]),
                format('      ⠉⠛⠿⠿⡇', '⢸⣿⣿⣿⣿⠀', '⣿⡿⠟', ' '*8, face2[4], face2[3], face3[7], 'w'),
                format(' '*13, '⠈⠉⠛⠀', '⠉', ' '*10, 'w', face2[3], face3[7], 'w')
               ]

      elif type == 'detail_rev':
        retStr = [format(8*' ' , '⠉⠉⠉⠁' , ' ⠚⠿⠿⣿⠿⠛' , 9*' ',  'w',  face1[6],  face1[5],  'w'),
                  format(' ⠐⠚⠻⠿⠿⠛' , '⣀⣤⣶⣶⣤⣀' , '⠉⠛⠉' , '⣀' , '⠒⠿⣿⣿⠷⠒' , 5*' ',  face1[7],  face1[6],  face1[0],  face1[5],  face1[4],  'w'),
                  format('⣿⠿⠛' , '⢀⣀' , '⠐⠚⠿⠿⠷⠒' , '⣀⣤⣶⣤⣄⣀' , '⠉⠛⠉' , ' ⠲⠿⣿⣿⠿⠒ ',  face2[3], face1[7],  face1[8],  face1[0],  face1[2],  face1[3]),
                  format('⣿⣿⣿' , ' ⣿⠿⠛' , '⢀⣀' , '⠐⠚⠻⠿⠿⠛' , '⢠⣴⣶⣶⣤⣤' , '  ⢀' , '⠉⠉⠛⠛',  face2[3],  face2[2],   face1[8],  face1[1],  face1[2],  face1[3],  face3[7]),
                  format('⣠⣾⣿' , ' ⣿⣿⣿' , ' ⠿⠛⠉' , '⢀⣀' , '⠉⠉⠛⠃' , '⠘⠻⠿⠿⣿' , ' ⣿⣿⣿⣿⣿',  face2[3],  face2[2],  face2[1],  face1[1],  face3[1],  face3[8],  face3[7]),
                  format('⠿⠋⠁' , ' ⣾⣿⣿' , ' ⣿⣿⣿' , ' ⣿⣿⣿⣿⡇' , '⢸⣿⣿⣿⣿' , ' ⣿⣿⣿⣶⣶',  face2[4],  face2[2],  face2[1],  face3[1],  face3[8],  face3[7]),
                  format('⣿⣿⣿' , ' ⠉' , '⣠⣴' , '⠀⣿⣿⣿' , ' ⣿⣿⣿⣿⡇' , '⢸⣶⣶⣤⣤' , ' ⣀' , '⠉⠉⠛⠛',  face2[4],  face2[0],  face2[2],  face2[1],  face3[1],  face3[8],  face3[7],  face3[6]),
                  format('⣴⣿⣿' , ' ⣿⣿⠿' , ' ⠉',  '⣀⣠' , ' ⣤⣤⣀⣀' , '⠁' , '⠈⠛⠛⠿⠿' , ' ⣿⣿⣿⣿⣿',  face2[4],  face2[0],  face2[8],  face2[1],  face3[1],  face3[2],  face3[0],  face3[6]),
                  format('⠻⠋' , '⣠' , ' ⣾⣿⣿' , ' ⣿⣿⡿' , '⠀⠿⠿⣿⣿⡇' , '⢸⣿⣿⣿⣿' , ' ⣿⣿⣿⣿⣿',  face2[5],  face2[4],  face2[0],  face2[8],  face3[2],  face3[0],  face3[6]),
                  format('⣿⣿⣿' , ' ⠉' , '⣠⣴' , ' ⣿⣿⣿' , '⠀⣿⣿⣿⣿⡇' , '⢸⣿⣿⣿⣶' , ' ⣤⣤⣀⣀' , '⠉',  face2[5],  face2[6],  face2[0],  face2[8],  face3[2],  face3[0],  face3[6],  face3[5]),
                  format('⣴⣿⣿' , ' ⣿⣿⠿', ' ⣀⣴⣾' , ' ⣿⣶⣶⣤⡄' , '⢀⣀' , '⠉⠉⠛' , ' ⠿⠿⣿⣿⣿',  face2[5],  face2[6],  face2[8],  face3[2],  face3[0],  face3[4],  face3[5]),
                  format(' ⢀⣠' , ' ⣾⣿⣿' , ' ⣿⡿⠛' , ' ⠉⠛⠛⠿⠇' , '⢸⣿⣿⣿⣿' , ' ⣿⣿⣿⣿⣿',  face2[5],  face2[6],  face2[7],  face3[3],  face3[4],  face3[5]),
                  format('    ⢀⣤⣾' , ' ⣿⣿⣿' , '⠀⣿⣿⣿⣿⡇' , '⢸⣿⣿⣿⣿' , ' ⣿⣿⣶⣶⣤',  face2[6],  face2[7],  face3[3],  face3[4],  face3[5]),
                  format(8*' ' , '⣴⣾⣿' , '⠀⣿⣿⣿⣿⡇' , '⢸⣶⣶⣤⣀      ', 'w', face2[7],  face3[3], face3[4]),
                  format(10*' ' , '⣀' , '⠀⣤⣀⡀' , 13*' ',  'w',  face2[7],  face3[3],  'w')

         ]


      return retStr
