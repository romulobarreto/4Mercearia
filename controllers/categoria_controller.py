from daos.categoria_dao import *
from daos.produto_dao import *
from models.categoria import *
from utils.buscas import buscar_nome
from utils.gerador import gerador_id

class CategoriaController:

    @staticmethod
    def validar_dados(nome, nome_atual=None):
        # Carrega a lista de categorias
        categorias = CategoriaDao.carregar_categoria()

        # Valida o valor de nome
        if not nome:
            return False, "⚠️ O nome não pode estar vazio."
        
        if nome != nome_atual and any(categoria["nome"] == nome for categoria in categorias):
            return False, "🚫 Categoria já cadastrada."
        
        return True, "✅ Dados aprovados."




    
    @staticmethod
    def cadastrar_categoria(nome):
        # Carrega a lista de categorias
        categorias = CategoriaDao.carregar_categoria()

        # Valida o valor de nome
        sucesso, mensagem = CategoriaController.validar_dados(nome)
        if not sucesso:
            return False, mensagem
        
        # Define o valor do maior_id
        id = gerador_id(categorias)

        # Cria a categoria
        categoria = Categoria(id, nome)

        # Transforma a categoria em dicionário e adiciona na lista
        categorias.append(categoria.salvar_dict())

        # Salva a lista de categoria no banco e exibe a mensagem
        sucesso, mensagem = CategoriaDao.salvar_categoria(categorias)

        if sucesso:
            return True, mensagem
        else:
            return False, mensagem
        





    @staticmethod
    def detalhar_categorias(id=None):
        # Carregar categorias
        categorias = CategoriaDao.carregar_categoria()

        # Verifica se existe categoria cadastrada
        if not categorias:
            return False, "\n⚠️ A lista de categorias está vazia!"
        
        # Detalhar categorias
        if id:
            lista_formatada = "\n📋 Detalhes da categoria:\n"
            for categoria in categorias:
                if categoria["id"] == id:
                    lista_formatada += f"ID {categoria["id"]}: {categoria["nome"].title()}\n---------------------------"
                    break
        else:
            lista_formatada = "\n📋 Lista de categorias cadastradas:\n"
            for categoria in sorted(categorias, key=lambda c: c["nome"]):
                lista_formatada += f"ID {categoria["id"]}: {categoria["nome"].title()}\n"
            lista_formatada += "---------------------------"

        return True, lista_formatada
    




    
    @staticmethod
    def excluir_categoria(id_categoria):
        # Carrega lista de categorias e produtos
        categorias = CategoriaDao.carregar_categoria()
        produtos = ProdutoDao.carregar_produto()

        # Valida se o id da categoria está cadastrado
        dicionario_categoria = None
        for categoria in categorias:
            if categoria["id"] == id_categoria:
                dicionario_categoria = categoria
                break
        
        if not dicionario_categoria:
            return False, f"⚠️ O ID: {id_categoria}, não está na lista de cadastro."
                
        
        # Verifica se a categoria está em uso com algum produto, se estiver, não pode ser excluída
        categoria_nome = buscar_nome(id_categoria, categorias)
        for produto in produtos:
            if produto["categoria_id"] == id_categoria:
                return False, f"\n⚠️ {categoria_nome.title()} não pode ser excluído pois está sendo usado por um produto."
        
        # Remove o dicionário da categoria da base
        categorias.remove(dicionario_categoria)

        # Salva a lista atualizada na base
        CategoriaDao.salvar_categoria(categorias)
        return True, f"✅ A categoria {categoria_nome.title()} foi deletada com sucesso."
        






    @staticmethod
    def editar_categoria(id_categoria, novo_nome, dicionario_categoria):
        # Carrega lista de usuários
        categorias = CategoriaDao.carregar_categoria()

        categoria_nome = buscar_nome(id_categoria, categorias)

        # Valida o nome da categoria
        if not novo_nome:
            return False, f"✅ A categoria {categoria_nome.title()} permanece a mesma."
        
        # Valida se o nome da categoria está cadastrado
        sucesso, mensagem = CategoriaController.validar_dados(novo_nome, dicionario_categoria["nome"])
        if not sucesso:
            return False, mensagem
            
        # Encontra a lista que deve ser editado e faz a alteração
        for categoria in categorias:
            if categoria["id"] == id_categoria:
                categoria["nome"] = novo_nome
                break

        # Salva a lista editada no banco
        sucesso, mensagem = CategoriaDao.salvar_categoria(categorias)

        # Mostra a mensagem de sucesso
        if sucesso:
            return True, f"{mensagem}\nCategoria antiga: {categoria_nome.title()}\nCategoria nova: {novo_nome.title()}"
        else:
            return False, mensagem