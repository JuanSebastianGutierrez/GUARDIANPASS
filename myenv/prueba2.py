from functools import reduce
numeros = [5, 10, 15, 20, 25, 30]
numeros_filtro = list(filter(lambda x: x > 10, numeros))
numeros_multiplicados = list(map(lambda x: x*2, numeros_filtro))
print(numeros_multiplicados)

palabras = ["python", "javascript", "c++", "java"]
palabras_mapeadas = list(map(lambda x: len(x),palabras))
print(palabras_mapeadas)


numeros = [3, -5, 7, -2, 9, -8, 4]
numeros_filtrados = list(filter(lambda x: x < 0, numeros))
numeros_negativos_sumados = reduce(lambda x,y: x+y, numeros_filtrados)
print(numeros_negativos_sumados)

listas = [[1, 2], [3, 4], [5, 6, 7]]
lista_filtrada = reduce(lambda x,y: x+y, listas)
print(lista_filtrada)

numeros = [4, 7, 10, 15, 20]
numeros_ala2 = list(map(lambda x: x**2, numeros))
numeros_filtrados = list(filter(lambda x: x>50, numeros_ala2))
print(numeros_filtrados)

cadenas = ["hola", "mundo", "python"]
cadena_mapeada = list(map(lambda x: x.upper(),cadenas))
print(cadena_mapeada)

numeros = [1, 2, 3, 4, 5, 6]
numeros_pares = list(filter(lambda x: x%2 == 0,numeros))
print(numeros_pares)

listas = [[1, 2, 3], [4, 5], [6, 7, 8]]
lista_mapeada = list(map(lambda x: sum(x), listas))
print(lista_mapeada)

cadenas = ["hola", "mundo", "python"]
cadena_final = list(map(lambda x: len(x),cadenas))
print(cadena_final)

palabras = ["sol", "luna", "estrella", "mar", "nube"]
palabras_filtradas = list(filter(lambda x: len(x) > 3, palabras))
print(palabras_filtradas)

lista = [1,2,3,4,5,6]
lista_final = [x**2 for x in lista if x%2 == 0]
print(lista_final)

names = ["sofia", "Amanda", "Yuly", "maria", "Juan"]
def uppercase_names(names):
    names_filter = list(filter(lambda x: x.istitle(),names))
    names_upper = list(map(lambda x: x.upper(),names_filter))
    print(names_upper)
uppercase_names(names)

lista = ["hola","mundo","python"]
def concatenate_strings(lista):
    lista_final = reduce(lambda x,y: x+y, lista)
    print(lista_final)
concatenate_strings(lista)

product_prices = {"manzana": 1.2, "naranja":0.75, "pera": 1.5}
def expensive_products(product_prices):
    for producto,valor in product_prices.items():
        if valor > 1:
            print(producto)
expensive_products(product_prices)

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
def diagonals_difference(matriz):
    suma1 = 0
    suma2 = 0
    n = len(matriz)
    for i in range(n):
        suma1 = matriz[i][i]
        suma2 = matriz[i][(n-1)-i]
        print(abs(suma1-suma2))
diagonals_difference(matriz)

numeros = [3, 7, 10, 15, 22, 33, 40, 55]
numeros_final = [x**2 for x in numeros if x%2 !=0]
print(numeros_final)

pares = list(range(0, 11, 2))
impares = list(range(1, 11, 2))

pares = list(range(0, 11, 2))
impares = list(range(1, 11, 2))
numeros = [(i,j) for i in pares for j in impares]
print(numeros)

palabras = ["PYTHON", "list", "Comprehension", "EXERCISES", "complexity", "CHALLENGE"]
palabra_final = [x for x in palabras if len(x)>5 and x.isupper()]
print(palabra_final)

palabras_palindromo = ["level", "radar", "hello", "world", "madam", "python", "racecar"]
palabras_final = [x for x in palabras_palindromo if x == x[::-1]]
print(palabras_final)

numeros_enteros = [123, 456, 789, 1010, 2020]
digitos_sumados = [sum(int(y) for y in str(x)) for x in numeros_enteros]
print(digitos_sumados)

palabras_combinacion = ["alpha", "beta", "gamma", "delta"]
palabras_combinadas = [y+x for y in palabras_combinacion for x in palabras_combinacion if y != x]
print(palabras_combinadas)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, -8, 9]]
matriz_transpuesta = [list(fila) for fila in zip(*matriz)]
print(matriz_transpuesta)

n_harmonico = list(range(1,11))
n_harmonico_final = [ 1/x for x in n_harmonico if x%1 == 0]
print(n_harmonico_final)

l = list(range(11))
l1 = [x**2 if x%2 == 0 else x*5 if x%5 == 0 else x**3 for x in l]
print(l1)

l = [0,1,2,3,4,5]
print(l[-1:-5:-1])

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_final = [2*x for x in numeros if x%2 == 0]

lista = list(range(10))
tupla = [(x,x**2) for x in lista]
print(tupla)

frase = "La programación es divertida y desafiante"
numero_vocales = [x  for x in frase if (x == "a" or x == "e" or x == "i" or x == "i" or x == "o" or x == "u")]
print(numero_vocales)

palabras = ["gato", "elefante", "sol", "luz", "universo", "planeta"]
longitud_palabras= [len(x) for x in palabras]
print(longitud_palabras)

palabras = ["árbol", "elefante", "universo", "carro", "oso", "iglesia", "avión"]
palabras_vocal= [x for x in palabras if (x[0] == "a") or (x[0] == "e") or (x[0] == "i") or (x[0] == "o") or (x[0] == "u")]
print(palabras_vocal)

l = list(range(1,10))
l1 = [x**2 if x%2 != 0 else x for x in l]
print(l1)

l = list(range(1,50))
l1 = [x for x in l if x%2 == 0 and x%3 == 0]
print(l1)

palabras = ["hola", "mundo", "sol", "día", "noche", "python", "cielo"]
palabras_final = [x[::-1] if len(x)> 3 else x for x in palabras]
print(palabras_final)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
listas_multiplicadas = [x*y for x,y in zip(lista1,lista2)]
print(listas_multiplicadas)

lista_anidada = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
lista_aplanada = [y for x in lista_anidada for y in x]
print(lista_aplanada)

texto = "programacion en python es divertido"
numero_letras = {x:len(x) for x in texto}
print(numero_letras)

numeros = [1, 2, 3, 4, 5]
numeros_mapeados = list(map(lambda x: x**2, numeros))
print(numeros_mapeados)

numeros = [2,10, 15, 20, 25, 30, 35, 40]
numeros_pares = list(filter(lambda x: x%2==0, numeros))
print(numeros_pares)

numeros = [2, 3, 4, 5]
numeros_producto = reduce(lambda x,y: x*y,numeros)
print(numeros_producto)

numeros = [3, 5, 7, 9, 11, 13]
numeros_map = list(map(lambda x: x**2, numeros))
numeros_filtrados = list(filter(lambda x: x>50,numeros_map))
print(numeros_filtrados)

cadenas = ["python", "javascript", "html", "css", "programacion"]
cadena_mas_larga = reduce(lambda x,y: x if len(x)>len(y) else y,cadenas)
print(cadena_mas_larga)

palabras = ["ordenador", "teclado", "pantalla", "raton", "altavoz"]
palabras_mapeadas = list(map(lambda x: len(x),palabras))
print(palabras_mapeadas)

palabras = ["level", "radar", "world", "madam", "python", "racecar"]
palabras_palindromas = list(filter(lambda x: x == x[::-1],palabras))
print(palabras_palindromas)

numeros = [2, 4, 6, 8, 10]
numeros_mapeados = list(map(lambda x: x**2, numeros))
numeros_reduce = reduce(lambda x,y: x+y,numeros_mapeados)
print(numeros_reduce)

temperaturas_celsius = [0, 20, 37, 100]
temperaturas_farenheit = list(map(lambda x: x *9/5 +32,temperaturas_celsius))
print(temperaturas_farenheit)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_impares = list(filter(lambda x: x%2!=0,numeros))
numeros_mapeados = list(map(lambda x:  x**3, numeros_impares))
print(numeros_mapeados)

employees = {"juan":{"salario": 1500, "horas" : 10},
             "andrea":{"salario": 1000, "horas" : 8},
             "maria":{"salario": 1200, "horas" :90}}
def s_i(employees):
    p = 0.1
    e1 = {k: v["salario"] + (p*v["salario"]) for k,v in employees.items()}
    print(e1)
s_i(employees)

l = [[1,2,3],[4,5],[6,7,8]]
def f_a_m(l):
    l1 = reduce(lambda x,y : x+y,l)
    l2 = reduce(lambda x,y : x*y,l1)
    print(l2)
f_a_m(l)

l = [[1,2,3],
     [4,5,6],
     [7,8,9]]
def s_m_d(l):
    y = 0
    for x in range(1,len(l)):
        for j in range(len(l),-1):
            y =[j][j]
        print(y)
s_m_d(l)