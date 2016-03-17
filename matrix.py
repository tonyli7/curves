import math


def make_bezier():
    b_mat = [
        [-1,3,-3,1],
        [3,-6,3,0],
        [-3,3,0,0],
        [1,0,0,0]
    ]
    return b_mat


def make_hermite():
    h_mat = [
        [-1,3,-3,1],
        [3,-6,3,0],
        [-3,3,0,0],
        [1,0,0,0]
    ]
    return h_mat

def generate_curve_coefs( p1, p2, p3, p4, t ):
    temp_mat=new_matrix()
    for i in range(4):
        temp_mat[i][0]=p1[i]
        temp_mat[i][1]=p2[i]
        temp_mat[i][2]=p3[i]
        temp_mat[i][3]=p4[i]
        
    print_matrix(temp_mat)
    if t == "h":
        return matrix_mult(make_hermite(),temp_mat)
    pass
    
def make_translate( x, y, z ):
    trans_mat=[
        [1,0,0,x],
        [0,1,0,y],
        [0,0,1,z],
        [0,0,0,1]
    ]
    return trans_mat
    pass

def make_scale( x, y, z ):
    scale_mat=[
        [x,0,0,0],
        [0,y,0,0],
        [0,0,z,0],
        [0,0,0,1]
    ]
    return scale_mat
    pass
    
def make_rotX( theta ):
    phi=theta*math.pi/180
    rotX_mat=[
        [1,0,0,0],
        [0,math.cos(phi),-math.sin(phi),0],
        [0,math.sin(phi),math.cos(phi),0],
        [0,0,0,1]
    ]
    return rotX_mat
    pass

def make_rotY( theta ):
    phi=theta*math.pi/180
    rotY_mat=[
        [math.cos(phi),0,-math.sin(phi),0],
        [0,1,0,0],
        [math.sin(phi),math.cos(phi),1,0],
        [0,0,0,1]
    ]
    return rotY_mat
    pass

def make_rotZ( theta ):
    phi=theta*math.pi/180
    rotZ_mat=[
        [math.cos(phi),-math.sin(phi),0,0],
        [math.sin(phi),math.cos(phi),0,0],
        [0,0,1,0],
        [0,0,0,1]
    ]
    return rotZ_mat
    pass

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    for i in matrix:
        print i
    pass

def ident( matrix ):
    if not len(matrix)==len(matrix[0]):
        print "Not a square"
        return -1
    ctr=0
    for i in matrix:
        j=0
        while j<len(matrix):
            i[j]=0
            i[ctr]=1
            j+=1
        ctr+=1
            
    pass

def scalar_mult( matrix, x ):
    for i in range(len(matrix)):
        for j in range (len(matrix[0])):
            matrix[i][j]*=x
    return matrix
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if not len(m1[0]) == len(m2):
        print "Error: length of matrix-1: %d does not match height of matrix-2:%d\n"%(len(m1[0]),len(m2))
        return -1
    new=new_matrix(len(m2[0]),len(m1))
    ctr=0
   
    for i in range(len(m1)):#loops rows
        t=0
        while t < len(m2[0]):#number of times it loops
            for j in range(len(m2)):#loops row elements in m1 and col in m2
                new[ctr][t]+=m1[i][j]*m2[j][t]
                #print str(m1[i][j])+" * "+str(m2[j][t]) , ctr, t
            t+=1
        ctr+=1
    return new
    pass

