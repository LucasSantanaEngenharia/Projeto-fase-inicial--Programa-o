# ========================
# Descrição narrativa:
# O presente código implementa um sistema interativo, escrito em Python, destinado ao cadastro e controle de equipamentos utilizados por uma empresa de construção civil — como, por exemplo, escavadeiras, caminhões ou qualquer outro tipo de maquinário e equipamentos.
# O sistema foi desenvolvido com o objetivo de facilitar a gestão operacional desses recursos, permitindo ao usuário realizar atividades fundamentais como registrar novos equipamentos, consultar os já cadastrados, buscar um item específico, atualizar o status de uso e até removê-los da base.

# Fluxograma:
# Arquivo: fluxograma_sistemacontrole.jpg
# (Veja o fluxograma visual nesta imagem separada)
# ========================


# sistema_equipamentos.py

class Equipamento:
    """Classe que representa um equipamento da empresa."""
    def __init__(self, id, nome, categoria, status):
        self.id = id # um identificador único (id)
        self.nome = nome # um nome descritivo
        self.categoria = categoria #  uma categoria (como 'Escavadeira', 'Caminhão', etc.)
        self.status = status # um status (como 'Disponível', 'Em uso', 'Em manutenção')

    def __str__(self):
        return f"[{self.id}] {self.nome} - {self.categoria} ({self.status})"  # Retorna uma representação em string do equipamento


class SistemaControle:
    """Classe que gerencia o cadastro e controle dos equipamentos."""
    def __init__(self):
        self.equipamentos = []  # Lista que armazenará todos os equipamentos cadastrados

    def cadastrar(self):
        print("\n--- Cadastro de Equipamento ---")  # Coleta os dados do equipamento via input
        id = input("ID do equipamento: ")
        nome = input("Nome do equipamento: ")
        categoria = input("Categoria (ex: Escavadeira, Caminhão, etc): ")
        status = input("Status (Disponível / Em uso / Em manutenção): ")

        equipamento = Equipamento(id, nome, categoria, status)
        self.equipamentos.append(equipamento)
        print("✅ Equipamento cadastrado com sucesso!")
 # Cria um novo objeto Equipamento e adiciona à lista


    def listar(self):
        print("\n--- Lista de Equipamentos Cadastrados ---")
        if not self.equipamentos:   # Verifica se há equipamentos cadastrados
            print("Nenhum equipamento cadastrado.")
            return
        for eq in self.equipamentos:  # Itera sobre a lista e imprime cada equipamento
            print(eq)

    def buscar(self):
        print("\n--- Buscar Equipamento por ID ---")
        id = input("Digite o ID: ")    # Procura um equipamento com ID correspondente
        for eq in self.equipamentos: 
            if eq.id == id:
                print("Equipamento encontrado:")
                print(eq)
                return
        print("❌ Equipamento não encontrado.")

    def atualizar(self):
        print("\n--- Atualizar Equipamento ---")
        id = input("Digite o ID do equipamento a ser atualizado: ")   # Procura o equipamento pelo ID
        for eq in self.equipamentos:
            if eq.id == id:
                print(f"Equipamento atual: {eq}") 
                novo_status = input("Novo status: ")   # Solicita novo status e atualiza
                eq.status = novo_status
                print("✅ Status atualizado com sucesso!")
                return
        print("❌ Equipamento não encontrado.")

    def remover(self):
        print("\n--- Remover Equipamento ---")
        id = input("Digite o ID do equipamento a ser removido: ")  # Procura e remove o equipamento da lista
        for eq in self.equipamentos:
            if eq.id == id:
                self.equipamentos.remove(eq)
                print("✅ Equipamento removido com sucesso!")
                return
        print("❌ Equipamento não encontrado.")

    def menu(self): # Exibe o menu principal e gerencia as opções escolhidas pelo usuário.
        while True:
            print("\n=== Sistema de Cadastro e Controle de Equipamentos ===")
            print("1. Cadastrar equipamento")
            print("2. Listar equipamentos")
            print("3. Buscar equipamento por ID")
            print("4. Atualizar status do equipamento")
            print("5. Remover equipamento")
            print("6. Sair")

            opcao = input("Escolha uma opção: ")

   # Executa a funcionalidade correspondente
            if opcao == "1":
                self.cadastrar()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.buscar()
            elif opcao == "4":
                self.atualizar()
            elif opcao == "5":
                self.remover()
            elif opcao == "6":
                print("Encerrando o sistema. Até logo!")
                break
            else:
                print("❌ Opção inválida. Tente novamente.")

# Execução do programa
if __name__ == "__main__": # Esta parte garante que o código só será executado se o script for rodado diretamente
    sistema = SistemaControle()
    sistema.menu()