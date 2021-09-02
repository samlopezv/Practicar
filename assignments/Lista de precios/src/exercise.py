def main():

    c = input('Ingresa la clave A,B,C o X para terminar: ')
    d = 0

    if c == 'A' or c == 'B' or c == 'C' or c =='X':
        while c != 'X':
            if c == 'A':
                e = 120
                print(e)
            elif c == 'B':
                e = 250
                print(e)
            else:
                e = 360
                print (e)

            d = d + e
            c = input('Ingresa la clave A,B,C o X para terminar: ')

        print(str(d))
    else:
        print('ERROR')


if __name__=='__main__':
    main()
