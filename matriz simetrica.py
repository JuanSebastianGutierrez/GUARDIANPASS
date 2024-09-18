matriz = [[0,2,1],
          [2,0,3],
          [1,3,0]]

def simetria_matriz():
    indices_distintos= {}
    for i in range(1,len(matriz)):
        for j in range(i):
            if matriz[i][j] != matriz[j][i]:
                indices_distintos[i,j] = matriz[i][j]
    return indices_distintos
simetria_matriz