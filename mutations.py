import numpy as np
def mutation(p):
    i = np.random.randint(len(p))
    p[i]=1-p[i]
    return p
