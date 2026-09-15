import numpy as np 
temperature = np.array([28, 31, 33, 29, 35, 32, 27])

print("\n The average temperature: ")
average = np.mean(temperature)
print(average)

print("Highest Temperature: ")
max = np.max(temperature)
print(max)

print("Lowest Temperature: ")
min= np.min(temperature)
print(min)


for i in range(len(temperature)):
    if(temperature[i]>30):
        print("day:",i)

update = temperature+2
print("\nUpdated Temperature:")
print(update)