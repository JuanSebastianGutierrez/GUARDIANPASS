from functools import reduce

# Pregunta 1: List Comprehension con condicionales m´ultiples
lista_numeros = list(range(10))
def transform_and_filter(lista_numeros):
    lista_final = [x*3 if x%2 != 0 and x>15 else x*2 if x%2 == 0 and x<10 else x for x in lista_numeros]
    print(f'1. {lista_final}')
transform_and_filter(lista_numeros)

# Pregunta 2: Combinaci´on avanzada de map, filter, y reduce or set
lista = ["hola","mundo","amazonas"]
def unique_characters(lista):
    lista_mapeada = list(map(lambda x: set(x), lista))
    print(f'2. {lista_mapeada}')
unique_characters(lista)

# Pregunta 3: Operaciones complejas con reduce
lista1 =  [[1,2,3],[4,5,6],[7,8,9]]
def flatten_and_multiply(lista):
    lista_aplanada = reduce(lambda x,y : x+y , lista1)
    lista_final = reduce(lambda x,y : x*y , lista_aplanada)
    print(f'3. {lista_final}')
flatten_and_multiply(lista)

# Pregunta 4: Diccionarios con funciones anidadas
employees = {"Juan":{"Salario": 1200, "Horas":8},
             "Maria":{"Salario": 1400, "Horas":7},
             "Sofia":{"Salario": 1500, "Horas":9}}
porcentaje_incremento = 0.1
def salary_increase(employees,porcentaje_incremento):
    employees1 = {k:v["Salario"]+(porcentaje_incremento*v["Salario"]) for k,v in employees.items()}
    print(f'4. {employees1}')
salary_increase(employees,porcentaje_incremento)

# Pregunta 5: Manipulación de submatrices con slicing
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
x = []
def sum_diagonals_matrix(maatriz,x):
    for i in range(1,len(matriz)):
        for j in range(len(matriz[i])-1):
            if i == j + 1:
                x.append(matriz[i][j])
    print(f'5. {sum(x)}')
sum_diagonals_matrix(matriz,x)

#Pregunta 6: Opción múltiple con slicing avanzado 
#Opcion correcta A
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def slice_and_reverse(lst):
    print(f"6. {lst[::3][::-1] + lst[-4:-1]}")
slice_and_reverse(lst)

#Pregunta 7: Opción Múltiple con Dict Comprehension
#Opción correcta D
d = {"a": 1, "bee": 2, "see": 3, "de": 4}
def invert_dict(d):
    print("7.", {v: k for k, v in d.items() if len(k) > 2})
invert_dict(d)