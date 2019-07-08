# Brief description of the topics to be studied along the course MCOM

<img src='LU_decomposition_sketch.JPG' width = 700>

> All the content of this folder can be accessed at [nbviewer](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/tree/master/Content/)

#### First steps in Python

The idea here is giving the required background to follow the course.

Access the directory `first_steps_Python` and take a look at the instructions.

#### Basic vector operations

* notation ([`basics-vector.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/basics-vector.ipynb))

* dot product ([`dot.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/dot.ipynb))

    - [x] Exercise: create a function for computing the dot product

* Hadamard product of vectors ([`hadamard.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/hadamard.ipynb))

    - [x] Exercise: create a function for computing the Hadamard product

* outer product ([`outer.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/outer.ipynb))

    - [x] Exercise: create a function for computing the outer product

* Vector norms
([`vector-norms.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/vector-norms.ipynb))

    - [x] Exercise: create a single function for computing the 2-, 1- and infinity-norm of a vector

#### Basic matrix operations

* matrix-vector product ([`matrix-vector.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/matrix-vector.ipynb))

    - [x] Exercise: matrix-vector product functions
    - [x] Exercise: comparison with the moving average code developed in a previous class
    - [x] Exercise: computation of first derivative by using the central finite difference

* matrix-matrix product ([`matrix-matrix.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/matrix-matrix.ipynb))

    - [x] Exercise: matrix-matrix product functions
    - [x] Exercise: rotation matrices

#### How to determine the computational cost of a given operation?

* Floating-point operations (flops) ([`flops.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/flops.ipynb))

    - [ ] Exercise (extra): total number of flops required to perform simple matrix operations

#### Structured matrices

* Permutation matrices ([`permutation_matrices.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/permutation_matrices.ipynb))

* Diagonal matrices ([`diagonal_matrices.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/diagonal_matrices.ipynb))

    - [ ] Exercise: products of diagonal and full matrices

* Triangular matrices ([`triangular_matrices.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/triangular_matrices.ipynb))

    - [ ] Exercise (extra): flops associated with the product of triangular matrices and vectors
    - [ ] Exercise: products of triangular matrices and vectors

* Block matrices ([`block_matrices.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/block_matrices.ipynb))

    - [ ] Exercise: product of two complex matrices

* Symmetric matrices ([`symmetric_matrices.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/symmetric_matrices.ipynb))

    - [ ] Exercise (extra): product of symmetric matrices and vectors

#### Numerical solution of linear systems

* Introduction to linear systems ([`intro_linear_syst.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/intro_linear_syst.ipynb))

* Triangular systems ([`triangular_systems.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/triangular_systems.ipynb))

    - [ ] Exercise: upper triangular system
    - [ ] Exercise: lower triangular system
    - [ ] Exercise: simple vertical seismic profiling

* Gaussian elimination - Introduction ([`gauss-elim-intro.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/gauss-elim-intro.ipynb))

* Gaussian elimination - Outer product formulation ([`gauss-elim-outer.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/gauss-elim-outer.ipynb))

* Gaussian elimination - Pivoting ([`gauss-elim-pivoting.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/gauss-elim-pivoting.ipynb))

    - [ ] Exercise: Gaussian elimination with partial pivoting
    - [ ] Exercise: Calculating inverse matrices

* LU decomposition - Introduction ([`lu_decomp_intro.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/lu_decomp_intro.ipynb))

    - [ ] Exercise: LU decomposition without pivoting

* LU decomposition - Pivoting ([`lu_decomp_pivoting.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/lu_decomp_pivoting.ipynb))

    - [ ] Exercise: LU decomposition with partial pivoting

* LDL<sup>T</sup> decomposition - Symmetric matrices ([`ldlt_decomp.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/ldlt_decomp.ipynb))

    - [ ] Exercise: LDL<sup>T</sup> decomposition

* Cholesky decomposition - Symmetric and positive definite matrices ([`chol_decomp.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/chol_decomp.ipynb))

    - [ ] Exercise: Cholesky decomposition

* Least squares ([`least_squares.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/least_squares.ipynb))

    - [ ] Exercise: Fitting a straight line

* Simple gravity network ([`grav_net.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/grav_net.ipynb))

    - [ ] Exercise: Calculating absolute gravity values from measurements of gravity differences

#### Numerical solution of nonlinear systems

> This topic is given in class and part of it can be found in the files `Nonlinear_methods.odp` and `Nonlinear_methods.pdf`

* Simple epicenter problem ([`epicenter.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/epicenter.ipynb))

    - [ ] Exercise: Compute the Jacobian and Hessian matrices
    - [ ] Exercise: Estimate the horizontal coordinates of an epicenter by using the Newton's, Gauss-Newton, Steepest decent and
    Levenberg-Marquardt methods

#### Interpolation

* Lagrange's method ([`lagrange.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/lagrange.ipynb))

    - [ ] Exercise: Interpolate a gravity anomaly on a regular profile

* Neville's method ([`neville.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/neville.ipynb))

    - [ ] Exercise (extra): Interpolate gravity data on a regular profile

* Cubic splines ([`cub_splines.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/cub_splines.ipynb))

    - [ ] Exercise (extra): Interpolate gravity data on a regular profile

* Polynomial fitting ([`polynomial.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/polynomial.ipynb))

    - [ ] Exercise: Interpolate gravity data on a regular profile
    - [ ] Exercise (extra): Interpolate gravity data on a regular grid

* Biharmonic Splines ([`biharmonic-splines.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/biharmonic-splines.ipynb))

    - [ ] Exercise (extra): Interpolate gravity data on a regular grid

#### Numerical solution of differential equations

* Finite differences - part 1 ([`fd_intro1.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/fd_intro1.ipynb))

    - [ ] Exercise: Solve the exponential decay equation

* Finite differences - part 2 ([`fd_intro2.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/fd_intro2.ipynb))

    - [ ] Exercise: Generalize the previous code

* *Finite differences - part 3*

#### Numerical integration

* Newton-Cotes formulas ([`newton-cotes.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/newton-cotes.ipynb))

    - [ ] Exercise: Simulate an abrupt temperature perturbation

#### Transforms

* Fourier Transform 1D - part 1 ([`fourier_1D_1.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/fourier_1D_1.ipynb))

    - [ ] Exercise: Implement the Fourier series for a periodic function

* Fourier Transform 1D - part 2 ([`fourier_1D_2.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/fourier_1D_2.ipynb))

* Fourier Transform 1D - part 3 ([`fourier_1D_3.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/fourier_1D_3.ipynb))

* Fourier Transform 1D - part 4 ([`fourier_1D_4.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/fourier_1D_4.ipynb))

    - [ ] Exercise: Implement the Discrete Fourier Transform 1D
    - [ ] Exercise: Calculate the horizontal derivative of a
    total-field anomaly on a profile
