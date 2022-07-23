def es_palisandro(N):
    N=str(N)
    return N == N[::-1]

N=int(input("Ingrese el número a evaluar:"))

if es_palisandro(N):
    print(bool(1))
else:
    print(bool(0))
