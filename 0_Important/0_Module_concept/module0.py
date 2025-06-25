# 1. What do you mean by __name__ == '__main__'

# What is a module?
# Any file with an extention of .py is called a module in python.

# Whenever we execute a program it's module name is __main__ and this name is stored in __name__ variable

def display():
      print('hello')

display()
print(__name__)

# Variations of import statement

# Normal
import math
import random

# clubbing together
import math,random

# importing specific names from module
from math import factorial,floor

# renaming modules
import math as m
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


m.factorial(5)

from math import factorial as f

f(5)

# Order of execution of a module

import sys
for p in sys.path:
  print(p)
  
# What are packages in Python

# A package in python is a directory containing similar sub packages and modules.

# A particular directory is treated as package if it has __init__.py file in it.
# The __init__.py file may be empty or contain some initialization code related to the package

# What are 3rd party packages?

# The python community creates packages and make it available for other programmers
# PyPI -> Python Package Index
# You can upload your own package
# You can also install packages from PyPI and install using pip
# pip is a package manager utility
# it is automatically installed with python