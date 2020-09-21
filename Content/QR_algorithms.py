import numpy as np

# Householder transformation
def House_vector(x, check_input=True):
    '''
    Compute the real N x 1 Householder vector (Golub and Van Loan,
    2013, Algorithm 5.1.1, p. 236) v, with v[0] = 1, such that N x N
    matrix P = I - beta outer(v,v) (Householder reflection) is
    orthogonal and Px = norm_2(x) u_0, where u_0 is an N x 1 vector
    with all elements equal to zero, except the 0th, that is equal
    to 1.

    Parameters
    ----------
    x : array 1D
        N x 1 vector perpendicular to the Householder vector.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    v : array 1D
        Householder vector.

    beta : float
        Scalar equal to 1/dot(v,v).
    '''
    x = np.asarray(x)
    if check_input is True:
        assert x.ndim == 1, 'x must be a vector'
        #assert x.size > 1, 'x size must be greater than 1'

    N = x.size
    sigma = np.dot(x[1:], x[1:])
    v = np.hstack([1, x[1:]])

    if (sigma == 0) and (x[0] >= 0):
        beta = 0
    elif (sigma == 0) and (x[0] < 0):
        beta = -2
    else:
        mu = np.sqrt(x[0]**2 + sigma)
        if x[0] <= 0:
            v[0] = x[0] - mu
        else:
            v[0] = -sigma/(x[0] + mu)
        beta = 2*v[0]**2/(sigma + v[0]**2)
        v /= v[0]

    return v, beta


def House_matvec(A, v, beta, order='AP', check_input=True):
        '''
        Compute the matrix-matrix product AP or PA, where P
        is a Householder matrix P = I - beta outer(v,v)
        (Golub and Van Loan, 2013, p. 236).

        Parameters
        ----------
        A : array 2D
            Matrix used to compute the product.

        v : array 1D
            Householder vector.

        beta : scalar
            Parameter 2/dot(v,v).

        order : string
            If 'PA', it defines the product AP. If 'AP',
            it defines the product PA. Default is 'AP'.

        check_input : boolean
            If True, verify if the input is valid. Default is True.

        Returns
        -------
        C : array 2D
            Matrix-matrix product.
        '''
        A = np.asarray(A)
        v = np.asarray(v)
        if check_input is True:
            assert A.ndim == 2, 'A must be a matrix'
            assert v.ndim == 1, 'v must be a vector'
            assert np.isscalar(beta), 'beta must be a scalar'
            assert order in ['PA', 'AP'], "order must be 'PA' or 'AP'"

        if order is 'AP':
            assert A.shape[1] == v.size, 'A shape[1] must be equal to v size'
            C = A - np.outer(np.dot(A, v), beta*v)
        else:
            assert v.size == A.shape[0], 'v size must be equal to A shape[0]'
            C = A - np.outer(beta*v, np.dot(v, A))

        return C


# Givens rotations
def Givens_rotation(a, b, check_input=True):
    '''
    Given real numbers a and b, this function computes c = cos(theta)
    and s = sin(theta) so that ca - sb = r and sa + cb = 0 (Golub and
    Van Loan, 2013, Algorithm 5.1.3, p. 240).

    Parameters
    ----------
    a, b : scalars
        They form the vector to be rotated.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    c, s : scalars
        Cosine and Sine of theta forming the Givens rotation matrix.
    '''
    if check_input is True:
        assert np.isscalar(a) and np.isscalar(b), 'a and b must be scalars'

    if b == 0:
        c = 1
        s = 0
    else:
        if np.abs(b) > np.abs(a):
            tau = -a/b
            s = 1/np.sqrt(1 + tau**2)
            c = s*tau
        else:
            tau = -b/a
            c = 1/np.sqrt(1 + tau**2)
            s = c*tau

    return c, s


def Givens_matvec(A, c, s, i, k, order='AG', check_input=True):
    '''
    Update matrix A with the matrix-matrix product AG or GTA, where
    G is a Givens rotation G(i, k, theta) (Golub and Van Loan, 2013,
    p. 241).

    Parameters
    ----------
    A : array 2D
        Matrix to be updated.

    c, s : scalars
        Cosine and Sine of theta forming the Givens rotation matrix.

    i, k : ints
        Indices of the Givens rotation matrix.

    order : string
        If 'AG', it defines the product AG. If 'GTA',
        it defines the product GTA. Default is 'AG'.

    check_input : boolean
        If True, verify if the input is valid. Default is True.
    '''
    A = np.asarray(A)
    if check_input is True:
        assert A.ndim == 2, 'A must be a matrix'
        assert np.isscalar(c) and np.isscalar(s), 'c and s must be scalars'
        assert isinstance(i, int) and (i >= 0), 'i must be a an integer >= 0'
        assert isinstance(k, int) and (k >= 0), 'k must be a an integer >= 0'
        assert np.allclose((c**2 + s**2), 1), 'c**2 + s**2 must be equal to 1'
        assert order in ['AG', 'GTA'], "order must be 'AG' or 'GTA'"

    M = A.shape[0]
    N = A.shape[1]
    G = np.array([[ c, s],
                  [-s, c]])
    if order is 'AG':
        assert (i <= N) and (k <= N), 'i and k must be < N'
        A[:,[i,k]] = np.dot(A[:,[i,k]], G)
    else:
        assert (i <= M) and (k <= M), 'i and k must be < M'
        A[[i,k],:] = np.dot(G.T, A[[i,k],:])


def Givens_cs2rho(c, s, check_input=True):
    '''
    Compute a single float rho representing the matrix Z
    | c   s |
    |-s   c |
    according to Golub and Van Loan, 2013, p. 242.

    Parameters
    ----------
    c, s : scalars
        Scalars computed with function Givens_rotation.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    rho : float
        Representing scalar.
    '''
    if check_input is True:
        assert np.isscalar(c) and np.isscalar(s), 'c and s must be scalars'
        assert np.allclose((c**2 + s**2), 1), 'c**2 + s**2 must be equal to 1'

    if c == 0:
        rho = 1
    elif np.abs(s) < np.abs(c):
        rho = np.sign(c)*s/2
    else:
        rho = 2*np.sign(s)/c

    return rho


def Givens_rho2cs(rho, check_input=True):
    '''
    Compute c and s from the representing scalar rho
    obtained with function Givens_cs2rho (Golub and Van Loan, 2013, p. 242).

    Parameters
    ----------
    rho : scalar
        Representing scalar obtained with function Givens_cs2rho.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    c, s : float
        Scalars computed with function Givens_rotation.
    '''
    if check_input is True:
        assert np.isscalar(rho), 'rho must be a scalar'

    if rho == 1:
        c = 0
        s = 1
    elif np.abs(rho) < 1:
        s = 2*rho
        c = np.sqrt(1 - s**2)
    else:
        c = 2/rho
        s = np.sqrt(1 - c**2)

    return c, s


# QR factorization
def QR_House(A, check_input=True):
    '''
    Compute the M x M Householder matrices Hj such that
    Q = H0 H1 ... HN-1 is an M x M orthogonal matrix and QTA = R,
    where A is an M x N matrix, M >= N, and R is an M x N upper
    triangular matrix. The upper triangular part
    of A is overwritten by R and the lower triangular part below the
    main diagonal is overwritten by the Householder vectors associated
    with the Householder matrices (Golub and Van Loan, 2013, Algorithm
    5.2.1, p. 249).

    Parameters
    ----------
    A : array 2D
        M x N matrix (M >= N) to be factored.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    '''
    A = np.asarray(A)
    if check_input is True:
        assert A.ndim == 2, 'A must be a matrix'
        assert A.shape[0] >= A.shape[1], 'A must be M x N, where M >= N'

    M = A.shape[0]
    N = A.shape[1]
    for j in range(N):
        v, beta = House_vector(x=A[j:,j], check_input=False)
        A[j:,j:] = House_matvec(A=A[j:,j:], v=v, beta=beta,
                                order='PA', check_input=False)
        # if j < M:
        #     A[j+1:,j] = v[1:M-j+2]
        # j is always lower than M
        #A[j+1:,j] = v[1:M-j+2]
        A[j+1:,j] = v[1:]


def Q_from_QR_House(A, check_input=True):
    '''
    Retrieve the M x M matrix Q from the lower triangle of the
    M x N matrix A computed with function QR_House.

    Parameters
    ----------
    A : array 2D
        M x N matrix returned by function QR_House.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    Q : array 2D
        M x M orthogonal matrix formed by the product of
        N M x M Householder matrices, where N is the number
        of columns of A.
    '''
    A = np.asarray(A)
    if check_input is True:
        assert A.ndim == 2, 'A must be a matrix'

    M = A.shape[0]
    N = A.shape[1]
    # Compute the full M x M Q matrix
    Q = np.identity(M)
    for j in range(N-1,-1,-1):
        v = np.hstack([1, A[j+1:,j]])
        beta = 2/(1 + np.dot(A[j+1:,j],A[j+1:,j]))
        Q[j:,j:] = House_matvec(A=Q[j:,j:], v=v, beta=beta,
                                order='PA', check_input=False)

    return Q


def QR_Givens(A, check_input=True):
    '''
    Compute the Givens rotations Gj such that
    Q = G0G1...Gt is an M x M orthogonal matrix and QTA = R,
    where A is an M x N matrix, M >= N, and R is an M x N upper
    triangular matrix. The upper triangular part
    of A is overwritten by R and the lower triangular part below the
    main diagonal is overwritten by the representing scalar obtained with
    function cs2rho (Golub and Van Loan, 2013, Algorithm 5.2.4, p. 252).

    Parameters
    ----------
    A : array 2D
        M x N matrix (M >= N) to be factored.

    check_input : boolean
        If True, verify if the input is valid. Default is True.
    '''
    A = np.asarray(A)
    if check_input is True:
        assert A.ndim == 2, 'A must be a matrix'
        assert A.shape[0] >= A.shape[1], 'A must be M x N, where M >= N'

    M = A.shape[0]
    N = A.shape[1]
    for j in range(N):
        for i in range(M-1, j, -1):
            c, s = Givens_rotation(a=A[i-1,j], b=A[i,j], check_input=False)
            #Givens_matvec(A, c, s, i-1, i, order='GTA', check_input=False)
            # By passing only the j: columns, the stored representing factors
            # aren't 'destroyed' by the algorithm
            Givens_matvec(A[:,j:], c, s, i-1, i, order='GTA', check_input=False)
            A[i,j] = Givens_cs2rho(c, s, check_input=False)


def Q_from_QR_Givens(A, check_input=True):
    '''
    Retrieve the M x M matrix Q from the lower triangle of the
    M x N matrix A computed with function QR_Givens by using the
    function rho2cs.

    Parameters
    ----------
    A : array 2D
        M x N matrix returned by function QR_Givens.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    Q : array 2D
        M x M orthogonal matrix formed by the product of N
        M x M Givens rotation matrices, where N is the number
        of columns of A.
    '''
    A = np.asarray(A)
    if check_input is True:
        assert A.ndim == 2, 'A must be a matrix'

    M = A.shape[0]
    N = A.shape[1]
    Q = np.identity(M)
    for j in range(N):
        for i in range(M-1, j, -1):
            c, s = Givens_rho2cs(rho=A[i,j], check_input=False)
            Givens_matvec(Q, c, s, i-1, i, order='AG', check_input=False)

    return Q


def QR_MGS(A, check_input=True):
    '''
    Compute the QR factorization of a full-column rank M x N
    matrix A, where Q1 is an M x N orthogonal matrix and R1 is
    an N x N upper triangular matrix by applying the Modified
    Gram-Schmidt method (Golub and Van Loan, 2013, Algorithm 5.2.6,
    p. 255).

    Parameters
    ----------
    A : array 2D
        Full-column rank M x N matrix (M >= N) to be factored.

    check_input : boolean
        If True, verify if the input is valid. Default is True.

    Returns
    -------
    Q1 : array 2D
         M x N orthogonal matrix.

    R1 : array 2D
        N x N upper triangular matrix.
    '''
    A = np.asarray(A)
    if check_input is True:
        assert A.ndim == 2, 'A must be a matrix'
        assert A.shape[0] >= A.shape[1], 'A must be M x N, where M >= N'

    M = A.shape[0]
    N = A.shape[1]

    Q1 = A.copy()
    R1 = np.zeros((N,N))
    for k in range(N):
        R1[k,k] = np.linalg.norm(Q1[:,k])
        Q1[:,k] = Q1[:,k]/R1[k,k]
        for j in range(k+1,N):
            R1[k,j] = np.dot(Q1[:,k],Q1[:,j])
            Q1[:,j] -= R1[k,j]*Q1[:,k]

    return Q1, R1
