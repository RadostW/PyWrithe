import numpy as np

def writhe(curve):
    '''
    Returns writhe of given closed parametric curve.

    Parameters
    ----------
    curve: np.array
        An ``N`` by 3 array describing locations of endpoints of ``N`` linear segments approximating the curve. All locations should be distinct.

    Returns
    -------
    float
        Value of writhe for closed curve comprised of linear segments given.

    Example
    -------
    >>> import numpy as np
    >>> curve = np.array([[-1,0,-1],[1,0,1],[0,-1,1],[0,1,1]])
    >>> pywrithe.pywrithe.writhe(curve)
    1.1 #TODO GET ACTUAL VALUE

    '''
    segments = np.transpose(np.array([np.roll(curve,1),curve]),(1,0,2)) # (segment,begin/end,coordinate) order
    r13 = segments[:,np.newaxis,0,:]-segments[np.newaxis,:,0,:] # (i,j,coordinate) order
    return r13
