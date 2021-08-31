def main():
    #escribe tu código abajo de esta línea
    n = int(input('Ingresa un número: '))
    x = 0
    y = 0

    while x < (n-1) :
        x = x+1
        if n % x == 0 : 
            y = y + x


    if y == n:
        print('El numero es perfecto')

    else:
        print ('El número no es perfecto')







if __name__=='__main__':
    main()
