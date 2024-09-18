#punto 5 
matriz = ((1,2,3),
          (4,5,6),
          (7,8,9))
def sum_diagonals(matriz):
    j = 0
    i = 0
    num = 0
    num1 = 0
    k = -1
    for x in matriz:
        num += matriz[i][j]
        num1 += matriz[i][k]
        j += 1
        i += 1
        k -= 1
    print(num, num1)
sum_diagonals(matriz)

#punto 6 
lst = [1,3,4,6,7,9]
def mystery_function(lst):
    return [x*2 for x in lst if x % 3 != 0]
print(mystery_function(lst))

#punto 7
lst = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
def advanced_slicing(lst):
    return lst[:5:2] + lst[5::2]

print(advanced_slicing(lst))