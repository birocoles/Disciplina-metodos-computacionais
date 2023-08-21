# First steps in Python

## Software Carpentry lesson

Access the lesson [Programming with Python](https://swcarpentry.github.io/python-novice-inflammation/)
at Software Carpentry. At [Setup](https://swcarpentry.github.io/python-novice-inflammation/setup.html):

#### Install Python

> If you have already installed Python, go to the next topic.

#### Obtain lesson materials

> Create a directory called `swc-python`, download the file
`python-novice-inflammation-data.zip` and unzip the directory `data`. We will
not use the other file.

Now, start a Jupyter Notebook at the directory `swc-python`. Use the name
`topic-1.ipynb`. We will use this notebook to do the tasks of topic
[`Python Fundamentals`](https://swcarpentry.github.io/python-novice-inflammation/01-intro/index.html).
After finishing this topic, start a new notebook at the
directory `swc-python` with the name `topic-2.ipynb`. Use this notebook to
do the tasks of topic [`Analyzing Patient Data`](https://swcarpentry.github.io/python-novice-inflammation/02-numpy/index.html)
and so on. We will cover the topics 1 to 10. Topics 11 and 12 are bonus.

## Notation for vectors and Pseudo-code

After finishing the Software Carpentry lesson, take a look in the notebook
[`notation.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/2022/Content/first_steps_Python/notation.ipynb).

## Simple Moving Average (SMA)

After finishing the Software Carpentry lesson and taking a look in the notebook
[`notation.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/2022/Content/first_steps_Python/notation.ipynb),
you are ready to understand the application of a [SMA filter](https://en.wikipedia.org/wiki/Moving_average#Simple_moving_average) to a synthetic data set. The key points are:

* Create functions at external files
* Create tests with `pytest`

## Templates for functions and tests

Along the course, we will create several functions and tests. In order to keep
them readable, I have established templates. Find them in the notebook
[`templates.ipynb`](https://nbviewer.jupyter.org/github/birocoles/Disciplina-metodos-computacionais/blob/2022/Content/first_steps_Python/templates.ipynb).
