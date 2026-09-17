import matplotlib.pyplot as plt
student = ["Student 1","Student 2","Student 3","Student 4","Student 5","Student 6","Student 7","Student 8","Student 9","Student 10",]
marks = [45,78,90,70,67,87,74,86,97,79]  

plt.bar(student,marks)
plt.title("Student Marks")
plt.xlabel("Stuents")
plt.ylabel("Marks")
plt.xticks(rotation=45)

plt.show()


excellent = 0
good = 0
average = 0
needs_improvement = 0

for i in marks:
    if i > 80:
        excellent+=1
    elif i > 60:
        good+=1
    elif i > 40:
        average+=1
    else:
        needs_improvement+=1

categories = ["Excellent", "Good", "Average", "Needs Improvement"]
students_count = [excellent, good, average, needs_improvement]

plt.pie(students_count,labels = categories,  autopct="%1.1f%%")

plt.title("Student Performance Distribution")

plt.show()