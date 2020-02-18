import pygame
import random
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("My game")
green = (0, 255, 0) 
blue = (0, 0, 128) 
s1=0
s2=0


x,y=(random.randrange(10,480,1),random.randrange(10,480,1))
w,h,vel=40,10,10
w2,h2,vel=40,10,10
x2,y2=(random.randrange(10,480,1),random.randrange(10,480,1))
x1,y1=(random.randrange(10,480,1),random.randrange(10,480,1))
font=pygame.font.SysFont("monospace",15)
run=True
while run:
	pygame.time.delay(100)
	if(s1!=s2 and x>=x2-w and x<=x2+w and y>=y2-h and y<=y2+h):
		run=False
		f=font.render("game over",1,(0,255,0))
		win.blit(f,(40,10))
		
	if(x>=x1-5-w-5 and x<=x1+5+5 and y>=y1-5-h-5 and y<=y1+5+5):
		s1+=1
		x1,y1=(random.randrange(10,480,1),random.randrange(10,480,1))
	
	if(x2>=x1-5-w-5 and x2<=x1+5+5 and y2>=y1-5-h-5 and y2<=y1+5+5):
		s2+=1
		x1,y1=(random.randrange(10,480,1),random.randrange(10,480,1))
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			run=False
	
	keys=pygame.key.get_pressed()
	
	if(keys[pygame.K_LEFT] and x>0):
		x-=vel
	elif(keys[pygame.K_RIGHT] and x<500-w):
		x+=vel
	elif(keys[pygame.K_UP] and y>0):
		y-=vel
	elif(keys[pygame.K_DOWN] and y<500-h):
		y+=vel
		
		
	if(keys[pygame.K_a] and x2>0):
		x2-=vel
	elif(keys[pygame.K_d] and x2<500-w2):
		x2+=vel
	elif(keys[pygame.K_w] and y2>0):
		y2-=vel
	elif(keys[pygame.K_s] and y2<500-h2):
		y2+=vel
		
		
	win.fill((0,0,0))
	f1=font.render("Score: "+str(s1),1,(0,255,0))
	f2=font.render("Score: "+str(s2),1,(255,255,255))
	
	pygame.draw.rect(win,(0,0,250),(x,y,w,h))
	pygame.draw.rect(win,(0,250,250),(x2,y2,w2,h2))
	pygame.draw.circle(win,(250,0,0),(x1,y1),20,5)
	win.blit(f1,(40,10))
	win.blit(f2,(150,10))
	pygame.display.update()
	
run=True
while run:
	
	if(s1>s2):
		f1=font.render("Player 1 wins",1,(0,255,0))
	else:
		f1=font.render("Player 2 wins",1,(0,255,0))
	win.blit(f1,(200,200))	
	pygame.display.update()
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			run=False


pygame.quit()