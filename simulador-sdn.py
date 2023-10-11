import psutil
import time

# Função para obter a largura de banda atual de uma interface de rede em Mbps
def obter_largura_banda():
    # Nome da interface de rede (pode variar dependendo do seu sistema)
    interface = "Ethernet"  # Substitua pelo nome da sua interface
    
    # Obtém as estatísticas de rede
    estatisticas_rede = psutil.net_io_counters(pernic=True).get(interface, None)
    
    if estatisticas_rede:
        # Largura de banda de entrada em bytes por segundo
        largura_banda_entrada = estatisticas_rede.bytes_recv
        
        # Largura de banda de saída em bytes por segundo
        largura_banda_saida = estatisticas_rede.bytes_sent
        
        # Converte para Mbps
        largura_banda_entrada_mbps = largura_banda_entrada * 8 / 1e6
        largura_banda_saida_mbps = largura_banda_saida * 8 / 1e6
        
        return largura_banda_entrada_mbps, largura_banda_saida_mbps
    else:
        return None, None

# Função para redirecionar o tráfego com base na largura de banda
def redirecionar_trafego(largura_banda_entrada, largura_banda_saida):
    if largura_banda_entrada < 50 or largura_banda_saida < 50:
        print("Redirecionando tráfego para um caminho alternativo...")
    else:
        print("Largura de banda adequada. Não é necessário redirecionamento.")

# Loop de simulação para monitoramento contínuo
while True:
    # Chama a função para obter a largura de banda
    largura_banda_entrada, largura_banda_saida = obter_largura_banda()
    
    # Verifica se as informações de largura de banda foram obtidas corretamente
    if largura_banda_entrada is not None and largura_banda_saida is not None:
        # Exibe a largura de banda atual
        print(f"Largura de banda de entrada: {largura_banda_entrada:.2f} Mbps")
        print(f"Largura de banda de saída: {largura_banda_saida:.2f} Mbps")
        
        # Chama a função para redirecionar o tráfego com base na largura de banda
        redirecionar_trafego(largura_banda_entrada, largura_banda_saida)
    else:
        # Exibe uma mensagem se não for possível obter informações de largura de banda
        print("Não foi possível obter informações de largura de banda.")
    
    # Aguarda 5 segundos antes da próxima medição
    time.sleep(5)
