#!/usr/bin/python3
import sys
import pygame
sys.path.append("../")
sys.path.append(".")
from env_init import *
import numpy as np
from render_support import PygameArtFxns as pafn
from render_support import GeometryFxns as gfn
from render_support import MathFxns
from render_support import TransformFxns as tfn
from support.transform_polygon import *
from support.Polygon import *
from support.polygon_debugging import *

def get_bound_triangles(min_x, min_y, max_x, max_y):
  offt = -40
  return  [[(min_x,min_y),(min_x-offt, max_y/2),(min_x,max_y)],
  [(min_x,max_y), (max_x/2,max_y+offt), (max_x,max_y)],
  [(max_x, max_y), (max_x + offt, max_y/2), (max_x, min_y)],
  [(max_x, min_y), (max_x/2, min_y-offt), (min_x, min_y)]]
  
x=1400
y=1000

pygame.init()
screen = pafn.create_display(x, y)
pafn.clear_frame(screen)
obs = [Polygon(o) for o in get_bound_triangles(0,0,x,y)]
for i,o in enumerate(obs):
  o.color = pafn.colors["white"]
for O in obs:
  sanity_check_polygon(screen, O)
pygame.display.update()
time.sleep(5)