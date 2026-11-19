# broker.py - O intermediário (igual RabbitMQ/Kafka simplificado)
import queue
import threading
import time
import json

class Broker:
    def __init__(self):
        # Um dicionário: cada tópico tem sua própria fila
        # Ex: {"pedido_pago": [msg1, msg2], "usuario_cadastrado": [msg3]}
        self.topicos = {}
        self.lock = threading.Lock()

    def publicar(self, topico, mensagem):
        with self.lock:
            if topico not in self.topicos:
                self.topicos[topico] = queue.Queue()
            
            # Adiciona timestamp e id pra rastrear
            envelope = {
                "id": f"{topico}-{time.time()}",
                "topico": topico,
                "timestamp": time.strftime("%H:%M:%S"),
                "dados": mensagem
            }
            self.topicos[topico].put(envelope)
            print(f"[BROKER] 📩 Mensagem recebida no tópico '{topico}': {mensagem}")
            return envelope

    def consumir(self, topico, timeout=1):
        """Tenta pegar uma mensagem, se não tiver retorna None"""
        if topico not in self.topicos:
            return None
        try:
            return self.topicos[topico].get(timeout=timeout)
        except queue.Empty:
            return None

    def tamanho_fila(self, topico):
        if topico not in self.topicos:
            return 0
        return self.topicos[topico].qsize()

# Instância global - todo mundo usa o mesmo broker
broker = Broker()