import pygame,sys
import random
import math
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((800,600))
background = pygame.image.load('background.png')
mixer.music.load('background.wav')
mixer.music.play(-1)
pygame.display.update()
#tittle
pygame.display.set_caption("space invadors")
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change=0

EnemyImg =[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enimies = 6
for i in range(num_of_enimies):
    EnemyImg.append(pygame.image.load('Enemy.png'))
    enemyX.append(random.randint(0,750))
    enemyY.append(random.randint(40,70))
    enemyX_change.append( 0.3)
    enemyY_change.append( 40)


BulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change= 0
bulletY_change= 10
bullet_state="ready"

score_value=0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY =10
def show_score(x,y):
    score = font.render("score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def player(x,y):
    pygame.display.update()
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    pygame.display.update()
    screen.blit(EnemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(BulletImg,(x+16,y+10))
def red(x,y):
    pygame.display.update()
    screen.blit(red)
    #print(x,y)
    #pygame.quit()
def inCollision(enemyX,enemyY,bulletX,bulletY):
    distance= math.sqrt(math.pow(enemyX-bulletX,2)+ (math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    else:
        return False
running=True

while running:
    #playerX += 0.1
    screen.blit(playerImg,(playerX,playerY))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #print("left arrow is pressed")
                playerX_change -=0.8
            if event.key == pygame.K_RIGHT:
                #print("RIGHT arrow is pressed")
                playerX_change +=0.8
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX_change,bulletY)
                #print("space arrow is pressed")
                #print(playerX,bulletY)
                
    playerX += playerX_change    
    if playerX <=0:
        playerX = 0
        
        
        
    elif playerX >=700:
        playerX = 700
    for i in range(num_of_enimies):
        enemyX[i] += enemyX_change[i]
        
        if enemyX[i] <=0:
            enemyX_change[i] =4
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i] >=800:
            enemyX_change[i] =-4
            enemyY[i]+=enemyY_change[i]
        collision = inCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound=mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state="ready"
            score_value+=1
            enemyX[i] = random.randint(0,750)
            enemyY[i] = random.randint(0,50)
        enemy(enemyX[i],enemyY[i],i) 
       
    if bulletY<=0:
        bulletY = 480
        bulletX = playerX
        bullet_state = "ready"
        

    
    if bullet_state is"fire":
        fire_bullet( bulletX,bulletY)
        bulletY -= bulletY_change
    
    
    player(playerX,playerY)
    
    screen.blit(background,(0,0))
    show_score(textX,textY)
    pygame.display.update()

pygame.display.update()

            

    
