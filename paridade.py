def inverteBit(numero, posicao):  # direita pra esquerda começando em zero
    return numero ^ (1 << posicao)

def contaUm(numero):
    return int(bin(numero).count('1'))

def adicionaBit(msg, bitsUm):
    if bitsUm % 2 == 0:
        return (msg << 1) | 0
    else:
        return (msg << 1) | 1
    
def verificaParidade(msg, msg_result):
    if ((msg & 1) == (msg_result & 1)):
        print("houve erro!")
    else:
        print("a mensagem não sofreu alteração")

msg = 2775  # 101011010111 em binário
msg = adicionaBit(msg, contaUm(msg)) # adiciona bit de paridade
msg_alt = adicionaBit(msg, contaUm(msg)) # adiciona nova paridade
msg_alt = inverteBit(msg, 1) # inverte o penúltimo bit
verificaParidade(msg, msg_alt)

msg = msg >> 1
msg_alt = msg_alt >> 1
print("original:", bin(msg)[2:], "-", msg)
print("alterado:", bin(msg_alt)[2:], "-", msg_alt)