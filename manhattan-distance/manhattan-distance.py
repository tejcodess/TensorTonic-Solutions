import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x=np.array(x)
    y=np.array(y)
    s=0
    if(len(x)!=len(y)):
        return 0.0
    for i in range(len(x)):
        a=x[i]-y[i]
        if(a<0):
            a=a*-1
        s=s+a
    return float(s)
    pass