# Rational numbers

def gcd(bigger, smaller):
    '''compute the greatest common divisor of two positive integers'''
    #print(' in gcd ')
    if not bigger > smaller :
        bigger, smaller = smaller, bigger
    while smaller != 0:
        remainder = bigger % smaller
        #print('gcd calc, big:{}, small:{}, rem:{}'.format(bigger, smaller, remainder))
        bigger, smaller = smaller, remainder
    return bigger

def lcm(a, b):
    '''calculate the least common multiple of two positive integers'''
    #print(' in lcm ')
    return (a*b)//gcd(a,b)


class Rational(object):
    '''Rational with numerator and denominator. 
       Denominator defaults to 1'''

    def __init__(self, numer, denom = 1):
        #print('in constructor')
        self.numer = numer
        self.denom = denom

    def __str__(self):
        '''String representation for printing'''
        #print(' in str ')
        return str(self.numer)  + '/'  +  str(self.denom)

    def __repr__(self):
        ''' Used in the interpreter. Call __str__ for now'''
        #print(' in repr ')
        return self.__str__()

    def __add__(self, param_Rational):
        '''Add two Rationals'''
        if type(param_Rational) == int:
            param_Rational = Rational(param_Rational)
        if type(param_Rational) == Rational:
            # find the lcm
            the_lcm = lcm(self.denom, param_Rational.denom)
            # multiply each numerator by the lcm, then add
            numerator_sum = the_lcm*self.numer/self.denom + \
                        the_lcm*param_Rational.numer/param_Rational.denom
            return Rational( int(numerator_sum), the_lcm )
        else:
            print("Wrong type in addition method.")
            raise(TypeError)
    __radd__ = __add__
        
    def __sub__(self, param_Rational):
        '''Subtract two Rationals'''
        #print(' in add ')
        if type(param_Rational) == int:
            param_Rational = Rational(param_Rational)
        if type(param_Rational) == Rational:
            # find the lcm
            the_lcm = lcm(self.denom, param_Rational.denom)
            # multiply each numerator by the lcm, then add
            numerator_sum = the_lcm*self.numer/self.denom - \
                        the_lcm*param_Rational.numer/param_Rational.denom
        return Rational( int(numerator_sum), the_lcm )
    __rsub__ = __sub__
    
    def __mul__(self, param_Rational):
        '''multiply two rationals'''
        numer = self.numer * param_Rational.numer
        denom = self.denom * param_Rational.denom
        return Rational(int(numer),denom)
   
        
    def __truediv__(self, param_Rational):
        '''devide two rationals'''
        numer = self.numer * param_Rational.denom
        denom = self.denom * param_Rational.numer
        return Rational(numer,denom)
          

    def reduce_rational(self):
        '''Return the reduced fraction value as a Rational'''
        # find the gcd and divide numerator and denominator by it
        the_gcd = gcd(self.numer, self.denom)
        return Rational( self.numer//the_gcd, self.denom//the_gcd)

    def __eq__(self, param_Rational):
        '''Compare two Rationals for equality and return a Boolean'''
        reduced_self  = self.reduce_rational()
        reduced_param = param_Rational.reduce_rational()
        return reduced_self.numer == reduced_param.numer and\
               reduced_self.denom == reduced_param.denom
        
# ------------------------------ MAIN --------------------
r1 = Rational(1,2)
print(r1)
##r2 = Rational(3,4)
##print(r2)
##print( gcd(18, 48))
##print( gcd(48, 18))
#print( lcm(48, 18) )
r3 = Rational(7, 18)
r4 = Rational(5, 48)
r5 = r3 + r4
print(r5)
               
#r6 = Rational(12,18)
#print(r6.reduce_rational())
#r7 = Rational(18,12)
#print(r7.reduce_rational())

r_2_3 = Rational(2,3)
if r_2_3 == r_2_3 :
    pass
else:
    print("error in equality method")

r_3_4 = Rational(3,4)
if r_2_3 == r_3_4 :
    print("error in equality method")

# the above were tested OK
error_addition = "Error in addition method"
error_subtraction = "Error in subtraction method"
error_subtraction_left = "Error in sub method involviing integer on left"
error_multiplication = "Error in mulitplication method"
error_division =  "Error in division method"
error_addition_left = "Error in addition method involving integer on left"
error_addition_right = "Error in addition method involving integer on right"

r_17_12 = Rational(17,12)
assert r_2_3 + r_3_4 == r_17_12, error_addition

r_1_12 = Rational(1, 12)
assert r_3_4 - r_2_3 == r_1_12, error_subtraction

r_6_13 = Rational(6,13)
answer_sub_left = 3 - r_6_13
assert 3 - r_6_13 == answer_sub_left, error_subtraction_left 

r_12_5 = Rational(12,5)
r_2_5  = Rational(2,5)
assert r_2_5 + 2 == r_12_5, error_addition_right

r_4_3 = Rational(4,3)
r_3_2 = Rational(3,2)
answer_mul = r_4_3 * r_3_2
assert r_4_3 * r_3_2 == answer_mul, error_multiplication

r_3_7 = Rational(3,7)
answer_add = 3 + r_3_7
assert 3 + r_3_7 == answer_add, error_addition_left

r_5_4 = Rational(5,4)
r_3_2 = Rational(3,2)
answer_division = r_5_4 / r_3_2
assert r_5_4 / r_3_2 == answer_division, error_division

print("program passed !")