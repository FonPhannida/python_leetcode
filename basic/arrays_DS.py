# #Arrays - DS - hackerrank
# A = [1,2,3]
# A.sort(reverse=True)
# print(A)


print("Please input total number of array: ")
arr_count = int(input().strip())

arr =[]
print("Please input number one by one: ")
for i in range(arr_count):
     arr.append(int(input().strip()))

print(arr)

arr.sort(reverse=True)
print(arr)















