import numpy

a = numpy.array([1, 2, 3, 4, 5])
print(a[1])

b = numpy.array([1, 2, 3], float)
print(b[2])

# task: print a reversed NumPy array with the element type float
numbers = numpy.array([1, 2, 3, 4, -8, -10], float)
reversed_number = numbers[::-1]
print(reversed_number)

number = [1, 2, 3, 4, -8, -10]


def reversed_number(number):

    num = numpy.array(number, float)
    # print(num)
    reversed_num = num[::-1]
    # print(reversed_num)

    return reversed_num


reversed_number(numbers)
