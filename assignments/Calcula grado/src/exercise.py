import math

def calcula_grado (n):
    if n >= 0 and n<= 1 :
        if n > 0.9:
            return 'A'
        elif n > 0.8:
            return 'B'
        elif n > 0.7:
            return 'C'
        elif n > 0.6:
            return 'D'
        elif n <= 0.6:
            return 'F'
    else:
        return 'Score incorrecto'

def main():
    #escribe tu código abajo de esta línea
    n = float(input('Ingresa un número entre 0 y 1: '))
    print(calcula_grado(n))


if __name__=='__main__':
    main()
