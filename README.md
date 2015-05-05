# Métodos Computacionais Aplicados à Geofísica

> Disciplina oferecida no programa de pós-graduação em 
geofísica do [Observatório Nacional - MCTI](http://www.on.br)

**Responsável**: [Vanderlei C. Oliveira Jr.](http://www.pinga-lab.org/people/oliveira-jr.html)

## Tópicos

A descrição breve dos tópicos a serem abordados durante a 
disciplina está no diretório `Aulas`. 

####Noções de programação em linguagem Python

####Tópicos de álgebra linear

####Solução numérica de sistemas lineares

> Eliminação de Gauss

> Decomposição LU

> Decomposição de Cholesky

> *Decomposição em valores singulares (SVD)*

####Solução numérica de sistemas não-lineares

> Método de Newton

> Método steepest descent (descida mais íngreme)

> Método de Gauss-Newton

> Método de Levenberg-Marquardt

> *Método dos gradientes conjugados*

####Interpolação

> Ajuste polinomial

> *Série de Fourier*

> Splines

> *Mínima curvatura*

####Solução numérica de equações diferenciais

> Diferenças finitas

> *Elementos finitos*

####*Integração numérica*

> *Fórmulas de Newton-Cotes*

> *Quadratura Gaussiana*

####*Transformadas*

> *Transformada de Fourier*

> *Transformada de Hilbert*

Obs.: Os tópicos destacados em *itálico* poderão ser abordados ou não,
dependendo do andamento do curso.

## Bibliografia recomendada

* Kelley, C. T. Iterative methods for optimization, SIAM, 1999, [versão pdf](http://www.siam.org/books/kelley/fr18/)

* Golub, G. H. e Van Loan, C. F. Matrix computations, 4th edition, Johns Hopkins University Press, 2013

* Boyd, S. e Vandenberghe, L. Convex optimization, Cambridge University Press, 2004

* Kinzelbach, W. Groundwater modelling: An introduction with sample programs in BASIC, Elsevler, 1986

* Lapidus, L. e Pinder, G. F. Numerical solution of partial differential equations in science and engineering, John Wiley & Sons, Inc., 1999

* Press, W. H., Teukolsky, S. A, Vetterling, W. T. e Flannery, B. P. Numerical recipes in C: The art of scientific computing, second edition, Cambridge University Press, 1992

* Periódicos/sites da área 

## A linguagem Python

Diferentemente de C ou Fortran, a linguagem [Python](https://www.python.org/) 
é interpretada. Isso signififca que o código não precisa ser previamente 
compilado e os comandos são executados imediatamente. De acordo com a 
[Software Carpentry](http://software-carpentry.org/index.html), quando 
estamos programando, o tempo total necessário para obtermos a solução 
desejada é determinado por duas coisas: *o tempo gasto por **você** para 
desenvolver o código* e *o tempo gasto pelo **computador** para rodar o 
código*. Estes fatores devem ser levados em consideração no momento da 
escolha de uma linguagem de programação. Para fins acadêmicos de pesquisa 
e ensino, a linguagem Python oferece algumas vantagens, dentre as quais 
eu destaco o fato de ser gratuita e distribuída livremente na internet, 
relativamente fácil de aprender e extremamente bem documentada.

Para mais informações, eu recomendo (fortemente) que você acesse o site 
da [Software Carpentry](http://software-carpentry.org/index.html). Mais 
especificamente, dê uma olhada nas [lições](http://software-carpentry.org/v4/python/index.html) 
de Python da versão 4. Grande parte do que está feito aqui é baseado nestas 
lições. Nestas lições, os instrutores recomendam o uso do ambiente de desenvolvimento 
integrado (*integrated development environment* - IDE) 
[Wing 101](http://wingware.com/downloads/wingide-101). Contudo, eu optei pelo 
[IPython Notebook](http://ipython.org/notebook.html#the-ipython-notebook).

## IPython Notebook

O **IPython Notebook** é um documento iterativo que permite combinar 
código, texto, equações feitas em LaTeX, figuras e animações. Além disso, 
é gratuito e extremamente bem documentado. Esta poderosa feramenta computacional 
possibilita reunir (quase) todas as etapas envolvidas no desenvolvimento de 
um código com fins acadêmicos, desde a leitura e processamento dos dados até a 
visualização dos resultados. Um tutorial completo sobre **IPython Notebook** 
pode ser encontrado nos seguinte endereços:

* [http://ipython.org/notebook.html#the-ipython-notebook](http://ipython.org/notebook.html#the-ipython-notebook)
* [http://ipython.org/ipython-doc/stable/notebook/index.html](http://ipython.org/ipython-doc/stable/notebook/index.html)

## Instalação do Python e de suas dependências

Uma maneira fácil de baixar e instalar a última versão do Python e de suas 
dependências é utilizar a distribuição [Anaconda](http://continuum.io/downloads), 
da [Continuum Analytics](http://continuum.io/). Basta escolher o instalador 
adequado para o seu sistema operacional e seguir as instruções. Esta 
distribuição Python já vem com quase tudo o que você precisa para fazer os 
seus primeiros códigos Python.

## Visualização online dos IPython Notebooks

O conteúdo de cada tópico a ser abordado durante a disciplina
(isto é, as notas de aula, figuras e IPython Notebooks)
está armazenado em um diretório diferente dentro do diretório
`Aulas`. Os IPython Notebooks de cada tópico podem ser visualizados 
no nbviewer pelo seguinte link:

http://nbviewer.ipython.org/github/birocoles/Disciplina-metodos-computacionais/tree/master/Aulas/

Para tanto, após clicar no link acima, entre no diretório desejado
e clique no IPython Notebook que você deseja visualizar. Este
IPython Notebook será mostrado como uma página estática e, portanto,
não poderá ser executado. Para executar o conteúdo de um determinado
IPython Notebook é necessário baixa-lo e instalar os programas
necessários.