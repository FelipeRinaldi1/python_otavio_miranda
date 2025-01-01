"""
Constante = variavies q nao mudam
*Muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)
"""

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1 

velocidade = 61 #velocidade atual do carro
local_carro = 99 #local em que o carro esta na estrada

velocidade_carro_maior_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (local_carro - RADAR_RANGE) \
and local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1= carro_passou_radar_1 and velocidade_carro_maior_radar_1


if velocidade_carro_maior_radar_1:
    print("Velocidade carro passou do radar 1")
if carro_passou_radar_1:
    print("Carro passou o radar 1")