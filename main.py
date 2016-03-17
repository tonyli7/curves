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

print_matrix(generate_curve_coefs([40,40,0,1],[50,100,0,1],[60,100,0,1],[100,40,0,1],"h"))
parse_file( 'script_nocurves', edges, transform, screen, color )
