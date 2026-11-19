# consumer.py - Quem RECEBE e processa (roda em background)
from broker import broker
import threading
import time

class Consumer:
    def __init__(self, nome, topico, funcao_processar):
        self.nome = nome
        self.topico = topico
        self.funcao = funcao_processar
        self.rodando = False

    def iniciar(self):
        self.rodando = True
        # Roda em thread separada pra não travar o sistema
        thread = threading.Thread(target=self._loop, daemon=True)
        thread.start()
        print(f"[{self.nome}] 👀 Ouvindo tópico '{self.topico}'...")

    def _loop(self):
        while self.rodando:
            msg = broker.consumir(self.topico)
            if msg:
                print(f"[{self.nome}] ⚙️ Processando: {msg['dados']}")
                try:
                    self.funcao(msg['dados'])
                    print(f"[{self.nome}] ✅ Concluído!")
                except Exception as e:
                    print(f"[{self.nome}] ❌ Erro: {e} - mensagem ficaria na DLQ")
            else:
                time.sleep(0.5) # Espera um pouco se fila vazia

    def parar(self):
        self.rodando = False

# --- Funções reais que seriam outros serviços ---

def enviar_email_confirmacao(dados):
    time.sleep(1) # Simula envio demorado
    print(f"   -> 📧 E-mail enviado para {dados['usuario']} - Pedido {dados['pedido_id']}")

def dar_baixa_estoque(dados):
    time.sleep(0.5)
    print(f"   -> 📦 Estoque atualizado para filme: {dados['filme']}")

def enviar_email_boas_vindas(dados):
    print(f"   -> 👋 Boas-vindas para {dados['nome']} ({dados['usuario']})")