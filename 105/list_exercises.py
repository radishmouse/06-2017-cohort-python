# genertate a list of numbers

import random
numbers = []
for n in range(1, 10):
    numbers.append(random.randint(1, 100))

print "\n\n\n"
print "#### sum ####"


print numbers
sum = 0
for n in numbers:
    sum = sum + n

print "sum %d" % sum


print "\n\n\n"
print "#### largest numbers ####"


largest = 0
for n in numbers:
    if n > largest:
        largest = n

print largest

print "\n\n\n"
print "#### smallest ####"


smallest = 1000
for n in numbers:
    if n < smallest:
        smallest = n

print smallest


print "\n\n\n"
print "#### positive numbers ####"

numbers = []
for n in range(1, 10):
    numbers.append(random.randint(-100, 100))
print numbers

for n in numbers:
    if n > 0:
        print n


print "\n\n\n"
print "#### positive numbers II ####"
positives = []
for n in numbers:
    if n > 0:
        positives.append(n)
print positives

print "\n\n\n"
print "#### multiply a list ####"
numbers = []
for n in range(10):
    numbers.append(random.randint(1, 100))
print numbers
factor = random.randint(1, 100)
print "factor: %d" % factor

factored_list = []
for n in numbers:
    factored_list.append(n * factor)
print factored_list

print "\n\n\n"
print "#### multiply vectors ####"
LENGTH_OF_LIST = 3
list1 = []
list2 = []
for n in range(LENGTH_OF_LIST):
    list1.append(random.randint(1, 10))
    list2.append(random.randint(1, 10))
print "%s x %s " % (list1, list2)

products = []
for n in range(len(list1)): # assuming same length list
    product = list1[n] * list2[n]
    products.append(product)
print products

print "\n\n\n"
print "#### matrix addition (2) ####"

NUMBER_OF_MATRICES = 4
LENGTH_OF_LIST = 4
matrices = []

for m in range(NUMBER_OF_MATRICES):
    matrix = []
    for y in range(LENGTH_OF_LIST):
        matrix_element = []
        for x in range(LENGTH_OF_LIST):
            matrix_element.append(random.randint(1, 10))
        matrix.append(matrix_element)
    matrices.append(matrix)

print "%s " % (matrices,)


# create new matrix, all zeros
new_matrix = []
for i in range(LENGTH_OF_LIST):
    new_matrix.append([])
    for j in range(LENGTH_OF_LIST):
        new_matrix[i].append(0)

for matrix in range(len(matrices)):
    print "matrix"
    for row in range(len(matrices[matrix])):
        # print "row %d" % row
        # print matrix[row]
        for col in range(len(matrices[matrix][row])):
            # print "%d %d %d" % (matrix, row, col)
            print "%d %d: %d" % (row, col, new_matrix[row][col])
            print "%d %d: %d" % (row, col, matrices[matrix][row][col])
            new_matrix[row][col] = new_matrix[row][col] + matrices[matrix][row][col]
            # print "%d %d: %d" % (col, row, matrix[col][row])
            # print matrix[row][col]

print new_matrix


print "\n\n\n"
print "#### de-dup is in separate file ####"

print "\n\n\n"
print "#### matrix multiplication ####"

NUMBER_OF_MATRICES = 2
LENGTH_OF_LIST = 2
matrices = []

for m in range(NUMBER_OF_MATRICES):
    matrix = []
    for y in range(LENGTH_OF_LIST):
        matrix_element = []
        for x in range(LENGTH_OF_LIST):
            matrix_element.append(random.randint(1, 10))
        matrix.append(matrix_element)
    matrices.append(matrix)

print "%s " % (matrices,)


# create new matrix, all zeros
new_matrix = []
for i in range(LENGTH_OF_LIST):
    new_matrix.append([])
    for j in range(LENGTH_OF_LIST):
        new_matrix[i].append(1)

for matrix in range(len(matrices)):
    # print "matrix"
    for row in range(len(matrices[matrix])):
        # print "row %d" % row
        # print matrix[row]
        for col in range(len(matrices[matrix][row])):
            # print "%d %d %d" % (matrix, row, col)
            # print "%d %d: %d" % (row, col, matrices[matrix][row][col])
            new_matrix[row][col] = new_matrix[row][col] * matrices[matrix][col][row]
            # print "%d %d: %d" % (col, row, matrix[col][row])
            # print matrix[row][col]

print new_matrix
