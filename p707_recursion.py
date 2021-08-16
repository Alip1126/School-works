# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:10:11 2021

@author: Al Yalikun

"""

def parentheses_recursive(str_par):
       if str_par == "" : 
           return True
       if str_par[0] == ")":
           return False
       else:
           if str_par.count("(") > 0 and str_par.count(")") > 0:
               str_par = str_par.replace("(", "",1)
               str_par = str_par.replace(")", "",1)
               #print(str_par)
               return parentheses_recursive(str_par)
           else:
               return False
           

assert parentheses_recursive("(())")
assert parentheses_recursive("()()()()()")
assert parentheses_recursive("(()()())")
print( parentheses_recursive("(((((()())))))"))
assert parentheses_recursive("((((((((((((((()))))))))))))))")
assert parentheses_recursive("(()()()()()()()())")
assert parentheses_recursive("(())(())(())(())")
print(parentheses_recursive(")("))
assert not parentheses_recursive("((((((()))")
assert not parentheses_recursive("((()())(")
assert not parentheses_recursive("())(()())")
assert not parentheses_recursive("()()())))(())")
assert not parentheses_recursive(")(((((()())))))(")
assert not parentheses_recursive("(((((((((((((()")

print("Program passed!")