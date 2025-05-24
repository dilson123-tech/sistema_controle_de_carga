class CargaModel:
    def __init__(self, nome: str, peso: float, destino: str):
        self.nome = nome
        self.peso = peso
        self.destino = destino

    def __repr__(self):
        return f"CargaModel(nome='{self.nome}', peso={self.peso}, destino='{self.destino}')"
