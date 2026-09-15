import numpy as np
marks = np.array([[23,43,21],[43,65,34],[98,45,64],[57,98,46],[98,83,54]])
print("\nStudent Marks")
print(marks)

print("\nAverage of Subject: ")
average = np.mean(marks, axis = 0)

print(average)

print("\nAverage of Students Marks: ")
