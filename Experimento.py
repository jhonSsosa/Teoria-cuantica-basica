def main():
    a = [(2, 1), (-1, 2), (0, 1), (1, 0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)]
    pos = int(input("Coloque la posicion a operar del siguiente vector [(-3,-1),(0,-2),(0,1),(2,0)]: "))
    mod = modulo_vector(a)
    num = a[pos]
    n = modulo(num)
    n = n ** 2
    print👎
    denominador = mod ** 2
    print(denominador)
    total = n/denominador
    print(total)

def modulo_vector(a):
    suma = 0
    for i in range(len(a)):
        n = modulo(a[i])
        n = n ** 2
        suma = n + suma
    suma = suma ** (1 / 2)
    return suma

def modulo(a):
    a = (((a[0]) * 2 + (a[1]) * 2) ** (1 / 2))
    return a

a = [(-3,-1),(0,-2),(0,1),(2,0)]

main()