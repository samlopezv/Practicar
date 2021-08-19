import math

def main():
    #escribe tu código abajo de esta línea
    a= float(input('Ancho: '))
    l = float(input('Largo: '))

    d = math.hypot(a,l)
    
    print(f'La diagonal es: {d}')

    print('La diagonal es: ' + str((math.hypot(a,l) )))


if __name__=='__main__':
    main()
