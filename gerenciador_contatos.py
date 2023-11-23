import pandas as pd
import ast

class GerenciadorContatos:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.dados = pd.read_csv(caminho_arquivo)

    def resumo(self):
        """Exibe um resumo do número de contatos e empresas."""
        print(f'\nTotal de contatos: {len(self.dados)}')
        print(f'Total de empresas: {self.dados["Empresa"].nunique()}')

    def listar_empresas(self):
        """Lista todas as empresas disponíveis."""
        print('\nEmpresas disponíveis:')
        print(self.dados['Empresa'].unique())

    def listar_gestores(self):
        """Lista todos os gestores disponíveis."""
        print('\nGestores disponíveis:')
        print(self.dados['Gestor Responsável (LUX)'].unique())

    def visualizar_colaboradores(self, empresa):
        """Visualiza colaboradores de uma empresa específica."""
        colaboradores = self.dados[self.dados['Empresa'] == empresa]
        print(colaboradores if not colaboradores.empty else "Empresa não encontrada.")

    def pesquisar_contato(self, nome):
        """Pesquisa contatos pelo nome."""
        resultado_pesquisa = self.dados[self.dados['Nome'].str.contains(nome, case=False)]
        print("\nContatos encontrados:" if not resultado_pesquisa.empty else f"Nenhum contato encontrado para o nome {nome}.")
        print(resultado_pesquisa)

    def visualizar_informacoes_contato(self, indice):
        """Visualiza informações de um contato específico."""
        contato = self.dados.loc[indice] if indice in self.dados.index else None
        print("\nInformações do Contato:" if contato is not None else "Índice não encontrado.")
        print(contato)

    def gerenciar_contatos(self, gestor):
        """Exibe contatos gerenciados por um gestor."""
        contatos = self.dados[self.dados['Gestor Responsável (LUX)'] == gestor]
        print(contatos if not contatos.empty else "Gestor não encontrado.")

    def adicionar_contato(self, info_contato):
        """Adiciona um novo contato."""
        self.dados = self.dados.append(info_contato, ignore_index=True)
        print("\nContato adicionado com sucesso!")

    def atualizar_contato(self, indice, info_contato):
        """Atualiza as informações de um contato."""
        if indice in self.dados.index:
            for coluna, valor in info_contato.items():
                if coluna in self.dados.columns:
                    self.dados.at[indice, coluna] = valor
                else:
                    print(f"Coluna {coluna} não encontrada.")
            print("Contato atualizado com sucesso!")
        else:
            print("Índice não encontrado.")

    def excluir_contato(self, indice):
        """Exclui um contato."""
        if indice in self.dados.index:
            self.dados = self.dados.drop(indice)
            print("Contato excluído com sucesso!")
        else:
            print("Índice não encontrado.")

    def salvar(self):
        """Salva as alterações no arquivo CSV."""
        self.dados.to_csv(self.caminho_arquivo, index=False)
        print("Alterações salvas com sucesso.")

def obter_entrada(mensagem, tipo=str):
    """Obtém uma entrada do usuário."""
    while True:
        try:
            entrada = tipo(input(mensagem))
            return entrada
        except ValueError:
            print(f"Por favor, digite uma {tipo.__name__} válida.")

def exibir_menu():
    """Exibe o menu principal."""
    print("\n***** Menu *****")
    print("1. Exibir resumo")
    print("2. Listar todas as empresas")
    print("3. Listar todos os gestores")
    print("4. Visualizar colaboradores por empresa")
    print("5. Pesquisar contato por nome")
    print("6. Visualizar informações de contato por índice")
    print("7. Gerenciar contatos por gestor")
    print("8. Adicionar um contato")
    print("9. Atualizar um contato")
    print("10. Excluir um contato")
    print("11. Salvar alterações")
    print("12. Sair")

def main():
    caminho_arquivo = input("Digite o caminho para o seu arquivo CSV: ")
    gerenciador = GerenciadorContatos(caminho_arquivo)

    while True:
        exibir_menu()
        escolha = obter_entrada("\nDigite sua escolha: ", int)

        if escolha == 1:
            gerenciador.resumo()
        elif escolha == 2:
            gerenciador.listar_empresas()
        elif escolha == 3:
            gerenciador.listar_gestores()
        elif escolha == 4:
            empresa = obter_entrada("Digite o nome da empresa: ")
            gerenciador.visualizar_colaboradores(empresa)
        elif escolha == 5:
            nome_pesquisa = obter_entrada("Digite o nome para pesquisa: ")
            gerenciador.pesquisar_contato(nome_pesquisa)
        elif escolha == 6:
            indice_visualizar = obter_entrada("Digite o índice do contato para visualizar: ", int)
            gerenciador.visualizar_informacoes_contato(indice_visualizar)
        elif escolha == 7:
            gestor = obter_entrada("Digite o nome do gestor: ")
            gerenciador.gerenciar_contatos(gestor)
        elif escolha == 8:
            info_contato = ast.literal_eval(input("Digite as informações do contato como um dicionário: "))
            gerenciador.adicionar_contato(info_contato)
        elif escolha == 9:
            indice_atualizar = obter_entrada("Digite o índice do contato a ser atualizado: ", int)
            info_atualizar = ast.literal_eval(input("Digite as novas informações do contato como um dicionário: "))
            gerenciador.atualizar_contato(indice_atualizar, info_atualizar)
        elif escolha == 10:
            indice_excluir = obter_entrada("Digite o índice do contato a ser excluído: ", int)
            gerenciador.excluir_contato(indice_excluir)
        elif escolha == 11:
            gerenciador.salvar()
        elif escolha == 12:
            print("Alterações salvas. Até logo!")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
