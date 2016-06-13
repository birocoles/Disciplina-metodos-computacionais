# Métodos Computacionais Aplicados à Geofísica

> Disciplina oferecida no programa de pós-graduação em 
geofísica do [Observatório Nacional - MCTI](http://www.on.br)

> Responsável: [Vanderlei C. Oliveira Jr.](http://www.pinga-lab.org/people/oliveira-jr.html)

## Tópicos abordados durante a disciplina

No diretório `Topicos` há uma descrição breve sobre os 
tópicos listados abaixo .

* **Noções de programação em linguagem Python**

* **Tópicos de álgebra linear**

* **Solução numérica de sistemas lineares**

* **Solução numérica de sistemas não-lineares**

* **Interpolação**

* **Solução numérica de equações diferenciais**

* **Integração numérica**

* **Transformadas**

## Bibliografia recomendada

* Kinzelbach, W. Groundwater modelling: An introduction with sample programs in BASIC, Elsevler, 1986

* Press, W. H., Teukolsky, S. A, Vetterling, W. T. e Flannery, B. P. Numerical recipes in C: The art of scientific computing, second edition, Cambridge University Press, 1992

* Horn, R. A. e Johnson, C. R. Topics in matrix analysis, Cambridge University Press, 1994

* Lapidus, L. e Pinder, G. F. Numerical solution of partial differential equations in science and engineering, John Wiley & Sons, Inc., 1999

* Kelley, C. T. Iterative methods for optimization, SIAM, 1999, [versão pdf](http://www.siam.org/books/kelley/fr18/)

* Boyd, S. e Vandenberghe, L. Convex optimization, Cambridge University Press, 2004

* Kreyszig, E. Advanced engineering mathematics, 9th edition, John Wiley & Sons, Inc., 2006

* Golub, G. H. e Van Loan, C. F. Matrix computations, 4th edition, Johns Hopkins University Press, 2013

* Periódicos/sites da área 

## A linguagem Python

Diferentemente de C ou Fortran, a linguagem [Python](https://www.python.org/) 
é interpretada. Isso signififca que o código não precisa ser previamente 
compilado e os comandos são executados imediatamente. De acordo com a 
[Software Carpentry](http://software-carpentry.org/index.html), quando 
estamos programando, o tempo total necessário para obtermos a solução 
desejada é determinado por duas coisas: *o tempo gasto por* **você** *para 
desenvolver o código* e *o tempo gasto pelo* **computador** *para rodar o 
código*. Estes fatores devem ser levados em consideração no momento da 
escolha de uma linguagem de programação. Para fins acadêmicos de pesquisa 
e ensino, a linguagem Python oferece algumas vantagens, dentre as quais 
eu destaco o fato de ser gratuita e distribuída livremente na internet, 
relativamente fácil de aprender e extremamente bem documentada.

Para mais informações, eu recomendo (fortemente) que você acesse o site 
da [Software Carpentry](http://software-carpentry.org/index.html). Mais 
especificamente, dê uma olhada na lição [Programming with Python] 
(http://swcarpentry.github.io/python-novice-inflammation/). 
Os códigos Python serão feitos utilizando-se o [Jupyter Notebook]
(http://jupyter.org/).

## Jupyter Notebook

O [**Jupyter Notebook**](http://jupyter.readthedocs.io/en/latest/content-quickstart.html) 
permite combinar código, texto, equações feitas em 
LaTeX, figuras e animações. Além disso, 
é gratuito e extremamente bem documentado. Esta poderosa feramenta computacional 
possibilita reunir (quase) todas as etapas envolvidas no desenvolvimento de 
um código com fins acadêmicos, desde a leitura e processamento dos dados até a 
visualização dos resultados. 

## Instalação do Python e de suas dependências

Uma maneira fácil de baixar e instalar a última versão do Python e de suas 
dependências é utilizar a distribuição [Anaconda](http://continuum.io/downloads), 
da [Continuum Analytics](http://continuum.io/). Para tanto:

1. Acesse o link do [Anaconda](http://continuum.io/downloads), 
escolha o instalador adequado para o seu sistema
operacional e sega as instruções. O Anaconda já vem com quase tudo o que você 
precisa para fazer os seus primeiros códigos.

2. Para checar se a instalação deu certo, abra uma janela do prompt de comando,
caso você esteja no Windows, ou um terminal, se estiver no Linux.

3. Digite o comando: `conda list`. Este comando mostrará uma
 lista de *coisas* que foram instaladas pelo Anaconda. Nesta lista,
 procure os itens: `python`, `ipython`, `ipython-notebook`, `numpy`,
 `matplotlib` e `scipy`. Se estes itens estiverem na lista, fique
 tranquilo(a)... pelo menos por enquanto :).