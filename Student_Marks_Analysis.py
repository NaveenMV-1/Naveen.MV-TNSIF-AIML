import numpy as np
marks = np.array([[23,43,21],[43,65,34],[98,45,64],[57,98,46],[98,83,54],[87,68,78],[98,65,78],[87,94,35],[75,68,78],[68,75,84]])
print("\nStudent Marks")
print(marks)
print("\nTotal Mark of Each Students:")
total = np.sum(marks, axis = 1)
print(total)

print("\nAverage of Subject: ")
average = np.mean(marks, axis = 0)
print(average)

print("\nAverage of Students Marks: ")
average_student = np.mean(marks,axis = 1)
print(average_student)

print("\nhighest Mark:")
max = np.max(marks)
print(max)

print("\nLowest Mark:")
min = np.min(marks)
print(min)

print("\nMarks greater than 75:")
for i in range(len(average_student)):
    if(average_student[i]>75):
        print("Student: ",i)