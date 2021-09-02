def main():
    n = int(input('Ingresa la edad a la que se comenzará a dar $10: '))
    d =10

    while d < 1000 :
        n = n+1
        d = d*2
    print(str(n) + ' ' + str(d))



if __name__=='__main__':
    main()
