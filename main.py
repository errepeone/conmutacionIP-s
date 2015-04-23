def CheckInputInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def validarIP(IP):
    valores = IP.split('.')
    enteros = []
    i = 0
    #print(valores)
    #print len(valores)
    if(len(valores) != 4):
        print("IP no valida")
        return False
    else:
        for valor in valores:
            #print valor
            if(CheckInputInt(valor) == True):
                #print valor
                if(int(valor) > 255):
                    print("IP no valida")
                    return False
                elif(int(valor) < 0):
                    print("IP no valida")
                    return False
                else:
                    #print valor
                    enteros.append(int(valor))
            else:
                print("IP no valida")
                return False
        if(len(enteros) == 4):
            return True
        else:
            print("IP no valida")
            return False


def IPtoBin(IP):
    valores = IP.split('.')
    binary = ''
    for c in valores:
        binary += bin(int(c))[2:].zfill(8)
    return binary


def main():
    binary = ''
    type = ''
    IP = raw_input("Inserte una direccion IP: ")
    while(validarIP(IP) != True):
        IP = raw_input("Inserte una direccion IP: ")
    if(validarIP(IP) != False):
        binary += IPtoBin(IP)
        print("R = Red\t\tH = Host")
        if(binary[0] == '0'):
            print("%s.%s.%s.%s") % (binary[0:8], binary[8:16], binary[16:24], binary[24:32])
            print('0' + ('R' * 7) + (('.' + ('H' *8) ) * 3))
            print("IP de Clase A\nFormato Binario")
            print("Red: %s\nHost: %s.%s.%s") % (binary[0:8], binary[8:16], binary[16:24], binary[24:32])
            print("Formato decimal\nRed: %d\nHost: %d.%d.%d") \
                 % (int(binary[0:8],2), int(binary[8:16],2), int(binary[16:24],2), int(binary[24:32],2))
        elif(binary[:2] == '10'):
            print("%s.%s.%s.%s") % (binary[0:8], binary[8:16], binary[16:24], binary[24:32])
            print('10' + ('R' * 6) + '.' + ('R' * 8) + (('.' + ('H' *8) ) * 2))
            print("IP de Clase B\nFormato Binario")
            print("Red: %s.%s\nHost: %s.%s") % (binary[0:8], binary[8:16], binary[16:24], binary[24:32])
            print("Formato decimal\nRed: %d.%d\nHost: %d.%d") \
                 % (int(binary[0:8],2), int(binary[8:16],2), int(binary[16:24],2), int(binary[24:32],2))
        else:
            print("%s.%s.%s.%s") % (binary[0:8], binary[8:16], binary[16:24], binary[24:32])
            print(binary[0:3] + ('R' * 5) + (('.' + ('R' * 8)) * 2) + (('.' + ('H' *8) ) * 1))
            print("IP de Clase C\nFormato Binario")
            print("Red: %s.%s.%s\nHost: %s") % (binary[0:8], binary[8:16], binary[16:24], binary[24:32])
            print("Formato decimal\nRed: %d.%d.%d\nHost: %d") \
                 % (int(binary[0:8],2), int(binary[8:16],2), int(binary[16:24],2), int(binary[24:32],2))


if __name__ == '__main__':
    main()
