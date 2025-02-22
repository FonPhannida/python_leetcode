# s = set('HelloWorld')
# s.add('H')
# s.add('B')
# print("Return: ", s) #return as set
# print("Return: "+str(s)) #string

# set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
# print(s.add('HelloWorld'))
# print(s)
# print(set(['a', 'c', 'e', 'HelloWorld', 'H', 'k', 'n', 'r', 'R']))


print("Please input total number of country stamps: ")
num = int(input().strip())
country = set()
print("Please input country stamps one by one: ")
for i in range(num):
    country_name = input().strip()
    country.add(country_name.lower())

print("Total unique country stamps:", len(country))
