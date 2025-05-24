from controllers.carga_controller import CargaController

def main():
    controlador = CargaController()
    print("Bem-vindo ao Sistema de Controle de Carga")

    while True:
        acao = input("Digite uma ação (listar, adicionar, sair): ").strip().lower()

        if acao == 'listar':
            controlador.listar_cargas()
        elif acao == 'adicionar':
            controlador.adicionar_carga()
        elif acao == 'sair':
            print("Saindo...")
            break
        else:
            print("Ação inválida, tenta de novo.")

if __name__ == '__main__':
    main()
