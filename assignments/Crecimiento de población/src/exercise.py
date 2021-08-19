import math

def main():
    #escribe tu código abajo de esta línea
    a=int(input('Población inicial: '))
    t=int(input('Tiempo en años: '))
    r=float(input('Tasa de crecimiento: '))

    p = math.trunc (a *(math.pow(math.e , t*r)))

    print(f'La población será: {p}')


if __name__=='__main__':
    main()
