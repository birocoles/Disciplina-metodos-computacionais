#Brief description of the topics to be studied along the course MCOM

<img src='LU_decomposition_sketch.JPG' width = 500>

> All the content of this folder can be accessed at [nbviewer](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/tree/master/Content/)

####First steps in Python

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

    - [x] Exercise **1**: implement the SMA filter

####Basic matrix operations

It presents some basic concepts about vectors and matrices.
Besides that, it is also presented some algorithms for computing:

* scalar-vector product ([`scalar-vector.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/scalar-vetor.ipynb))

* dot product ([`dot.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/dot.ipynb))

* other products of vectors ([`other.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/other.ipynb))

    - [x] Exercise **2**: Hadamard product
    - [x] Exercise **3**: Outer product
    - [x] Exercise **4**: Outer product versus `numpy.meshgrid` function

* matrix-vector product ([`matrix-vector.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/matrix-vector.ipynb))

    - [x] Exercise **5**: matrix-vector product functions
    - [x] Exercise **6**: comparison with the moving average code developed in a previous class
    - [x] Exercise **7**: computation of first derivative by using the central finite difference

* matrix-matrix product ([`matrix-matrix.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/matrix-matrix.ipynb))

    - [x] Exercise **8**: matrix-matrix product functions
    
####Special matrices
    
* Diagonal matrices ([`diagonal_matrices.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/diagonal_matrices.ipynb))

    - [x] Exercise **9**: products of diagonal and full matrices
    
* Triangular matrices ([`triangular_matrices.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/triangular_matrices.ipynb))

    - [x] Exercise **10**: products of triangular matrices and vectors
    
* Symmetric matrices ([`symmetric_matrices.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/symmetric_matrices.ipynb))

    - [x] Exercise **11**: product of symmetric matrices and vectors
    
* *Banded matrices* (`banded_matrices.ipynb`) - extra

* *Block matrices*  (`block_matrices.ipynb`) - extra

####Numerical solution of linear systems

Present some classical algorithms for solving linear systems.

* Introduction to linear systems ([`intro_linear_syst.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/intro_linear_syst.ipynb))

* Special linear systems ([`special_linear_syst.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/special_linear_syst.ipynb))

    - [x] Exercise **12**: upper triangular system
    - [x] Exercise **13**: lower triangular system

* Gaussian elimination - Introduction ([`gauss-elim-intro.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/gauss-elim-intro.ipynb))

* Gaussian elimination - Outer product formulation ([`gauss-elim-outer.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/gauss-elim-outer.ipynb))

* Gaussian elimination - Pivoting ([`gauss-elim-pivoting.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/gauss-elim-pivoting.ipynb))

    - [x] Exercise **14**: Gaussian elimination with partial pivoting
    - [x] Exercise **15**: Calculating inverse matrices

* LU decomposition - Introduction ([`lu_decomp_intro.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/lu_decomp_intro.ipynb))

    - [x] Exercise **16**: LU decomposition without pivoting

* LU decomposition - Pivoting ([`lu_decomp_pivoting.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/lu_decomp_pivoting.ipynb))

    - [x] Exercise **17**: LU decomposition with partial pivoting

* LDL<sup>T</sup> decomposition - Symmetric matrices ([`ldlt_decomp.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/ldlt_decomp.ipynb))

    - [ ] Exercise **18**: LDL<sup>T</sup> decomposition

* Cholesky decomposition - Symmetric and positive definite matrices ([`chol_decomp.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/chol_decomp.ipynb))

    - [ ] Exercise **19**: Cholesky decomposition

* *Singular Value Decomposition (SVD)* (`svd.ipynb`) - extra

* Least squares ([`least_squares.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/least_squares.ipynb))

    - [ ] Exercise **20**: Fitting a straight line

* Simple gravity network ([`grav_net.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/grav_net.ipynb))

    - [ ] Exercise **21**: Calculating absolute gravity values from measurements of gravity differences

####Numerical solution of nonlinear systems

* Newton ([`newton.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/newton.ipynb))

* Steepest descent ([`steepest_decent.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/steepest_decent.ipynb))

* Gauss-Newton ([`gauss_newton.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/gauss_newton.ipynb))

* Levenberg-Marquardt ([`leven_marq.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/leven_marq.ipynb))

* *Conjugated gradient* (`conjugated_grad.ipynb`) - extra

* Simple epicenter problem ([`epicenter.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/master/Content/epicenter.ipynb))

    - [ ] Exercise **22**: Estimate the horizontal coordinates of a epicenter

####Interpolation

* Lagrange's method

* Neville's method

* Polynomial fitting

* Cubic splines

####Solução numérica de equações diferenciais

* Diferenças finitas

* *Elementos finitos*

####*Integração numérica*

* *Fórmulas de Newton-Cotes*

* *Quadratura Gaussiana*

####*Transformadas*

* *Transformada de Fourier*

* *Transformada de Hilbert*


####**P.S.**

Os tópicos destacados em *itálico* poderão ser abordados ou não,
dependendo do andamento do curso.


#### Template para a elaboração dos códigos

Todos os códigos a serem desenvolvidos durante a disciplina deverão
seguir a formatação do Jupyter Notebook `template-codigo.ipynb`, que está
dentro do diretório `Conteudo`.