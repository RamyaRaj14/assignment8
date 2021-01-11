#Customized Exceptions
class AttendanceShortageException(Exception):
 def __init__(self,atten):
     self.attendance=atten
class IncomeException(Exception):
 def __init__(self,inc):
     self.income=inc
class GPAException(Exception):
 def __init__(self,arg):
     self.cgpa=arg
 
student_attendance=int(input("Enter the  student attendance:"))
parents_income=int(input("Enter the  parent's income:"))
students_CGPA=int(input("Enter the  students CGPA:"))
if student_attendance<75:
 raise AttendanceShortageException("student attendance is less than 75")
elif parents_income>500000:
 raise IncomeException("parents income is higher than 500000")
elif students_CGPA<7:
 raise GPAException("students CGPA is less than 7")

else:
 print("bye")
