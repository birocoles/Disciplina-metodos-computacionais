import numpy as np
import scipy as sp
from scipy.linalg import dft
from numpy.testing import assert_almost_equal as aae
import pytest
import QR_algorithms as qra

# Householder Vector
def test_House_vector_parameter_beta():
    'verify that beta = 2/dot(v,v)'
    np.random.seed(23)
    a = np.random.rand(7)
    v, beta = qra.House_vector(x=a)
    aae(beta, 2/np.dot(v,v), decimal=10)

def test_House_vector_orthogonal_reflection():
    'verify that the resulting Householder reflection is orthogonal'
    np.random.seed(14)
    # real vector
    a = np.random.rand(7)
    v, beta = qra.House_vector(x=a)
    P = np.identity(a.size) - beta*np.outer(v,v)
    aae(np.dot(P.T,P), np.dot(P,P.T), decimal=10)
    aae(np.dot(P.T,P), np.identity(a.size), decimal=10)


def test_House_vector_reflection_property():
    'verify that Px = norm_2(x) u_0'
    np.random.seed(43)
    # real vector
    x = np.random.rand(7)
    v, beta = qra.House_vector(x=x)
    # compute the Householder reflection
    P = np.identity(x.size) - beta*np.outer(v,v)

    x_norm_2 = np.linalg.norm(x)
    u_0 = np.zeros_like(x)
    u_0[0] = 1

    aae(np.dot(P,x), x_norm_2*u_0, decimal=10)


def test_House_vector_matvec_matmat_reflection():
    'verify matrix-matrix product with Householder reflections'
    np.random.seed(32)
    # real vector
    N = 7
    a = np.random.rand(N)
    v, beta = qra.House_vector(x=a)
    P = np.identity(a.size) - beta*np.outer(v,v)
    A = np.random.rand(N,N)
    PA1 = np.dot(P, A)
    PA2 = qra.House_matvec(A=A, v=v, beta=beta, order='PA')
    aae(PA1, PA2, decimal=10)
    AP1 = np.dot(A, P)
    AP2 = qra.House_matvec(A=A, v=v, beta=beta, order='AP')
    aae(AP1, AP2, decimal=10)


# Givens rotations
def test_Givens_rotation_definition():
    'verify if Givens rotation satisfies its definition'
    np.random.rand(3)
    # general a and b
    a = 10*np.random.rand()
    b = 10*np.random.rand()
    c, s = qra.Givens_rotation(a=a, b=b)
    G = np.array([[ c, s],
                  [-s, c]])
    v = np.array([a, b])
    Gv = np.dot(G.T, v)
    aae(Gv[1], 0, decimal=10)
    # b = 0
    a = 10*np.random.rand()
    b = 0
    c, s = qra.Givens_rotation(a=a, b=b)
    G = np.array([[ c, s],
                  [-s, c]])
    v = np.array([a, b])
    Gv = np.dot(G.T, v)
    aae(Gv[1], 0, decimal=10)
    # |b| > |a|
    a = 7*np.random.rand()
    b = 10*np.random.rand()
    c, s = qra.Givens_rotation(a=a, b=b)
    G = np.array([[ c, s],
                  [-s, c]])
    v = np.array([a, b])
    Gv = np.dot(G.T, v)
    aae(Gv[1], 0, decimal=10)


def test_Givens_matvec_matmat():
    'verify matrix-matrix product with Givens rotations'
    np.random.seed(3)
    M = 5
    N = 7
    A = np.round(np.random.rand(M,N), decimals=3)
    i = 2
    k = 3
    c, s = qra.Givens_rotation(a=A[i,3], b=A[k,3])
    # verify product GTA
    G = np.identity(M)
    G[i,i] = c
    G[i,k] = s
    G[k,i] = -s
    G[k,k] = c
    A2 = A.copy()
    qra.Givens_matvec(A=A2, c=c, s=s, i=i, k=k, order='GTA')
    aae(A2, np.dot(G.T,A), decimal=10)
    # verify AG
    G = np.identity(N)
    G[i,i] = c
    G[i,k] = s
    G[k,i] = -s
    G[k,k] = c
    A2 = A.copy()
    qra.Givens_matvec(A=A2, c=c, s=s, i=i, k=k, order='AG')
    aae(A2, np.dot(A,G), decimal=10)


def test_Givens_cs2rho_Givens_rho2cs():
    'verify consistency'
    np.random.seed(11)
    a = 10*np.random.rand()
    b = 10*np.random.rand()
    c, s = qra.Givens_rotation(a=a, b=b)
    rho = qra.Givens_cs2rho(c=c, s=s)
    c2, s2 = qra.Givens_rho2cs(rho=rho)
    aae(c, c2, decimal=10)
    aae(s, s2, decimal=10)


# QR factorization
def test_QR_House_Q_from_QR_House_decomposition():
    'verify the computed Q and R matrices'
    np.random.seed(7)
    M = 6
    N = 5
    A = np.random.rand(M,N)
    A2 = A.copy()
    qra.QR_House(A2)
    Q = qra.Q_from_QR_House(A=A2)
    R = np.triu(A2)
    aae(A, np.dot(Q, R), decimal=10)


def test_QR_House_Q_from_QR_House_orthogonal():
    'verify the orthogonality of the computed Q'
    np.random.seed(78)
    M = 6
    N = 5
    A = np.random.rand(M,N)
    qra.QR_House(A)
    Q = qra.Q_from_QR_House(A=A)
    aae(np.identity(M), np.dot(Q.T,Q), decimal=10)


def test_QR_House_Cholesky():
    'verify that R is the transpose of the Cholesky factor of ATA'
    np.random.seed(8)
    M = 6
    N = 5
    A = np.random.rand(M,N)
    ATA = np.dot(A.T,A)
    qra.QR_House(A)
    R = np.triu(A)
    aae(ATA, np.dot(R.T,R), decimal=10)


def test_QR_Givens_Q_from_QR_Givens_decomposition():
    'verify the computed Q and R matrices'
    np.random.seed(7)
    M = 6
    N = 5
    A = np.random.rand(M,N)
    A2 = A.copy()
    qra.QR_Givens(A2)
    Q = qra.Q_from_QR_Givens(A=A2)
    R = np.triu(A2)
    aae(A, np.dot(Q, R), decimal=10)


def test_QR_Givens_Q_from_QR_Givens_orthogonal():
    'verify the orthogonality of the computed Q'
    np.random.seed(78)
    M = 6
    N = 5
    A = np.random.rand(M,N)
    qra.QR_Givens(A)
    Q = qra.Q_from_QR_Givens(A=A)
    aae(np.identity(M), np.dot(Q.T,Q), decimal=10)


def test_QR_Givens_Cholesky():
    'verify that R is the transpose of the Cholesky factor of ATA'
    np.random.seed(8)
    M = 6
    N = 5
    A = np.random.rand(M,N)
    ATA = np.dot(A.T,A)
    qra.QR_Givens(A)
    R = np.triu(A)
    aae(ATA, np.dot(R.T,R), decimal=10)


def test_QR_MGS_decomposition():
    'verify the computed Q and R matrices'
    np.random.seed(6)
    M = 6
    N = 5
    A = np.random.rand(M,N)
    Q1, R1 = qra.QR_MGS(A)
    aae(A, np.dot(Q1, R1), decimal=10)


def test_QR_MGS_Q_orthogonal():
    'verify the orthogonality of the computed Q'
    np.random.seed(1)
    M = 6
    N = 5
    A = np.random.rand(M,N)
    Q1, R1 = qra.QR_MGS(A)
    aae(np.identity(N), np.dot(Q1.T,Q1), decimal=10)


def test_QR_MCS_Cholesky():
    'verify that R is the transpose of the Cholesky factor of ATA'
    np.random.seed(98)
    M = 6
    N = 5
    A = np.random.rand(M,N)
    ATA = np.dot(A.T,A)
    Q1, R1 = qra.QR_MGS(A)
    aae(ATA, np.dot(R1.T,R1), decimal=10)
