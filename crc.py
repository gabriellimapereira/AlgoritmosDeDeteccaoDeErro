# crc.py

def xor(a, b):
    return ['0' if i == j else '1' for i, j in zip(a, b)]

def calcular_crc(msg, gerador='1001'):
    # realiza a divisão binária usando xor
    msg = list(msg) + ['0'] * (len(gerador) - 1)
    temp = msg[:len(gerador)]
    for i in range(len(msg) - len(gerador) + 1):
        if temp[0] == '1':
            temp = xor(temp, list(gerador))
        temp = temp[1:]
        if i + len(gerador) < len(msg):
            temp.append(msg[i + len(gerador)])
    return temp

def verificar_crc(msg_crc, gerador='1001'):
    # verifica se sobra só 0 após divisão
    temp = msg_crc[:len(gerador)]
    for i in range(len(msg_crc) - len(gerador) + 1):
        if temp[0] == '1':
            temp = xor(temp, list(gerador))
        temp = temp[1:]
        if i + len(gerador) < len(msg_crc):
            temp.append(msg_crc[i + len(gerador)])
    return all(bit == '0' for bit in temp)

