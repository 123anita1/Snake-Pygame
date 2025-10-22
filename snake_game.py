import pygame
import random
pygame.init()
screen=pygame.display.set_mode((600,600))
def show_text(msg,x,y,color):
        fontobj=pygame.font.SysFont('freesans', 32)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
def snake():
        red=(255,0,0)
        green=(0,255,0)
        blue=(0,0,255)
        pygame.display.set_caption('Snake')
        foodx=(random.randint(0,590)//10)*10
        foody=(random.randint(0,590)//10)*10
        snakex=(random.randint(0,590)//10)*10
        snakey=(random.randint(0,590)//10)*10
        down=0
        up=0
        right=0
        left=0
        score=0
        clock=pygame.time.Clock()
        snakelist=[(snakex,snakey)]
        def show_text(msg,x,y,color):
            fontobj=pygame.font.SysFont('freesans', 32)
            msgobj=fontobj.render(msg,False,color)
            screen.blit(msgobj,(x,y))
        while True:
            screen.fill((0,0,0))
            food=pygame.draw.rect(screen,red,(foodx,foody,10,10))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_DOWN and up==0:
                        down=1; up=0; right=0; left=0
                    elif event.key==pygame.K_UP and down==0:
                        up=1; down=0; right=0; left=0
                    elif event.key==pygame.K_RIGHT and left==0:
                        right=1; down=0; up=0; left=0
                    elif event.key==pygame.K_LEFT and right==0:
                        left=1; down=0; up=0; right=0
            if down==1:
                snakey+=10
            if up==1:
                snakey-=10
            if right==1:
                snakex+=10
            if left==1:
                snakex-=10
            if snakex<0:
                snakex=590
            if snakex>590:
                snakex=0
            if snakey<0:
                snakey=590
            if snakey>590:
                snakey=0
            snakelist.append((snakex,snakey))
            if len(snakelist)>score+1:
                del snakelist[0]
            for segment in snakelist:
                pygame.draw.rect(screen,green,(segment[0],segment[1],10,10))
            snake_rect=pygame.Rect(snakex,snakey,10,10)
            food_rect=pygame.Rect(foodx,foody,10,10)
            if snake_rect.colliderect(food_rect):
                foodx=(random.randint(0,590)//10)*10
                foody=(random.randint(0,590)//10)*10
                score+=1
            show_text('Score: '+str(score),450,0,blue)
            pygame.display.update()
            clock.tick(10)
while True:
    red=(255,0,0)
    blue=(0,0,255)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,red,(50,250,200,100))
    pygame.draw.rect(screen,red,(350,250,200,100))
    show_text('Play', 120,285,blue)
    show_text('Quit', 420,285,blue)
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            if 50<event.pos[0]<250 and 250<event.pos[1]<350:
                print('play')
                screen.fill((0,0,0))
                snake()
            if 350<event.pos[0]<550 and 250<event.pos[1]<350:
                pygame.quit()
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
