[TOC]

# 安装
pip install pygame

# hello world
```python
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)  
# 最后这两个参数的作用是？
pygame.display.set_caption('Hello World')
# 设置窗口标题
while True:
	event in pygame.event.get():
		if event.type == QUIT:
			exit()
	screen.blit()
	x, y = pygame.mouse.get_pos()
	x -= mouse_cursor.get_wit





```