import pygame as g
import random

window_width = 1280
window_height = 720

TITLE = """  MATRIX  """

FPS = 10
LETTER_H = 24
LETTER_W = 24

START = window_width//2//LETTER_W - len(TITLE)//2
START_Y = window_height//2//LETTER_H
CHANCE = 1000
NOISE_CHANCE = 100


g.init()

BLACK = (0, 0, 0)
GREEN = (0,255,0)

screen = g.display.set_mode((window_width, window_height))


clock = g.time.Clock()

font = g.font.SysFont('Consolas',22)

y = 0
green_lightness = 255


matrix = [[{'char':chr(random.randint(50,1000)), 'light': (random.randint(1,2)if yy == 0 else 0)} for xx in range(window_width//LETTER_W)] for yy in range(window_height//LETTER_H) ]
#print(matrix[1][5]['char'])
running = True
start = [ i for i in range(len(matrix[0]))]
lettersCnt=0
while running:
        # События
        for event in g.event.get():
                if event.type == g.QUIT:
                        running = False

        # Расчёты
        lettersCnt+=1
        for x in range(len(matrix[0])):
             minus = random.randint(7,11)
             offset = random.randint(1,20)
             for y in range(len(matrix)-1,0,-1):
                
                matrix[y][x]['light'] -= minus
                
                # matrix[y][x]['char'] = chr(random.randint(50,1000))
                if matrix[y][x]['light'] < 0: 
                    matrix[y][x]['light'] = 0
                
                if y>=1 and matrix[y][x]['light']+offset < matrix[y-1][x]['light'] and random.randint(1,100)>30: 
                    # if y>=offset and matrix[y][x]['light'] < matrix[y-offset][x]['light'] and random.randint(1,100)>85: 
                    matrix[y][x]['light'] = 255
                    matrix[y][x]['char'] = chr(random.randint(50,1000))
                
                    if random.randint(1,CHANCE)>1:
                        if x>=START and x<=min(START+len(TITLE),window_width) and y==START_Y:
                            matrix[y][x]['char'] = TITLE[(abs(START-x) % (len(TITLE)))]
                if random.randint(1,NOISE_CHANCE)==1:
                     matrix[y][x]['char'] = chr(random.randint(50,1000))
                if y==1 and x==1:
                    if lettersCnt == FPS*4:
                        matrix[0] = [{'char':chr(random.randint(50,1000)), 'light': random.randint(1,10)} for xx in range(window_width//LETTER_W)]
                        print('!')
                        break
                    if lettersCnt == FPS*6:
                        matrix[0] = [{'char':chr(random.randint(50,1000)), 'light': random.randint(1,25)} for xx in range(window_width//LETTER_W)]
                        print('!')
                        break

                     
                    
                    
                
                #screen.fill(BLACK)        
                text = font.render(matrix[y][x]['char'], True, (0,matrix[y][x]['light'],0), BLACK)
                textRect = text.get_rect()
                textRect.center = (x*LETTER_W, y*LETTER_H)
                screen.blit(text,textRect) 
        # Вывод на экран
        
        

        clock.tick(FPS)
        g.display.flip()