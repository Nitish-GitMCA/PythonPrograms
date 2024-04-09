# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 03:44:06 2024

@author: nitis
"""

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#argument
def sum(a,b=5):
    print(a+b)
sum(50)   


def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9)) 
