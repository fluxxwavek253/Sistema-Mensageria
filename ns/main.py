# main.py - Roda o sistema completo
from producer import Producer
from consumer import Consumer, enviar_email_confirmacao, dar_baixa_estoque, enviar_email_boas_vindas
import time

print("=== 🚀 MINI MENSAGERIA INICIADA ===\n")

# 1. Cria os consumidores (eles ficam esperando)
# Mesmo tópico, 2 consumidores diferentes = Pub/Sub
c1 = Consumer("Serviço-Email", "pedido_pago", enviar_email_confirmacao)
c2 = Consumer("Serviço-Estoque", "pedido_pago", dar_baixa_estoque)
c3 = Consumer("Serviço-Usuarios", "usuario_cadastrado", enviar_email_boas_vindas)

c1.iniciar()
c2.iniciar()
c3.iniciar()

time.sleep(1)

# 2. Produtor envia - ele NÃO espera ninguém!
api = Producer("CineFlow-API")

print("\n--- Usuário comprando filme (API responde na hora) ---")
api.enviar("pedido_pago", {"pedido_id": 101, "usuario": "maria@gmail.com", "valor": 49.90, "filme": "Duna 2"})
print(">>> API já respondeu 'Pedido Confirmado!' sem esperar e-mail/estoque\n")

time.sleep(1)

api.enviar("usuario_cadastrado", {"usuario": "joao@gmail.com", "nome": "João"})
api.enviar("pedido_pago", {"pedido_id": 102, "usuario": "ana@gmail.com", "valor": 19.90, "filme": "Interestelar"})

# Deixa os consumidores terminarem
print("\n--- Aguardando consumidores processarem em background... ---")
time.sleep(4)
print("\n=== FIM ===")