def intervalo_mas_cercano(A, q):
    def buscar(A, inicio, fin):
        if inicio == fin:
            valor = A[inicio]
            if valor <= q:
              menor = (valor, inicio)
            else:
              menor = (0, 0)
            if valor >= q:
              mayor = (valor, inicio)
            else:
              mayor = (0, 0)
            return menor, mayor

        medio = (inicio + fin) // 2
        menor_izq, mayor_izq = buscar(A, inicio, medio)
        menor_der, mayor_der = buscar(A, medio + 1, fin)

        if menor_izq[0] >= menor_der[0]:
            menor = menor_izq
        else:
            menor = menor_der

        if mayor_izq[0] <= mayor_der[0]:
            mayor = mayor_izq
        else:
            mayor = mayor_der
        return menor, mayor

    menor, mayor = buscar(A, 0, len(A) - 1)
    return [menor[1], mayor[1]]

A = [4, 0, 7, 11, 9, 12, 56, 3]
q = 8.13

resultado = intervalo_mas_cercano(A, q)
print("Resultado:", resultado)
