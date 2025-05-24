from models.carga_model import CargaModel
from repositories.carga_repository import CargaRepository

class CargaController:
    def __init__(self):
        self.repo = CargaRepository()

    def listar_cargas(self):
        cargas = self.repo.listar()
        if not cargas:
            print("Nenhuma carga cadastrada ainda.")
            return
        print("\nCargas cadastradas:")
        for idx, carga in enumerate(cargas, 1):
            print(f"{idx}. Nome: {carga.nome}, Peso: {carga.peso} kg, Destino: {carga.destino}")

    def adicionar_carga(self):
        print("Adicionando nova carga...")

        while True:
            nome = input("Nome da carga: ").strip()
            if nome:
                break
            print("Nome não pode ser vazio. Tente novamente.")

        while True:
            try:
                peso = float(input("Peso da carga (kg): "))
                if peso > 0:
                    break
                else:
                    print("Peso deve ser maior que zero.")
            except ValueError:
                print("Peso inválido. Digite um número.")

        while True:
            destino = input("Destino da carga: ").strip()
            if destino:
                break
            print("Destino não pode ser vazio. Tente novamente.")

        nova_carga = CargaModel(nome, peso, destino)

        try:
            self.repo.adicionar(nova_carga)
            print("Carga adicionada com sucesso!")
        except ValueError as e:
            print(str(e))
