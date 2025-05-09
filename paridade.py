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

