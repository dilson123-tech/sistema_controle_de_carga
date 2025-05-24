import json

def limpar_duplicatas_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r") as f:
            cargas = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Arquivo não encontrado ou vazio. Nada a limpar.")
        return

    # Usamos um set pra rastrear entradas únicas como tuplas
    vistos = set()
    cargas_unicas = []

    for carga in cargas:
        tupla_carga = (carga["nome"], carga["peso"], carga["destino"])
        if tupla_carga not in vistos:
            vistos.add(tupla_carga)
            cargas_unicas.append(carga)

    with open(caminho_arquivo, "w") as f:
        json.dump(cargas_unicas, f, indent=4)

    print(f"{len(cargas) - len(cargas_unicas)} duplicatas removidas. Arquivo limpo!")

# Use o caminho do seu arquivo JSON aqui
limpar_duplicatas_arquivo("data/banco_de_dados.json")
