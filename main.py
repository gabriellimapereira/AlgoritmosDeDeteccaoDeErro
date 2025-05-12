import time
from checksum import calcular_checksum, verificar_checksum
from hamming import calcular_hamming, verificar_hamming
from crc import calcular_crc, verificar_crc
import paridade

# Função para calcular o tempo total
def medir_tempo(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

# 6 mensagens para testar
mensagens = [
    (0b10110110, 0b10110111),  # 1011.0110 -> 1011.0111 (erro)
    (0b11001001, 0b11001111),  # 1100.1001 -> 1100.1111 (erro)
    (0b10000000, 0b10001101)   # 1000.0000 -> 1000.1101 (erro)
]

# Inicializa variáveis para tempo total
tempo_checksum = 0
tempo_hamming = 0
tempo_crc = 0
tempo_paridade = 0

# Repetir um milhão de vezes e calcular o tempo
for i in range(1_000_000):
    # Paridade
    msg_paridade = mensagens[i % 3][0]
    msg_paridade_erro = mensagens[i % 3][1]
    _, tempo_paridade_exec = medir_tempo(paridade.verificaParidade, msg_paridade, msg_paridade_erro)
    tempo_paridade += tempo_paridade_exec

    # Checksum
    dados = [msg_paridade]
    dados_alt = [msg_paridade_erro]
    _, tempo_checksum_exec = medir_tempo(verificar_checksum, dados, calcular_checksum(dados))
    tempo_checksum += tempo_checksum_exec

    # Hamming
    bits = bin(msg_paridade)[2:].zfill(8)
    hamming = calcular_hamming(bits)
    _, tempo_hamming_exec = medir_tempo(verificar_hamming, hamming)
    tempo_hamming += tempo_hamming_exec

    # CRC
    mensagem = bin(msg_paridade)[2:].zfill(8)
    crc = calcular_crc(mensagem)
    _, tempo_crc_exec = medir_tempo(verificar_crc, list(mensagem) + crc)
    tempo_crc += tempo_crc_exec

    # Mostrar os resultados apenas na milionésima execução
    # Mostrar os resultados apenas na milionésima execução
if i == 999_999:
    print("\nResultado na milionésima execução:")

    print("\nParidade:")
    paridade_ok = paridade.verificaParidade(msg_paridade, msg_paridade_erro)
    print("mensagem está correta?" if paridade_ok else "houve erro!")

    print("\nChecksum:")
    print("válido?", verificar_checksum(dados, calcular_checksum(dados)))
    print("com erro?", verificar_checksum(dados_alt, calcular_checksum(dados_alt)))

    print("\nHamming:")
    corrigido, pos = verificar_hamming(hamming)
    print("mensagem corrigida:", corrigido)
    print("erro detectado na posição:", pos)

    print("\nCRC:")
    crc_valido = verificar_crc(list(mensagem) + crc)
    print("válido?", crc_valido)
    print("com erro?", verificar_crc(list(mensagem) + crc))

# Exibir o tempo total gasto por cada algoritmo
print("\nTempo total de execução (1 milhão de verificações):")
print(f"Checksum: {tempo_checksum:.5f} segundos")
print(f"Hamming: {tempo_hamming:.5f} segundos")
print(f"CRC: {tempo_crc:.5f} segundos")
print(f"Paridade: {tempo_paridade:.5f} segundos")
