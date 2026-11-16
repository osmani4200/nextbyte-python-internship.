#variables
name="usman"
age=22
cgpa=3.47
is_student=True

#Variables Printing
print(name)
print(age)
print(cgpa)
print(is_student)

#Variables Datatypes
print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

#User Input
DOB = input("Enter Your Date of Birth:")


print("Your DOB is:",DOB)
print(type(DOB))

#MINI ASSIGNMENT STUDENT INFORMATION
FullName=input("Enter your full name:")
Age = input("Enter your Age:")
Institute=input("Enter your Institute name:")
GPA=input("Enter your GPA:")

print("NAME:",FullName)
print("AGE", Age)
print("INSTITUTE",Institute)
print("GPA", GPA)

# ARITHMETIC OPERATORS
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

#COMPERISON OPERATORS
a = 20
b = 10

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#LOGICAL OPERATORS
age = 22
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)

#MINI ASSIGNMENT
age=int(input("Enter your age:"))
GPA=float(input("Enter your GPA:"))
Degree_completed= True

Eligibility= age >=18 and GPA >=1.5 and Degree_completed
print("ELIGIBILITY:", Eligibility)

#CONDITIONS
age=int(input("Enter your age:"))
if age < 18:
    print("You are not-adult",)
elif age>=18:
    print("You are adult")
else:
    print("paida hoky aou")