import math

def es_bisiesto (a):
        if ( a % 4 == 0 ) and not(a % 100 == 0):
            return 'True'
        elif ( a % 4 == 0 ) and (a % 400 == 0):
                return 'True'
        else:
            return 'False'


def main():
    #escribe tu código abajo de esta línea
    b = int(input('Ingresa un año: '))
    c = es_bisiesto(b)
    print(c)

if __name__=='__main__':
    main()
