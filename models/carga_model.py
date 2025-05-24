class CargaModel:
    def __init__(self, nome, peso, destino):
        self.nome = nome
        self.peso = peso
        self.destino = destino

    def to_dict(self):
        return {
            "nome": self.nome,
            "peso": self.peso,
            "destino": self.destino
        }
