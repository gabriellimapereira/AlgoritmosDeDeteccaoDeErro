# checksum.py

def calcular_checksum(dados):
    # soma todos os bytes e retorna o complemento de 8 bits
    soma = sum(dados)
    checksum = (~soma) & 0xFF
    return checksum

def verificar_checksum(dados, checksum):
    # verifica se soma dos dados + checksum = 0xFF
    return ((sum(dados) + checksum) & 0xFF) == 0xFF
