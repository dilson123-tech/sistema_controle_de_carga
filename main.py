from controllers.carga_controller import CargaController

def main():
    controller = CargaController()
    print("Bem-vindo ao Sistema de Controle de Carga")

    while True:
        acao = input("Digite uma ação (listar, adicionar, deletar, sair): ").strip().lower()

        if acao == "listar":
            controller.listar_cargas()
        elif acao == "adicionar":
            controller.adicionar_carga()
        elif acao == "deletar":
            controller.deletar_carga()
        elif acao == "sair":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Ação inválida. Tente novamente.")

if __name__ == "__main__":
    main()
