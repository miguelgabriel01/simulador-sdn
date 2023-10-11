# Teoria: Redirecionamento em SDN

Em SDN, o redirecionamento de tráfego é uma prática fundamental que visa otimizar
o fluxo de dados na rede. A SDN separa o plano de controle do plano de dados, 
permitindo que decisões de roteamento e redirecionamento sejam tomadas de forma 
mais dinâmica e centralizada.
Quando se trata de redirecionamento de tráfego, o controlador SDN desempenha um 
papel crucial. Ele monitora a rede, coleta informações de largura de banda, latência,
carga e outras métricas, e com base nessas informações, pode decidir redirecionar o tráfego
para rotas alternativas ou dispositivos que possam oferecer um melhor desempenho.
Essas decisões de redirecionamento podem ser tomadas por meio de políticas definidas 
por operadores de rede ou algoritmos de otimização. Por exemplo, se um link estiver congestionado, 
o controlador SDN pode redirecionar o tráfego para um caminho menos congestionado.

# Código:

O código simula o monitoramento da largura de banda de uma interface de rede em um ambiente de rede fictício.
Ele gera valores aleatórios de largura de banda de entrada e saída a cada 5 segundos e, com base nessas simulações,
decide se o tráfego deve ser redirecionado.

psutil: É uma biblioteca em Python que fornece informações do sistema, incluindo estatísticas de rede, como a largura de banda.

# Saída:

![image](https://github.com/miguelgabriel01/simulador-sdn/assets/49694646/e996fa4d-87ac-4ce1-83e6-239d4e447f8b)

# Explicação:

## Largura de banda de entrada e saída:

A largura de banda de entrada e saída é simulada em Megabits por segundo (Mbps). É uma medida da velocidade de transmissão
de dados na rede.

## Redirecionamento de tráfego:

Com base na largura de banda simulada:
Se a largura de banda de entrada ou saída for inferior a 50 Mbps, o código imprime "Redirecionando tráfego para um caminho 
alternativo...". Isso indica que, em uma situação real, quando a largura de banda está baixa, pode ser necessário redirecionar
o tráfego para evitar congestionamentos.
Se a largura de banda for 50 Mbps ou mais, o código imprime "Largura de banda adequada. Não é necessário redirecionamento.".
Isso reflete que, se a largura de banda está boa, não há necessidade de redirecionar o tráfego.

## Relação com SDN (Redes Definidas por Software):

Na prática, nas redes definidas por software (SDN), a capacidade de monitorar a largura de banda em tempo real é fundamental.
Os controladores SDN podem usar informações de largura de banda, entre outras, para tomar decisões dinâmicas, como redirecionar
o tráfego para otimizar a rede e garantir um desempenho ideal.
Portanto, o código e a saída estão simulando um cenário onde a largura de banda é monitorada e decisões são tomadas com base nessa
largura de banda simulada, o que é relevante para o gerenciamento dinâmico de redes, um princípio fundamental nas Redes Definidas 
por Software (SDN).



