from display import *
from matrix import *
import math
import numpy as np


def add_circle( points, cx, cy, cz, r, step ):
    
    x0=r+cx
    y0=cy
    x1=0
    y1=0
    for t in np.arange(0,1.001,step):
        x1=r*math.cos(2*math.pi*t)+cx
        y1=r*math.sin(2*math.pi*t)+cy
        
        add_edge(points,x0,y0,0,x1,y1,0)
        x0=x1
        y0=y1
    pass

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    xi=x0
    yi=y0
    xf=0
    yf=0
    if curve_type == "hermite":
        x_coef=generate_curve_coefs(x0,x2,x1,x3,"hermite")
        y_coef=generate_curve_coefs(y0,y2,y1,y3,"hermite")
        for t in np.arange(0,1.001,step):
            xf = x_coef[0][0]*t**3 + x_coef[1][0]*t**2 + x_coef[2][0]*t + x_coef[3][0]
            yf = y_coef[0][0]*t**3 + y_coef[1][0]*t**2 + y_coef[2][0]*t + y_coef[3][0]
            add_edge(points, xi, yi, 0, xf, yf, 0);
            xi=xf
            yi=yf

    elif curve_type == "bezier":
        x_coef=generate_curve_coefs(x0,x1,x2,x3,"bezier")
        y_coef=generate_curve_coefs(y0,y1,y2,y3,"bezier")
        for t in np.arange(0,1.001,step):
            xf = x_coef[0][0]*t**3 + x_coef[1][0]*t**2 + x_coef[2][0]*t + x_coef[3][0]
            yf = y_coef[0][0]*t**3 + y_coef[1][0]*t**2 + y_coef[2][0]*t + y_coef[3][0]
            add_edge(points, xi, yi, 0, xf, yf, 0);
            xi=xf
            yi=yf
    
    return "Please input a type"
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

