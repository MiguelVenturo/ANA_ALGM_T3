print("--->BIENVENIDOS AL LABERINTO DE CHAVIN<---")
lab = [
    [1, 1, 1, 3, 0, 1, 1, 1, 4],  
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    [1, 1, 3, 1, 0, 1, 1, 1, 1]   
]

res = [[0 for _ in range(9)] for _ in range(9)]

def imprime(mat):
    for fila in mat:
        for val in fila:
            print(f"{val}", end=" ")
        print()
    print()

def valida(fil, col) -> bool:
    if fil < 0 or col < 0 or fil >= len(lab) or col >= len(lab[0]):
        return False
    if lab[fil][col] == 0:
        return False
    if res[fil][col] == 1:
        return False
    return True

def labbas(fil, col, puntos) -> bool:
    if fil == 0 and col == 0:
        if valida(fil, col):
            puntos += lab[fil][col] if lab[fil][col] in (3, 4) else 0
            if puntos >= 23:
                res[fil][col] = 1
                imprime(res)
                return True
        return False

    if valida(fil, col):
        res[fil][col] = 1
        puntos += lab[fil][col] if lab[fil][col] in (3, 4) else 0

        if labbas(fil - 1, col, puntos):   
            return True
        if labbas(fil, col + 1, puntos):   
            return True
        if labbas(fil + 1, col, puntos):   
            return True
        if labbas(fil, col - 1, puntos):   
            return True

        res[fil][col] = 0  
        return False

    return False


print("Laberinto original:")
imprime(lab)

if labbas(8, 0, 0):
    print("¡El raton Salió del laberinto!")
else:
    print("No hay salida válida con al menos 23 puntos.")
