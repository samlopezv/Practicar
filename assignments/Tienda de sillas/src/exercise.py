import math

def silla(s):
    if s == 'B':
        return int(700)
    elif s == 'E':
        return int(900)
    elif s == 'L':
        return int(1500)


def cielnte(c):
    if c == 'F':
       return 0.2
    elif c == 'N':
        return 0
   
def descu(d):
    if (d >= 10000) and (d <20000):
        return 0.10
    elif d>= 20000:
        return 0.15
    else:
        return 0
        

def main():
    #Preguntas
    s = input('Tipo de silla B(básica), E(estándar), L(lujo): ')
    c = input('Ingresa el tipo de cliente F(frecuente) o N(normal): ')
    tot = int(input('Cantidad de sillas: '))

    #Precio normal
    silla (s)
    total = s*tot

    #Descuento de compra
    d = float(total)
    descu(d)
    desc1 = total*d
    totaldesc1 = total - desc1


    #Descuento cliente
    cliente (c)
    desc2 = totaldesc1*c
    totaldesc2 = totaldesc1 - desc2

    #Suma descuentos
    desctotal = desc1 + desc2

    comprob = total - desctotal



    #Resultados
    print(f'Precio antes del descuento: {total}')
    print(f'Descuento: {desctotal}')
    print(f'Total a pagar: {totaldesc2}')
    print(f'Comprobación {comprob}')



  


if __name__=='__main__':
    main()
