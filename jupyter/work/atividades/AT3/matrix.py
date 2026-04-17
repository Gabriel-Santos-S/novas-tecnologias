def transpor_matriz(matriz):
    m_transpo = []

    for j in range(len(matriz[0])):
        linha = []
        for i in range(len(matriz)):
            linha.append(matriz[i][j])
            
        m_transpo.append(linha)
    return m_transpo


def  multiplicar_matriz(matriz_a, matriz_b):
    mutiplicado = []

    for i in range(len(matriz_a)):
        linha = []
        for j in range(len(matriz_b[0])):
            soma = 0
            for k in range(len(matriz_a[0])):
                mult = matriz_a[i][k] * matriz_b[k][j]
                soma += mult
            linha.append(soma)
        mutiplicado.append(linha)

    return mutiplicado