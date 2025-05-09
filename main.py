from checksum import calcular_checksum, verificar_checksum
from hamming import calcular_hamming, verificar_hamming
from crc import calcular_crc, verificar_crc
import paridade

# mensagem original
msg = 182  # binário: 10110110
print("original:", bin(msg)[2:], "-", msg)

# checksum
dados = [msg]
chk = calcular_checksum(dados)
dados_alt = [183]  # erro simulado
print("\nchecksum:")
print("válido?", verificar_checksum(dados, chk))
print("com erro?", verificar_checksum(dados_alt, chk))

# hamming
bits = bin(msg)[2:].zfill(8)
hamming = calcular_hamming(bits)
hamming[-2] = '1' if hamming[-2] == '0' else '0'  # inverte penúltimo bit
corrigido, pos = verificar_hamming(hamming)
print("\nhamming:")
print("mensagem corrigida:", corrigido)
print("erro detectado na posição:", pos)

# crc
mensagem = bin(msg)[2:].zfill(8)
crc = calcular_crc(mensagem)
mensagem_crc = list(mensagem) + crc
mensagem_crc[-2] = '1' if mensagem_crc[-2] == '0' else '0'  # inverte penúltimo bit
print("\ncrc:")
print("válido?", verificar_crc(list(mensagem) + crc))
print("com erro?", verificar_crc(mensagem_crc))

# paridade
print("\nparidade:")
msg_com_paridade = paridade.adicionaBit(msg, paridade.contaUm(msg))
msg_alt = paridade.inverteBit(msg_com_paridade, 1)  # inverte penúltimo bit
paridade.verificaParidade(msg_com_paridade, msg_alt)

# exibição dos valores finais
msg_sem_paridade = msg_com_paridade >> 1
msg_alt_sem_paridade = msg_alt >> 1
print("original:", bin(msg_sem_paridade)[2:], "-", msg_sem_paridade)
print("alterado:", bin(msg_alt_sem_paridade)[2:], "-", msg_alt_sem_paridade)

