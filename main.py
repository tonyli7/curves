from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = new_matrix()
transform = new_matrix()

print_matrix(make_hermite())
print_matrix(make_bezier())

drawing=new_matrix()

print generate_curve_coefs(40,20,10,20,"hermite")

#print_matrix(generate_curve_coefs([40,40,0,1],[50,100,0,1],[60,100,0,1],[100,40,0,1],"hermite"))
parse_file( 'script_curves', edges, transform, screen, color )
display(screen)
