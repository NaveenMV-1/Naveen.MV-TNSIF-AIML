import pandas as pd
data = {
    "Name": ["Arun", "Bala", "Charan", "Deepak", "Karthik", "Rahul", "Vijay", "Surya"],
    "Department": ["CSE", "ECE", "CSE", "IT", "CSE", "ECE", "IT", "CSE"],
    "Marks": [85, 72, 91, 68, 78, 88, 65, 95],
    "Attendance": [90, 75, 85, 92, 78, 88, 70, 96]
}

datas = pd.DataFrame(data)
print(datas)

print("\nFirst 5 Students:")
print(datas.head(5))

print("\nAverage Marks:")
average = datas["Marks"].mean()
print(average)

print("\nStudents who scored more than 75:")
print(df[df["Marks"] > 75])


print("\nStudents whose attendance is below 80%:")
print(df[df["Attendance"] < 80])


print("\nStudents sorted by Marks:")
print(df.sort_values("Marks"))