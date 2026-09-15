# 1. Reverse an Array

arr1 = [10,20,30,40,50]
left = 0
right = len(arr1)-1
while left < right:
    temp = arr1[left]
    arr1[left] = arr1[right]
    arr1[right] = temp

    left += 1
    right -= 1
print(arr1)

# 2. Count Even, Odd and Zero

arr2 = [10, 5, 0, 7, 8, 0, 13, 4]
even = 0
odd = 0
zero = 0

for i in range(0,len(arr2)):
    if(arr2[i]!=0):
        if(arr2[i]%2==0):
            even += 1
        elif(arr2[i]%2==1):
            odd += 1
    elif(arr2[i] == 0):
        zero += 1
print(even)
print(odd)
print(zero)

# 3. Sum of Positive and Negative Numbers

arr3 = [10, -5, 20, -8, 15, -2]

positive = 0
negative = 0

for i in range(len(arr3)):

    if arr3[i] > 0:
        positive += arr3[i]

    elif arr3[i] < 0:
        negative += arr3[i]

print(positive)
print(negative)

# 4. Remove Duplicate Elements 

arr = [10, 20, 10, 30, 20, 40, 30]

result = []

for i in range(len(arr)):

    found = False

    for j in range(len(result)):
        if arr[i] == result[j]:
            found = True
            break

    if found == False:
        result.append(arr[i])

print(result)

# 5. Find the Missing Number 

arr = [1, 2, 3, 5, 6, 7]

n = 7

for i in range(1, n + 1):

    found = False

    for j in range(len(arr)):
        if arr[j] == i:
            found = True
            break

    if found == False:
        print("Missing Number:", i)
        break

# 6. Rotate an Array 

arr = [1, 2, 3, 4, 5]
k = 2

for i in range(k):
    last = arr[len(arr) - 1]

    for j in range(len(arr) - 1, 0, -1):
        arr[j] = arr[j - 1]

    arr[0] = last

print(arr)

# 7. Find the Most Frequent Element

arr = [2, 5, 2, 8, 5, 2, 3, 5, 2]

max_frequency = 0
most_frequent = 0

for i in range(len(arr)):

    frequency = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            frequency += 1

    if frequency > max_frequency:
        max_frequency = frequency
        most_frequent = arr[i]

print("Most Frequent Element:", most_frequent)
print("Frequency:", max_frequency)

# 8. Maximum Subarray Sum 

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = arr[0]
max_sum = arr[0]

start = 0
end = 0
temp_start = 0

for i in range(1, len(arr)):

    if arr[i] > current_sum + arr[i]:
        current_sum = arr[i]
        temp_start = i
    else:
        current_sum = current_sum + arr[i]

    if current_sum > max_sum:
        max_sum = current_sum
        start = temp_start
        end = i

print("Maximum Subarray Sum:", max_sum)

print("Subarray:", end=" ")
for i in range(start, end + 1):
    print(arr[i], end=" ")


# 9. Check Whether Two Arrays are Equal 

arr1 = [1, 2, 2, 3, 4]
arr2 = [4, 2, 1, 2, 3]

if len(arr1) != len(arr2):
    print("Arrays are Not Equal")

else:
    equal = True

    for i in range(len(arr1)):

        count1 = 0
        count2 = 0

        for j in range(len(arr1)):
            if arr1[i] == arr1[j]:
                count1 += 1

        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                count2 += 1

        if count1 != count2:
            equal = False
            break

    if equal:
        print("Arrays are Equal")
    else:
        print("Arrays are Not Equal")