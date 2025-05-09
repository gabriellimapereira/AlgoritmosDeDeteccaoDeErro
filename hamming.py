# hamming.py

def calcular_hamming(bits):
    # insere bits de paridade nas potências de 2
    bits = list(bits)
    n = len(bits)
    r = 0
    while (2 ** r) < (n + r + 1):
        r += 1
    res = ['0'] * (n + r)
    j = 0
    for i in range(1, len(res) + 1):
        if not (i & (i - 1)) == 0:
            res[i - 1] = bits[j]
            j += 1
    for i in range(r):
        pos = 2 ** i
        val = 0
        for j in range(1, len(res) + 1):
            if j & pos and j != pos:
                val ^= int(res[j - 1])
        res[pos - 1] = str(val)
    return res

def verificar_hamming(bits):
    # detecta e corrige erro em bits de hamming
    erro = 0
    n = len(bits)
    for i in range(n.bit_length()):
        pos = 2 ** i
        val = 0
        for j in range(1, n + 1):
            if j & pos:
                val ^= int(bits[j - 1])
        if val != 0:
            erro += pos
    if erro:
        bits[erro - 1] = '1' if bits[erro - 1] == '0' else '0'
    return ''.join(bits), erro
