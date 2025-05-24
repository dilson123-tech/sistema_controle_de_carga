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
        print()

    def adicionar_carga(self):
        print("Adicionando nova carga...")

        while True:
            nome = input("Nome da carga (ou 'sair' para voltar): ").strip()
            if nome.lower() == 'sair':
                print("Voltando ao menu principal.")
                return
            if nome:
                break
            print("Nome não pode ser vazio. Tente novamente.")

        while True:
            try:
                peso = float(input("Peso da carga (kg): "))
                if peso > 0:
                    break
                print("Peso deve ser maior que zero.")
            except ValueError:
                print("Peso inválido. Digite um número.")

        while True:
            destino = input("Destino da carga (ou 'sair' para voltar): ").strip()
            if destino.lower() == 'sair':
                print("Voltando ao menu principal.")
                return
            if destino:
                break
            print("Destino não pode ser vazio. Tente novamente.")

        nova_carga = CargaModel(nome, peso, destino)
        try:
            self.repo.adicionar(nova_carga)
            print("Carga adicionada com sucesso!")
        except ValueError as e:
            print(str(e))

    def deletar_carga(self):
        cargas = self.repo.listar()
        if not cargas:
            print("Nenhuma carga cadastrada para deletar.")
            return

        print("\nCargas cadastradas:")
        for idx, carga in enumerate(cargas, 1):
            print(f"{idx}. Nome: {carga.nome}, Peso: {carga.peso} kg, Destino: {carga.destino}")
        print()

        try:
            indice = int(input("Digite o número da carga que deseja excluir: ")) - 1
            if 0 <= indice < len(cargas):
                carga_escolhida = cargas[indice]
                confirm = input(f"Tem certeza que deseja excluir '{carga_escolhida.nome}'? (s/n): ").lower()
                if confirm == 's':
                    self.repo.remover(indice)
                    print("Carga excluída com sucesso.")
                else:
                    print("Ação cancelada.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
