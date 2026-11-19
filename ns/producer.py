# producer.py - Quem ENVIA (ex: seu site, seu e-commerce)
from broker import broker

class Producer:
    def __init__(self, nome):
        self.nome = nome

    def enviar(self, topico, dados):
        print(f"[{self.nome}] 🚀 Publicando em '{topico}'...")
        return broker.publicar(topico, dados)

# Exemplo de uso real
if __name__ == "__main__":
    # Simulando seu sistema de filmes / e-commerce
    app = Producer("CineFlow-API")

    app.enviar("pedido_pago", {
        "pedido_id": 101,
        "usuario": "maria@gmail.com",
        "valor": 49.90,
        "filme": "Duna 2"
    })

    app.enviar("usuario_cadastrado", {
        "usuario": "joao@gmail.com",
        "nome": "João"
    })