def mochila(peso, valor, cap):
    n = len(valor)
    tabla = [[0] * (cap + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for cap in range(1, cap + 1):
            if peso[i-1] <= cap:  
                tabla[i][cap] = max(tabla[i-1][cap], tabla[i-1][cap-peso[i-1]] + valor[i-1])
            else:
                tabla[i][cap] = tabla[i-1][cap]

    res = tabla[n][cap]
    cap = cap
    opc = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == tabla[i-1][cap]:
            continue
        else:
            opc.append(i)
            res -= valor[i-1]
            cap -= peso[i-1]

    opc.reverse()
    return tabla[n][cap], opc

if __name__ == "__main__":

    peso = [2, 3, 4, 5]
    valor  = [3, 4, 5, 6]
    cap = 5
    print("Ejemplo 1:", mochila(peso, valor, cap))

    peso = [1, 2, 3, 4]
    valor  = [1, 6, 10, 12]
    cap = 5
    print("Ejemplo 2:", mochila(peso, valor, cap))

    peso = [4, 3, 2, 1]
    valor  = [5, 4, 3, 1]
    cap = 6
    print("Ejemplo 3:", mochila(peso, valor, cap))
