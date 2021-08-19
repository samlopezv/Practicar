import math

def main():
    #escribe tu código abajo de esta línea
    x1=float(input('X1: '))
    y1=float(input('y1: '))
    x2=float(input('x2: '))
    y2=float(input('y2: '))

    d = round((math.hypot(x2-x1, y2-y1)),2)

    print(f'La distancia es: {d}')


if __name__=='__main__':
    main()
