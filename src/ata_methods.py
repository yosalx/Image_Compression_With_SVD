import numpy as np
import math
import qr_decomposition
import numpy as np

def find_v(matrix):
    a = matrix
    at = a.transpose()
    v = np.dot(at,a)
    return v

def find_svd(a):
    def find_ata(a):
        at = a.transpose()
        return np.dot(at,a)
    v = find_ata(a)
    rows = len(a)
    cols = len(a[0])
    
    # pake qr method Gilang
    eval,evec = qr_decomposition.find_eig_qr(v) 
    
    # pake library eigen
    # eval,evec = np.linalg.eig(v)
    
    eigenValues = eval
    eigenVectors = evec
    idx = eigenValues.argsort()[::-1]   
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:,idx]
    
    n = len(eigenValues)
    singular = np.zeros(n)
    for i in range(n):
        if (eigenValues[i] < 1e-16):
            singular[i] = 0
        else:
            singular[i] = math.sqrt(eigenValues[i])
    
    print((-1) * eigenVectors.transpose())
    vT = (-1) * eigenVectors.transpose()
    v = (-1) * eigenVectors

    matrixs = np.zeros((rows,cols))
    for i in range(np.linalg.matrix_rank(a)):
        matrixs[i][i] = math.sqrt(eigenValues[i])

    matu = np.zeros((rows,rows))
    rank = np.linalg.matrix_rank(a)
    for j in range(rank):
        matu[:,j] = (np.matmul(a,vT[j])) / math.sqrt(abs(eigenValues[j]))
    svd = np.dot(matu,np.dot(matrixs,vT))
    return matu,singular,vT