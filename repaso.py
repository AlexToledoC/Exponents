def run():
    LIMIT = 10000
    
    contador = 0
    exponent = 2 ** contador
    while exponent < LIMIT:
        print("2 elevado a " + str(contador) + " es igual a " + str(exponent))
        contador += 1
        exponent = 2 ** contador


if __name__ == '__main__':
    run()