from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    f = open(fname,'r').read().split('\n')
    print f
    i=0
    while i < len(f):
        if f[i] == "line":
            args=f[i+1].split(" ")
            for j in range(6):
                args[j]=int(args[j])
           
            add_edge(points,args[0],args[1],args[2],args[3],args[4],args[5])
            i+=1
        elif f[i] == "ident":
            ident(transform)
        elif f[i] == "scale":
            args=f[i+1].split(" ")
            for j in range(3):
                args[j]=float(args[j])
            scale=make_scale(args[0],args[1],args[2])
          
            transform=matrix_mult(scale,transform)
            i+=1
            print_matrix(transform)
        elif f[i] == "transform":
            args=f[i+1].split(" ")
            for j in range(3):
                args[j]=float(args[j])
            translate=make_translate(args[0],args[1],args[2])
          
            transform=matrix_mult(translate,transform)
            i+=1
            print_matrix(transform)
        elif f[i] == "xrotate":
            transform=matrix_mult(make_rotX(float(f[i+1])), transform)
            i+=1
        elif f[i] == "yrotate":
            transform=matrix_mult(make_rotY(float(f[i+1])), transform)
            i+=1
        elif f[i] == "zrotate":
            transform=matrix_mult(make_rotZ(float(f[i+1])), transform)
           
            i+=1
        elif f[i] == "circle":
            pts=f[i+1].split(" ")
            add_circle(points,float(pts[0]),float(pts[1]),0,float(pts[2]),.001)
        elif f[i] == "hermite":
            coefs=f[i+1].split(" ")
            add_curve(points,
                      float(coefs[0]),float(coefs[1]),float(coefs[4]),float(coefs[5]),
                      float(coefs[2]),float(coefs[3]),float(coefs[6]),float(coefs[7]),
                      .001,"hermite")
        elif f[i] == "bezier":
            coefs=f[i+1].split(" ")
            add_curve(points,
                      float(coefs[0]),float(coefs[1]),float(coefs[2]),float(coefs[3]),
                      float(coefs[4]),float(coefs[5]),float(coefs[6]),float(coefs[7]),
                      .001,"bezier")
        elif f[i] == "apply":
            points=matrix_mult(transform,points)
          
        elif f[i] == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif f[i] == "save":
            save_extension(screen,f[i+1])
       
        i+=1
    pass

