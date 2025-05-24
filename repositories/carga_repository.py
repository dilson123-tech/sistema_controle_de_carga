import os
import json
import shutil
import datetime
from models.carga_model import CargaModel

class CargaRepository:
    def __init__(self):
        self.caminho_banco = 'data/banco_de_dados.json'
        self.cargas = self.carregar()

    def carregar(self):
        if not os.path.exists(self.caminho_banco):
            return []
        with open(self.caminho_banco, 'r') as f:
            dados = json.load(f)
            return [CargaModel(**item) for item in dados]

    def salvar(self):
        try:
            backup_nome = f"data/banco_de_dados_backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            shutil.copy(self.caminho_banco, backup_nome)
        except FileNotFoundError:
            pass
        
        with open(self.caminho_banco, 'w') as f:
            json.dump([carga.to_dict() for carga in self.cargas], f, indent=4)

    def listar(self):
        return self.cargas

    def adicionar(self, nova_carga):
        for carga in self.cargas:
            if (carga.nome == nova_carga.nome and 
                carga.peso == nova_carga.peso and 
                carga.destino == nova_carga.destino):
                raise ValueError("Essa carga já está cadastrada.")
        self.cargas.append(nova_carga)
        self.salvar()
