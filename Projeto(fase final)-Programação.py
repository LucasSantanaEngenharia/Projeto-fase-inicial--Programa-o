class Usuario:    # Classe que representa um usuário do sistema
    def __init__(self, usuario_id, nome, funcao, senha):
        self.usuario_id = usuario_id   #  Número identificador único do usuário
        self.nome = nome    # Nome completo do usuário
        self.funcao = funcao   # Cargou ou função exercida na empresa/obra
        self.senha = senha    # Senha de acesso para login no sistema

    def __str__(self):
        return f"{self.nome} ({self.funcao})"   # Representação em string para mostrar o nome e função do usuário logado
    
class Equipamento:   # Classe que representa um equipamento
    def __init__(self, id, nome, categoria, status):
        self.id = id    # Identificador único do equipamento
        self.nome = nome    # Nome do equipamento
        self.categoria = categoria   # Categoria (Equipamento: Ferramenta, Maquinário, Dispositivo etc.)
        self.status = status    # Status atual (Disponível, Em uso, Em manutenção etc.) 
        self.historico = []   # Lista para armazenar as ações feitas com o equipamento

    def adicionar_historico(self, acao, usuario):   # Método para registrar ações realizadas no histórico do equipamento
        self.historico.append(f"{acao} por {usuario.nome} ({usuario.funcao})")   # Adiciona a ação com nome e função do usuário responsável

    def __str__(self):   # Retorna uma descrição breve do equipamento (em string)
        return f"[{self.id}] {self.nome} - {self.categoria} ({self.status})"

class SistemaControle:   # Classe principal que gerencia o sistema de controle (equipamentos e usuários cadastrados)
    def __init__(self):
        self.equipamentos = []   # Lista com todos os equipamentos cadastrados
        self.usuarios = {}    # Lista de usuários cadastrados (chave: ID)
        self.usuario_logado = None   # Referência ao usuário atualmente logado

    def cadastrar_usuario(self):   # Função para cadastrar um novo usuário no sistema
        print("\n--- Cadastro de Usuário ---")
        usuario_id = input("ID do usuário: ")
        if usuario_id in self.usuarios:
            print("❌ ID já cadastrado.")
            return
        nome = input("Nome completo: ")
        funcao = input("Função/Cargo: ")
        senha = input("Senha: ")
        self.usuarios[usuario_id] = Usuario(usuario_id, nome, funcao, senha)   # Adiciona o usuário à lista
        print("✅ Usuário cadastrado com sucesso!")

    def login(self):   # Função para realizar login com ID e senha
        print("\n🔐 Login do Usuário")
        usuario_id = input("ID do usuário: ")
        senha = input("Senha: ")
        usuario = self.usuarios.get(usuario_id)
        if usuario and usuario.senha == senha:
            self.usuario_logado = usuario
            print(f"✅ Bem-vindo, {usuario.nome}!")
        else:
            print("❌ ID ou senha incorretos.")

    def logout(self):   # Função para sair da conta logada
        if self.usuario_logado:
            print(f"👋 {self.usuario_logado.nome} saiu do sistema.")
            self.usuario_logado = None
        else:
            print("⚠️ Nenhum usuário logado.")

    def cadastrar_equipamento(self):   # Função para cadastrar novo equipamento
        print("\n--- Cadastro de Equipamento ---")
        id = input("ID do equipamento: ")
        nome = input("Nome: ")
        categoria = input("Categoria (Equipamento: Ferramenta, Maquinário, Dispositivo etc.): ")
        status = input("Status (Disponível / Em uso / Em manutenção etc): ")

        equipamento = Equipamento(id, nome, categoria, status)
        equipamento.adicionar_historico("Cadastrado", self.usuario_logado)
        self.equipamentos.append(equipamento)
        print("✅ Equipamento cadastrado com sucesso!")

    def listar_equipamentos(self):   # Função para exibir todos os equipamentos cadastrados
        print("\n--- Lista de Equipamentos ---")
        if not self.equipamentos:
            print("Nenhum equipamento cadastrado.")
        for eq in self.equipamentos:
            print(eq)

    def buscar_por_id(self):   # Função para buscar um equipamento pelo seu ID
        print("\n--- Buscar por ID ---")
        id = input("Digite o ID do equipamento: ")
        for eq in self.equipamentos:
            if eq.id == id:
                print(eq)
                return
        print("❌ Equipamento não encontrado.")

    def buscar_por_categoria(self):   # Função para buscar equipamentos por categoria
        print("\n--- Buscar por Categoria ---")
        categoria = input("Digite a categoria: ")
        encontrados = [eq for eq in self.equipamentos if eq.categoria.lower() == categoria.lower()]
        if encontrados:
            for eq in encontrados:
                print(eq)
        else:
            print("❌ Nenhum equipamento encontrado na categoria.")

    def buscar_por_status(self):   # Função para buscar equipamentos por status
        print("\n--- Buscar por Status ---")
        status = input("Digite o status: ")
        encontrados = [eq for eq in self.equipamentos if eq.status.lower() == status.lower()]
        if encontrados:
            for eq in encontrados:
                print(eq)
        else:
            print("❌ Nenhum equipamento com esse status.")

    def atualizar_status(self):    # Atualiza o status de um equipamento (ex: de "Em uso" para "Disponível")
        print("\n--- Atualizar Status ---")
        id = input("ID do equipamento: ")
        for eq in self.equipamentos:
            if eq.id == id:
                novo_status = input("Novo status: ")
                eq.status = novo_status
                eq.adicionar_historico("Status atualizado", self.usuario_logado)
                print("✅ Status atualizado com sucesso!")
                return
        print("❌ Equipamento não encontrado.")

    def remover_equipamento(self):   # Remove um equipamento do sistema
        print("\n--- Remover Equipamento ---")
        id = input("ID do equipamento: ")
        for eq in self.equipamentos:
            if eq.id == id:
                self.equipamentos.remove(eq)
                print("✅ Equipamento removido.")
                return
        print("❌ Equipamento não encontrado.")

    def relatorio_geral(self):   # Gera um relatório geral com o total de equipamentos por categoria
        print("\n📊 --- Relatório Geral ---")
        print(f"Total de equipamentos: {len(self.equipamentos)}")
        categorias = {}
        for eq in self.equipamentos:
            categorias[eq.categoria] = categorias.get(eq.categoria, 0) + 1
        for cat, count in categorias.items():
            print(f"- {cat}: {count} equipamentos")

    def historico_equipamento(self):    # Exibe o histórico de ações realizadas em um equipamento específico
        print("\n📚 --- Histórico de Uso ---")
        id = input("Digite o ID do equipamento: ")
        for eq in self.equipamentos:
            if eq.id == id:
                print(f"Histórico do equipamento {eq.nome}:")
                for entrada in eq.historico:
                    print(f" - {entrada}")
                return
        print("❌ Equipamento não encontrado.")

    def menu(self):   # Menu principal do sistema com autenticação de usuário
        while True:
            if not self.usuario_logado:   # Menu para usuários não autenticados
                print("\n=== MENU PRINCIPAL ===")
                print("1. Login")
                print("2. Cadastrar novo usuário")
                print("3. Sair")
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    self.login()
                elif escolha == "2":
                    self.cadastrar_usuario()
                elif escolha == "3":
                    print("Sistema encerrado.")
                    break
                else:
                    print("❌ Opção inválida.")
            else:     
                # Menu completo para usuário autenticado
                print(f"\n🔧 Menu do sistema - Logado como: {self.usuario_logado.nome} ({self.usuario_logado.funcao})")
                print("1. Cadastrar equipamento")
                print("2. Listar equipamentos")
                print("3. Buscar por ID")
                print("4. Buscar por categoria")
                print("5. Buscar por status")
                print("6. Atualizar status")
                print("7. Remover equipamento")
                print("8. Relatório geral")
                print("9. Histórico de uso")
                print("10. Logout")
                opcao = input("Escolha uma opção: ")

                if opcao == "1":
                    self.cadastrar_equipamento()
                elif opcao == "2":
                    self.listar_equipamentos()
                elif opcao == "3":
                    self.buscar_por_id()
                elif opcao == "4":
                    self.buscar_por_categoria()
                elif opcao == "5":
                    self.buscar_por_status()
                elif opcao == "6":
                    self.atualizar_status()
                elif opcao == "7":
                    self.remover_equipamento()
                elif opcao == "8":
                    self.relatorio_geral()
                elif opcao == "9":
                    self.historico_equipamento()
                elif opcao == "10":
                    self.logout()
                else:
                    print("❌ Opção inválida.")


if __name__ == "__main__":  # Execução principal do sistema
    sistema = SistemaControle()   # Cria uma instância do sistema
    sistema.menu()   # Inicia o menu principal