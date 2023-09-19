"""
write account program for save data about employed and use function 
data:
name, age, born date, salary, work
"""

def name():
    
    global e1_n
    global e2_n
    global e3_n
    global e4_n

    e1_n = "Derek Patison "
    e2_n = "Mark Tolstoy "
    e3_n = "Helen Kolrum "
    e4_n = "Lucifer Morningstar "

    print("Name employees: ")
    print("Hello " +  e1_n)
    print("Hello " + e2_n)
    print("Hello " + e3_n)
    print("Hello " + e4_n)
    print(" ")

def age():
    e1_a = "23"
    e2_a = "48"
    e3_a = "35"
    e4_a = "50"

    print("Age employees: ")
    print(e1_n + ": " +  e1_a)
    print(e2_n + ": " + e2_a)
    print(e3_n + ": " + e3_a)
    print(e4_n + ": " + e4_a)
    print(" ")

def born_date():
    bd_1 = "23/11/1999"
    bd_2 = "4/3/2002"
    bd_3 = "5/6/1990"
    bd_4 = "7/7/1997"

    print("Born date employees: ")
    print(e1_n + ": " + bd_1)
    print(e2_n + ": " + bd_2)
    print(e3_n + ": " + bd_3)
    print(e4_n + ": " + bd_4)
    print(" ")

def salary():
    e1_s = "20000"
    e2_s = "5000"
    e3_s = "70000"
    e4_s = "34567"

    print("Salary employees: ") 
    print(e1_n + ": " + e1_s)
    print(e2_n + ": " + e2_s)
    print(e3_n + ": " + e3_s)
    print(e4_n + ": " + e4_s)
    print(" ")

def work():
    e1_w = "Manager"
    e2_w = "Director"
    e3_w = "Cleaner"
    e4_w = "Waiter"
    
    print("Work employees: ")
    print(e1_n + ": " + e1_w)
    print(e2_n + ": " + e2_w)
    print(e3_n + ": " + e3_w)
    print(e4_n + ": " + e4_w)
    print(" ")

name()
age()
born_date()
salary()
work()
  