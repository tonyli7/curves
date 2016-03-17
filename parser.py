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
        
        i+=1
    pass

