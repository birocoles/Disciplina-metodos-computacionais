# Brief description of the topics to be studied along the course MCOM

<img src='LU_decomposition_sketch.JPG' width = 500>

> All the content of this folder can be accessed at [nbviewer](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/tree/master/Content/)

#### First steps in Python

> The contents of this topic are at the directory: `first_steps_Python`

It presents a basic introduction of Python programming. 
I would like to stress that the main goal in 
this part of the course IS NEITHER TEACHING PROGRAMMING NOR PYTHON.
Rather, it gives the required background to follow the classes.

The content of this topic is mostly based on the lessons
[Programming with Python](http://swcarpentry.github.io/python-novice-inflammation/)
of the [Software Carpentry](http://software-carpentry.org/).

* Software Carpentry Lessons ([`SC\analyzing_patient_data.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/first_steps_Python/SC/analyzing_patient_data.ipynb))

* Simple moving average filter ([`SMA\sma.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/first_steps_Python/SMA/sma.ipynb))

    - [ ] Exercise **1**: implement the SMA filter

#### Basic matrix operations

It presents some basic concepts about vectors and matrices.
Besides that, it is also presented some algorithms for computing:

* scalar-vector product ([`scalar-vector.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/scalar-vetor.ipynb))

* dot product ([`dot.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/dot.ipynb))

* other products of vectors ([`other.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/other.ipynb))

    - [ ] Exercise **2**: Hadamard product
    - [ ] Exercise **3**: Outer product
    - [ ] Exercise **4**: Outer product versus `numpy.meshgrid` function

* matrix-vector product ([`matrix-vector.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/matrix-vector.ipynb))

    - [ ] Exercise **5**: matrix-vector product functions
    - [ ] Exercise **6**: comparison with the moving average code developed in a previous class
    - [ ] Exercise **7**: computation of first derivative by using the central finite difference

* matrix-matrix product ([`matrix-matrix.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/matrix-matrix.ipynb))

    - [ ] Exercise **8**: matrix-matrix product functions
    
#### Special matrices
    
* Diagonal matrices ([`diagonal_matrices.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/diagonal_matrices.ipynb))

    - [ ] Exercise **9**: products of diagonal and full matrices
    
* Triangular matrices ([`triangular_matrices.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/triangular_matrices.ipynb))

    - [ ] Exercise **10**: products of triangular matrices and vectors
    
* Symmetric matrices ([`symmetric_matrices.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/symmetric_matrices.ipynb))

    - [ ] Exercise **11**: product of symmetric matrices and vectors
    
* *Banded matrices* (`banded_matrices.ipynb`) - extra

* *Block matrices*  (`block_matrices.ipynb`) - extra

#### Numerical solution of linear systems

Present some classical algorithms for solving linear systems.

* Introduction to linear systems ([`intro_linear_syst.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/intro_linear_syst.ipynb))

* Special linear systems ([`special_linear_syst.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/special_linear_syst.ipynb))

    - [ ] Exercise **12**: upper triangular system
    - [ ] Exercise **13**: lower triangular system

* Gaussian elimination - Introduction ([`gauss-elim-intro.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/gauss-elim-intro.ipynb))

* Gaussian elimination - Outer product formulation ([`gauss-elim-outer.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/gauss-elim-outer.ipynb))

* Gaussian elimination - Pivoting ([`gauss-elim-pivoting.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/gauss-elim-pivoting.ipynb))

    - [ ] Exercise **14**: Gaussian elimination with partial pivoting
    - [ ] Exercise **15**: Calculating inverse matrices

* LU decomposition - Introduction ([`lu_decomp_intro.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/lu_decomp_intro.ipynb))

    - [ ] Exercise **16**: LU decomposition without pivoting

* LU decomposition - Pivoting ([`lu_decomp_pivoting.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/lu_decomp_pivoting.ipynb))

    - [ ] Exercise **17**: LU decomposition with partial pivoting

* LDL<sup>T</sup> decomposition - Symmetric matrices ([`ldlt_decomp.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/ldlt_decomp.ipynb))

    - [ ] Exercise **18**: LDL<sup>T</sup> decomposition

* Cholesky decomposition - Symmetric and positive definite matrices ([`chol_decomp.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/chol_decomp.ipynb))

    - [ ] Exercise **19**: Cholesky decomposition

* *Singular Value Decomposition (SVD)* (`svd.ipynb`) - extra

* Least squares ([`least_squares.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/least_squares.ipynb))

    - [ ] Exercise **20**: Fitting a straight line

* Simple gravity network ([`grav_net.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/grav_net.ipynb))

    - [ ] Exercise **21**: Calculating absolute gravity values from measurements of gravity differences

#### Numerical solution of nonlinear systems

* Newton ([`newton.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/newton.ipynb))

* Steepest descent ([`steepest_decent.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/steepest_decent.ipynb))

* Gauss-Newton ([`gauss_newton.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/gauss_newton.ipynb))

* Levenberg-Marquardt ([`leven_marq.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/leven_marq.ipynb))

* *Conjugated gradient* (`conjugated_grad.ipynb`) - extra

* Simple epicenter problem ([`epicenter.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/epicenter.ipynb))

    - [ ] Exercise **22**: Estimate the horizontal coordinates of a epicenter

#### Interpolation

* Lagrange's method ([`lagrange.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/lagrange.ipynb))

    - [ ] Exercise **23**: Interpolate a gravity anomaly on a regular profile

* Neville's method ([`neville.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/neville.ipynb))

    - [ ] Exercise **24**: Interpolate gravity data on a regular profile
    
* Cubic splines ([`cub_splines.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/cub_splines.ipynb))

    - [ ] Exercise **25**: Interpolate gravity data on a regular profile

* Polynomial fitting ([`polynomial.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/polynomial.ipynb))
    - [ ] Exercise **26**: Interpolate gravity data on a regular profile
    - [ ] Exercise **27**: Interpolate gravity data on a regular grid

#### Numerical solution of differential equations

* Finite differences - part 1 ([`fd_intro1.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/fd_intro1.ipynb))

    - [ ] Exercise **28**: Solve the exponential decay equation
    
* Finite differences - part 2 ([`fd_intro2.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/fd_intro2.ipynb))

    - [ ] Exercise **extra**: Generalize the previous code

#### Numerical integration

* Newton-Cotes formulas ([`newton-cotes.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/newton-cotes.ipynb))

    - [ ] Exercise **29**: Simulate a vertical seismic profiling

* *Gaussian quadrature*

#### Transforms

* Fourier Transform 1D - part 1 ([`fourier_1D_1.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/fourier_1D_1.ipynb))

    - [ ] Exercise **extra**: Implement the Fourier series for a periodic function
    
* Fourier Transform 1D - part 2 ([`fourier_1D_2.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/fourier_1D_2.ipynb))

* Fourier Transform 1D - part 3 ([`fourier_1D_3.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/fourier_1D_3.ipynb))

* Fourier Transform 1D - part 4 ([`fourier_1D_4.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/fourier_1D_4.ipynb))

    - [ ] Exercise **30**: Implement the Discrete Fourier Transform 1D
    - [ ] Exercise **extra**: Calculate the horizontal derivative of a
    total-field anomaly on a profile
    - [ ] Exercise **extra**: Calculate the Analytic Signal Amplitude of a 
    total-field anomaly on a profile


#### **P.S.**

The topics in *italic* may be given or not, depending on the development of 
the course.

#### Template for elaborating the codes

All codes to be developed along this course must follow the format described in
the Jupyter Notebook `code-template.ipynb`, which is in the folder `Contents`.