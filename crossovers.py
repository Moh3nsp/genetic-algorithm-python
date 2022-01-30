import numpy as np

def singlepointcrossover(p1,p2):
    nvar=len(p1)
    valid_section=np.random.randint(nvar-1)
    c1= list(p1[:valid_section]) +  list(p2[valid_section+1:])
    c2= list(p2[:valid_section]) + list( p1[valid_section+1:])
    return c1,c2