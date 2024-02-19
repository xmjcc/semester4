#tasks:
#create a class
#add constructor
#write a test harness
#overload the __str__ method -> test
#add a static variable to implement a unique id
#add a set to store the courses
#create a dictionary of objects -> dictionary comprehension
#overload the __eq__ method -> test
#overload the __lt__ and __gt__ methods -> test
#demonstrate a dataclass

'''
Created by Narendra for COMP216 (Sept 2020)
wk02a3_student.py

Create a simple student class. 
'''

class Student:
    '''
    The Student class.
    Each object will have the following:
      name set from the first argument in constructor
      program set from the second argument in contructor
      courses a set containing the courses enrolled in.
      __id unique generated id.
    '''
    __id = 10_000
    def __init__(self, name:str, program:str): 
        '''
        This constructor requires two arguments.

        It does the following:
         uses the first argument to initialise the name of this student
         uses the second argument to initialize the program of this student
         initialises __courses to a set containing a single course 'Programming I'
         initializes __id to the value of class variable __id (which is then incremented)        
        '''        
        self.name = name                    #define a python property name
        self.program = program
        self.__courses = {'Programming I'}                 #courses
        self.__id = str(Student.__id)
        Student.__id += 1


    def __str__(self) -> str:
        '''
        Return a string representation of this object.        
        '''            
        return f'{self.__id} {self.name} {self.program} {self.__courses}'
    
    def __eq__(self, other:'Student') -> bool:
        '''
        overloads the == operator
        return true if the program of the object matches the program of this object
        '''
        return self.program == other.program

    def __lt__(self, other:'Student') -> bool:
        '''
        overloads the < operator
        return true if the other object is enrolled is more courses
        '''
        return  len(self.__courses) < len(other.__courses)

    def __gt__(self, other:'Student') -> bool:
        '''
        overloads the > operator
        return true if the other object is enrolled is less courses
        '''
        return  len(self.__courses) > len(other.__courses)
    
    def __add__(self, course:str) -> 'Student':
        '''
        overloads the + operator
        adds the argumen to the set of courses
        Why is self returned?
        '''
        self.__courses.add(course)
        return  self

    def add_course(self, course:str) -> None:
        '''
        overloads the == operator
        return true if the two objects belongs to the same program
        '''
        self.__courses.add(course)

    def change_program(self, program:str) -> None:
        '''
        assigns the argumen to this object program attribute
        '''        
        self.program = program

#test harness
dat = [
    ('Narendra', 'Game - Programming'), ('Arben', 'Game - Programming'),
    ('Mayy', 'Artificial Intelligence'), ('Yin', 'Software Engineering Technology'),
    ('Nicoletta', 'Health Informatics'), ('Ilia', 'Software Engineering Technician'),
    ('Hao', 'Artificial Intelligence'), ('Joanne', 'Software Engineering Technology')
    ]

#initialises the dictionay of students
#uses list comprehension
students = {pair[0].lower(): Student(pair[0], pair[1]) for pair in dat}

students['narendra'].add_course('Advanced Graphics')
students['arben'].add_course('Game Programming II')
students['arben'].add_course('Simulation Design')
students['mayy'].add_course('Introduction to Artificial Intelligence')
students['nicoletta'].add_course('Telehealth')
students['ilia'].change_program('Mobile Applications')


for s in students.values():
    print(s)

s1 = 'narendra'
s2 = 'arben'

print(f'{s1} and {s2} are in {"same program" if students[s1] == students[s2] else "different programs"}')
print(f'{s1} has {"less" if students[s1] < students[s2] else "more"} courses than {s2}')

s2 = 'hao'
print(f'{s1} and {s2} are in {"same program" if students[s1] == students[s2] else "different programs"}')
print(f'{s1} has {"less" if students[s1] < students[s2] else "more"} courses than {s2}')

c = 'Programming II'
students[s1] = students[s1] + c
print(f'\n{students[s1]} after adding {c}')


from dataclasses import dataclass
@dataclass (init=True, repr=True, eq=True)
class Item:
    length: int
    title: str
    artise: str

i = Item(length=5, title='triller', artise='micheal jackson')
print(i)