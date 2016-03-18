from display import *
from matrix import *
import math

def param_cx(r, deg,step):
    return r*cos(step*2*deg*pi/180)

def param_cy(r, deg,step):
    return r*sin(step*2*deg*pi/180)

def add_circle( points, cx, cy, cz, r, step ):
    
    for i in range(0,1,step):
        x=param_cx(r,deg,i)
        y=param_cy(r,deg,i)
        
        add_point(points,x,y,0)
    pass

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    pmat=[
        [x0,x1,x2,x3],
        [y0,y1,y2,y3],
        [z0,z1,z2,z3],
        [1,1,1,1]

    ]
    if curve_type == "hermite":
        
    pass

def draw_lines( matrix, screen, color ):
    
    
    for i in range(0,len(matrix[0])-1,2):
        x0=matrix[0][i]
        y0=matrix[1][i]
        x1=matrix[0][i+1]
        y1=matrix[1][i+1]
        draw_line(screen,x0,y0,x1,y1,color)
    pass

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)
    pass

def add_point( matrix, x, y, z=0 ):
    matrix[0].append(x)
    matrix[1].append(y)
    matrix[2].append(z)
    matrix[3].append(1)
    pass


def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    
    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

