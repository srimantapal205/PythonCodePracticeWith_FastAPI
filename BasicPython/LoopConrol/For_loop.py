"""
For Loop Example
"""
myList = [1, 2, 3, 4, 5]
for i in myList:
    print(i)
print('--------------')
for  i in range(3, 6):
    print(i)

print('-------Sum of loop-------')

sum_of_for_loop = 0

for i in myList:
    sum_of_for_loop += i
    print(sum_of_for_loop)
    print('--')
print(sum_of_for_loop)

print('-------Sum of range loop-------')
r_sum = 0
for i in range(1, 6):
    r_sum += i
    print(r_sum)
print(r_sum)
print('------------------')

print('----------String operation------------')
strLst = ['A', 'B', 'C', 'D', 'E']
for i in strLst:
    print(i)
print('------------------')
for i in strLst:
    print(i)
    i = 'X'
