print("--->BIENVENIDOS AL LABERINTO CHAVIN<---")
laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 3, 1, 1, 1],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 3, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 4],
    [1, 3, 1, 0, 1, 1, 1, 1, 'I']
]


def valor_celda(x):
    if x in ['F', 'I', 1]:
        return 1
    if x == 3 or x == 4:
        return x
    return 0


def imprimir_laberinto(lab, path=None):
    for i, fila in enumerate(lab):
        for j, x in enumerate(fila):
            if path and (i, j) in path:
                print("\033[92m*\033[0m", end=" ")  
            elif x == 0:
                print("x", end=" ")                  
            elif x == 'F':
                print("\033[91mF\033[0m", end=" ")   
            elif x == 'I':
                print("\033[94mI\033[0m", end=" ")   #
            else:
                print(str(x), end=" ")
        print()
    print()

def backtrack(x, y, suma, visitados, path):
    if laberinto[x][y] == 'F':
        if suma >= 23:
            path.append((x, y))
            return True
        return False
    visitados[x][y] = True
    path.append((x, y))
    for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
        nx, ny = x+dx, y+dy
        if 0<=nx<9 and 0<=ny<9 and laberinto[nx][ny]!=0 and not visitados[nx][ny]:
            val = valor_celda(laberinto[nx][ny])
            if backtrack(nx, ny, suma+val, visitados, path):
                return True
    visitados[x][y] = False
    path.pop()
    return False


for i in range(9):
    for j in range(9):
        if laberinto[i][j] == 'I':
            xi, yi = i, j
        if laberinto[i][j] == 'F':
            xf, yf = i, j

print("Laberinto original:\n")
imprimir_laberinto(laberinto)

visitados = [[False]*9 for _ in range(9)]
camino = []
if backtrack(xi, yi, valor_celda('I'), visitados, camino):
    print("¡Se encontró un camino! El ratón logra salir \n")
    imprimir_laberinto(laberinto, set(camino))
else:
    print("No hay camino posible")

