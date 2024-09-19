import pygame as py
import sys
import time as t

bg_color1 = (255,255,255)
bg_color2 = (60,60,60)

py.init()
angle=1
a=0
a=str(a)

screen_image = py.display.set_mode((150,150))
screen_rect = screen_image.get_rect()
py.display.set_caption("cookies")

cookies_image = py.image.load("Game\Cookies\image\cookies.bmp")
cookies_rect = py.Rect(0,0,100,100)
cookies_rect.center = screen_rect.center

txt_font = py.font.SysFont(None,48)
txt_image = txt_font.render(a,True,bg_color2,bg_color1)
txt_rect = txt_image.get_rect()
txt_rect.x = 20
txt_rect.y = 20

screen_image.fill(bg_color1)
screen_image.blit(cookies_image,cookies_rect)
screen_image.blit(txt_image,txt_rect)
py.display.flip()

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()
        elif event.type == py.MOUSEBUTTONDOWN:
            mouse = py.mouse.get_pressed()
            if mouse == (True, False, False):
                a=int(a)
                a+=1
                a=str(a)
    new_cookies_image = py.transform.rotate(cookies_image, angle)
    angle += 1
    screen_image.blit(new_cookies_image,cookies_rect)
    txt_image = txt_font.render(a,True,bg_color2,bg_color1)
    screen_image.blit(txt_image,txt_rect)
    py.display.update()
    t.sleep(0.01)
    