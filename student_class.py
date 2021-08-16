# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 00:10:06 2021

@author: Al Yalikun
"""

class Person(object):
    def __init__(self, first_name = '', last_name = ''):
        ''' Create a person: first_name, last_name, Defaults are nulls.'''
        self.last_name = last_name
        self.first_name = first_name

    def __str__(self):
        '''String representation for printing'''
        result_str = "Name: {}".format(self.first_name + ' ' + \
                                        self.last_name)
        return result_str
        
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name
    
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

class Student(Person):
    def __init__(self, first_name = "", last_name = "" , id_num = 0 , \
                 tuition_type =""):
        '''create a student, inherit Person class's behaviors, while have
        id number, in state or out of state status.'''
        Person.__init__(self, first_name, last_name)
        self.id_num = id_num
        self.tuition_type = tuition_type
        
    def __str__(self):
        '''using the __str__ from Person class'''
        name_result = Person.__str__(self)
        student_result = name_result + " ; Student Id number: {}". \
        format(self.id_num) +" ; Tuition type: {}".format(self.tuition_type)
        return student_result

    def get_id_num(self):
        return self.id_num
    
    def set_id_num(self, id_num):
        self.id_num = id_num

    def get_tuition_type(self):
        return self.tuition_type
    
    def set_tuition_type(self, tuition_type):
        self.tuition_type = tuition_type
        
        
class Undergrad(Student):
    def __init__(self, first_name = "", last_name = "" , id_num = 0, \
                     tuition_type = "", class_num = 0, gpa = 0.0):
        '''create an Undergrad, inherit Student class's behaviors, 
        while have class number and gpa'''
        Student.__init__(self, first_name, last_name , id_num , tuition_type)
        self.class_num = class_num
        self.gpa = gpa
    
    def __str__(self):
        '''using the __str__ from Student class'''
        undergrad_result = Student.__str__(self) + " ; Class level: {}". \
            format(self.class_num) + " ; Gpa: {}".format(self.gpa)
        return undergrad_result
    
    def get_class_num(self):
        return self.class_num
    
    def set_class_num(self, class_num):
        self.class_num = class_num
    
    def get_gpa(self):
        return self.gpa
    
    def set_gpa(self, gpa):
        self.gpa = gpa
        
    def advance_level(self):
        '''advacning class level for college student'''
        if self.class_num < 4 :
            return Student.__str__(self) + " ; Class level: {}". \
            format(self.class_num + 1) + " ; Gpa: {}".format(self.gpa)
        if self.class_num == 4 :
            return Student.__str__(self) + " ; Class level: {}". \
            format("Graduated") + " ; Gpa: {}".format(self.gpa)
        else:
            return "invalid year"

print("----------Person Class----------")
p1 = Person("Scarlett", "Aiden")
assert p1.__str__() == "Name: Scarlett Aiden"
print(p1)
assert p1.get_first_name() == "Scarlett"
assert p1.get_last_name() == "Aiden"
p1.set_first_name("Micheal")
assert p1.first_name == ("Micheal")
assert p1.__str__() == "Name: Micheal Aiden"
p1.set_last_name("Obama")
assert p1.last_name == "Obama"
assert p1.__str__() == "Name: Micheal Obama"
print(p1)

p2 = Person("LeBron", "James")
assert p2.__str__() == "Name: LeBron James"
print(p2)
assert p2.get_first_name() == "LeBron"
assert p2.get_last_name() == "James"
p2.set_first_name("Kobe")
assert p2.first_name == ("Kobe")
assert p2.__str__() == "Name: Kobe James"
p2.set_last_name("Bryant")
assert p2.last_name == "Bryant"
assert p2.__str__() == "Name: Kobe Bryant"
print(p2)

print()
print("----------Student Class----------") 
         
s1 = Student("Al" , "Yalkun" , 1231 ,"In-state")
print(s1)
assert s1.__str__() == "Name: Al Yalkun ; Student Id number: 1231 ; Tuition"+\
    " type: In-state"
assert s1.get_first_name() == "Al"
assert s1.get_last_name()=="Yalkun"
assert s1.get_id_num() == 1231
assert s1.get_tuition_type()== "In-state"
s1.set_first_name("Joseph")
assert s1.get_first_name() == "Joseph"
s1.set_last_name("Stalin")
assert s1.get_last_name() == "Stalin"
s1.set_id_num(1949)
assert s1.get_id_num() == 1949
s1.set_tuition_type("Out of state")
assert s1.get_tuition_type() == "Out of state"
assert s1.__str__() == "Name: Joseph Stalin ; Student Id number: 1949 ; Tui"+\
    "tion type: Out of state"
print(s1)

s2 = Student("Earl" , "Johnson" , 6969 ,"Out of state")
print(s2)
assert s2.__str__() == "Name: Earl Johnson ; Student Id number: 6969 ; Tui"+\
    "tion type: Out of state"
assert s2.get_first_name() == "Earl"
assert s2.get_last_name()=="Johnson"
assert s2.get_id_num() == 6969
assert s2.get_tuition_type()== "Out of state"
s2.set_first_name("Winston")
assert s2.get_first_name() == "Winston"
s2.set_last_name("Churchill")
assert s2.get_last_name() == "Churchill"
s2.set_id_num(1951)
assert s2.get_id_num() == 1951
s2.set_tuition_type("In-state")
assert s2.get_tuition_type() == "In-state"
assert s2.__str__()== "Name: Winston Churchill ; Student Id number: 1951 ; "+\
    "Tuition type: In-state"
print(s2)

print()
print("----------Undergrad Class----------")

u1 = Undergrad("Mike" , "Miles" , 1241 , "Out of state" , 2 , 3.1)
print(u1)
assert u1.get_first_name() == "Mike"
assert u1.get_last_name()=="Miles"
assert u1.get_id_num() == 1241
assert u1.get_tuition_type()== "Out of state"
assert u1.get_class_num() == 2
assert u1.get_gpa() == 3.1
assert u1.__str__() == "Name: Mike Miles ; Student Id number: 1241 ; "+\
    "Tuition type: Out of state ; Class level: 2 ; Gpa: 3.1"
u3 = u1.advance_level() # one class level up    
print(u3)
assert u3 == "Name: Mike Miles ; Student Id number: 1241 ; "+\
    "Tuition type: Out of state ; Class level: 3 ; Gpa: 3.1"
    
u1.set_first_name("Frank")
assert u1.get_first_name() == "Frank"
u1.set_last_name("Ocean")
assert u1.get_last_name() == "Ocean"
u1.set_id_num(5612)
assert u1.get_id_num() == 5612
u1.set_tuition_type("In-state")
assert u1.get_tuition_type() == "In-state"
u1.set_class_num(3)
assert u1.get_class_num() == 3
u1.set_gpa(2.4)
assert u1.get_gpa() == 2.4
print(u1)

u2 = Undergrad("Abel" , "Jefferson" , 1442 , "In-state" , 4 , 3.5)
print(u2)
assert u2.get_first_name() == "Abel"
assert u2.get_last_name()=="Jefferson"
assert u2.get_id_num() == 1442
assert u2.get_tuition_type()== "In-state"
assert u2.get_class_num() == 4
assert u2.get_gpa() == 3.5
assert u2.__str__() == "Name: Abel Jefferson ; Student Id number: 1442 ; "+\
    "Tuition type: In-state ; Class level: 4 ; Gpa: 3.5"
u4 = u2.advance_level() # one level up 
print(u4)
assert u4 == "Name: Abel Jefferson ; Student Id number: 1442 ; "+\
    "Tuition type: In-state ; Class level: Graduated ; Gpa: 3.5"
    
u2.set_first_name("George")
assert u2.get_first_name() == "George"
u2.set_last_name("Miller")
assert u2.get_last_name() == "Miller"
u2.set_id_num(2442)
assert u2.get_id_num() == 2442
u2.set_tuition_type("Out of state")
assert u2.get_tuition_type() == "Out of state"
u2.set_class_num(1)
assert u2.get_class_num() == 1
u2.set_gpa(4.0)
assert u2.get_gpa() == 4.0
print(u2)
print("Program passed!")
