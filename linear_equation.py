# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:07:16 2021

@author: Al Yalikun
linear equation : y = mx + b
"""


class Liner_equation(object):
    '''Linear equation with m and b.'''
    def __init__(self, m_value, b_value):
        self.m_value = m_value
        self.b_value = b_value   
    def __str__(self):
        '''String representation for printing'''
        if self.m_value == 0:
            return "y = " + str(self.b_value)
        if self.b_value > 0:
            return "y = " + str(self.m_value) +"x " + "+ " + str(self.b_value)
        elif self.b_value < 0:
            return "y = " + str(self.m_value) +"x " + str(self.b_value)
        elif self.b_value == 0:
            return "y = " + str(self.m_value) + "x"
    def __repr__(self):
        ''' Used in the interpreter. Call __str__ for now'''
        return self.__str__()   
    def __add__(self, param_Liner):
        '''Add two Liners equations'''
        if type(param_Liner) == int:
            param_Liner = Liner_equation(0, param_Liner)
        if type(param_Liner) == Liner_equation:
            #sum the m values and b values
            m_sum = self.m_value + param_Liner.m_value
            b_sum = self.b_value + param_Liner.b_value
        return Liner_equation(int(m_sum), int(b_sum))
    def value(self,x):
        '''find the value of equation'''
        x_totall = self.m_value * x + self. b_value
        return "value of equation = " + str(x_totall)
    def compose(self,param_Liner):
        '''composing two liner equations '''
        composed_m = self.m_value * param_Liner.m_value
        composed_b = self.m_value * param_Liner.b_value
        sum_of_b = composed_b + self.b_value
        if sum_of_b > 0:
            composed_e = "y = " + str(composed_m) + "x" + " + " + str(sum_of_b)
        if sum_of_b < 0:
            composed_e = "y = " + str(composed_m) + "x" + str(sum_of_b)
        return "composed equation : " + str(composed_e)
    def __eq__(self, param_Liner):
        '''Compare two liner for equality and return a Boolean'''
        return self.m_value, self.b_value == param_Liner.m_value,\
                            param_Liner.b_value
                            
try:  
    print("----------testing for m values----------")        
    e1 = Liner_equation(4,5)
    print(e1)
    e2 = Liner_equation(-1, 1)
    print(e2)        
    e3 = Liner_equation(0, 3)
    print(e3)
    print("----------testing for b values----------")
    e4 = Liner_equation(6, 2)
    print(e4)
    e5 = Liner_equation(5, -2)
    print(e5)
    e6 = Liner_equation(4, 0)
    print(e6)
except SyntaxError:
    print("Value m or b is not defined!")
    
print("----------testing with assertion----------")    

error_addition = "Error in addition method"
error_compose = "Error in compose method"
error_value = "Error in value method"
print("----------Addition method----------") 

e7 = Liner_equation(3, 6)
e8 = Liner_equation(2, 3)
sum_1 = e7 + e8
expected = Liner_equation(5, 9)
assert sum_1 == expected , error_addition

e9 = Liner_equation(-1, 6)
e10 = Liner_equation(3, 3)
sum_2 = e9 + e10
expected = Liner_equation(2, 9)
assert sum_2 == expected , error_addition

e11 = Liner_equation(0, 4)
e12 = Liner_equation(2, 3)
sum_3 = e11 + e12
expected = Liner_equation(2, 7)
assert sum_3 == expected , error_addition

e13 = Liner_equation(6, -2)
e14 = Liner_equation(7, 3)
sum_4 = e13 + e14
expected = Liner_equation(13, 1)
assert sum_4 == expected , error_addition

e15 = Liner_equation(8, 0)
e16 = Liner_equation(2, 3)
sum_5 = e15 + e16
expected = Liner_equation(10, 3)
assert sum_5 == expected , error_addition

print("Method passed!")

print("----------Compose method----------") 

e17 = Liner_equation(7, 2)
e18 = Liner_equation(3, 4)
comp_1 = e17.compose(e18)
assert e17.compose(e18) == comp_1 , error_compose

e19 = Liner_equation(-1, 6)
e20 = Liner_equation(3, 2)
comp_2 = e19.compose(e20)
assert e19.compose(e20) == comp_2 , error_compose

e21 = Liner_equation(0, 6)
e22 = Liner_equation(2, 3)
comp_3 = e21.compose(e22)
assert e21.compose(e22) == comp_3 , error_compose

e23 = Liner_equation(1, -5)
e24 = Liner_equation(2, 2)
comp_4 = e23.compose(e24)
assert e23.compose(e24) == comp_4 , error_compose

e25 = Liner_equation(5, 0)
e26 = Liner_equation(4, 8)
comp_5 = e25.compose(e26)
assert e25.compose(e26) == comp_5 , error_compose

print("Method passed!")

print("----------value method----------")

e27 = Liner_equation(4, 12)
value_1 = e27.value(3)
assert e27.value(3) == value_1 , error_value

e28 = Liner_equation(-3, 4)
value_2 = e28.value(2)
assert e28.value(2) == value_2 , error_value

e29 = Liner_equation(0, 11)
value_3 = e29.value(5)
assert e29.value(5) == value_3 , error_value

e30 = Liner_equation(3, -2)
value_4 = e30.value(4)
assert e30.value(4) == value_4 , error_value

e31 = Liner_equation(7, 0)
value_5 = e31.value(8)
assert e31.value(8) == value_5 , error_value

print("Method passed!")

print("Program passed!")








       