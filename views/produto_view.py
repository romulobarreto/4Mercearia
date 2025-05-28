from decimal import Decimal, InvalidOperation
from controllers.produto_controller import *
from views.fornecedor_view import *
from views.categoria_view import *
from utils.buscas import buscar_nome, buscar_nome
from utils.formatacao import formatar_preco

class ProdutoView():
    @staticmethod
    def cadastrar_produto():
        # Carrega as listas de categoria e fornecedores e verifica se estão vazias, se estiverem, cancela o cadastro
        categorias = CategoriaDao.carregar_categoria()
        fornecedores = FornecedorDao.carregar_fornecedor()

        if not categorias:
            print("\n🚫 Não existe nenhuma categoria cadastrada, não é possível cadastrar um produto.")
            return
        
        if not fornecedores:
            print("\n🚫 Não existe nenhum fornecedor cadastrado, não é possível cadastrar um produto.")
            return

        # Solicita os inputs ao usuário
        nome = input("\nDigite o nome do produto: ").strip().lower()
        try:
            preco = Decimal(input("\nDigite o preço do produto: R$").strip().replace(".", "").replace(",", "."))
        except InvalidOperation:
            print("\n⚠️ O valor não está na formatação correta.")
            return
        try:
            quantidade = int(input("\nDigite a quantidade em estoque do produto: ").strip())
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return
        
        # Mostra as categorias disponíveis para o usuário escolher uma
        print("\n📋 Lista de categorias:")
        for categoria in sorted(categorias, key=lambda c: c["nome"]):
            print(f"{categoria["id"]}: {categoria["nome"].title()}")

        categoria_id = input("\nDigite o ID da categoria (ou deixe vazio para interromper o cadastro): ").strip()

        if not categoria_id:
            print("✅ Nenhuma categoria foi alterada.")
            return
        
        try:
            categoria_id = int(categoria_id)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return

        # Mostra os fornecedores disponíveis para o usuário escolher um
        print("\n📋 Lista de fornecedores:")
        for fornecedor in sorted(fornecedores, key=lambda c: c["nome"]):
            print(f"{fornecedor["id"]}: {fornecedor["nome"].title()}")

        fornecedor_id = input("\nDigite o ID do fornecedor (ou deixe vazio para interromper o cadastro): ").strip()

        if not fornecedor_id:
            print("✅ Nenhum fornecedor foi editado.")
            return
        
        try:
            fornecedor_id = int(fornecedor_id)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return

        # Chama a função de cadastrar um produto
        sucesso, mensagem = ProdutoController.cadastrar_produto(nome, preco, quantidade, categoria_id, fornecedor_id)
        print(mensagem)





    @staticmethod
    def detalhar_produtos(id=None):
        # Chama a função de detalhar 
        sucesso, mensagem = ProdutoController.detalhar_produtos(id)
        # Exibe o resultado
        print(mensagem)






    @staticmethod
    def excluir_produto():
        # Chama a lista de produto
        produtos = ProdutoDao.carregar_produto()

        # Se a lista estiver vazia, encerra a função
        if not produtos:
            return False, "\n⚠️ Não existem produtos para serem excluídos."
        
        # Chama e exibe a lista de produtos para o usuário ver as opções e escolher uma
        ProdutoView.detalhar_produtos()

        # Solicita ao usuário o ID do produto que ele deseja excluir
        id_produto = input("\nDigite o ID do produto que deseja excluir (Caso não queira cancelar, deixe em branco): ")

        if not id_produto:
            print("✅ Nenhum produto foi excluído.")
            return

        # Converte o ID para INT
        try:
            id_produto = int(id_produto)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return       

        # Chama a função de excluir o produto
        sucesso, mensagem = ProdutoController.excluir_produto(id_produto)
        print(mensagem)






    @staticmethod
    def editar_produto():
        # Carrega as listas de categoria, fornecedores e produtos e verifica se estão vazias, se estiverem, cancela o cadastro
        categorias = CategoriaDao.carregar_categoria()
        fornecedores = FornecedorDao.carregar_fornecedor()
        produtos = ProdutoDao.carregar_produto()

        if not categorias:
            print("\n🚫 Não existe nenhuma categoria cadastrada, não é possível editar um produto.")
            return
        
        if not fornecedores:
            print("\n🚫 Não existe nenhum fornecedor cadastrado, não é possível editar um produto.")
            return
        
        if not produtos:
            print("\n🚫 Não existe nenhum produto cadastrado, não é possível editar um produto.")
            return
        
        # Chama e exibe a lista de produtos para o usuário ver as opções e escolher uma
        ProdutoView.detalhar_produtos()

        # Solicita o ID do produto que será editado e valida
        id_produto = input("\nDigite o ID do produto que deseja editar (Caso não queira cancelar, deixe em branco): ")

        if not id_produto:
            print("✅ Nenhum produto foi editado.")
            return

        # Converte o ID para INT
        try:
            id_produto = int(id_produto)
        except ValueError:
            print("\n⚠️ O valor não está na formatação correta.")
            return

        # Verifica se o ID corresponde a um produto cadastrado
        lista_produto = None
        for produto in produtos:
            if produto["id"] == id_produto:
                lista_produto = produto
                break
        
        if not lista_produto:
            print(f"❌ O ID: {id_produto}, não é um produto cadastrado.")
            return

        # Exibe o produto escolhido de forma detalhada
        ProdutoView.detalhar_produtos(id_produto)
        
        # Solicita a chave ao usuário
        chave = input("\nDigite a chave que deseja alterar (Nome, Preço, Quantidade, Categoria, Fornecedor): ").strip().lower().replace("ç", "c").replace("categoria", "categoria_id").replace("fornecedor", "fornecedor_id")

        # Valida se a chave existe
        if chave not in lista_produto:
            print(f'\n⚠️ A chave: {chave} é inválida.')
            return

        # Pede o input para atualizar a chave que o usuário escolheu
        # Caso queira mudar o nome
        if chave == "nome":
            nome = input('\nDigite o novo nome do produto (ou pressione Enter para manter o mesmo): ').strip().lower()
            if not nome:
                print(f"\n✅ O nome do produto: {lista_produto["nome"].title()} foi mantido.")
                return
            else:
                preco = Decimal(lista_produto["preco"])
                quantidade = lista_produto["quantidade"]
                categoria_id = lista_produto["categoria_id"]
                fornecedor_id = lista_produto["fornecedor_id"]

        # Caso queira mudar o preco
        elif chave == "preco":
            preco = input('\nDigite o novo preço do produto (ou pressione Enter para manter o mesmo): R$').strip().replace(".", "").replace(",", ".")
            if not preco:
                print(f"\n✅ O produto: {lista_produto["nome"].title()} teve o preço mantido.")
                return
            try:
                preco = Decimal(preco)
            except InvalidOperation:
                print("\n⚠️ O valor não está na formatação correta.")
                return
            nome = lista_produto["nome"]
            quantidade = lista_produto["quantidade"]
            categoria_id = lista_produto["categoria_id"]
            fornecedor_id = lista_produto["fornecedor_id"]

        # Caso queira mudar a quantidade em estoque
        elif chave == "quantidade":
            quantidade = input('\nDigite a nova quantidade do produto (ou pressione Enter para manter o mesmo): ').strip()
            if not quantidade:
                print(f"\n✅ O produto: {lista_produto["nome"].title()} teve o estoque mantido.")
                return
            try:
                quantidade = int(quantidade)
            except ValueError:
                print("\n⚠️ O valor não está na formatação correta.")
                return
            nome = lista_produto["nome"]
            preco = Decimal(lista_produto["preco"])
            categoria_id = lista_produto["categoria_id"]
            fornecedor_id = lista_produto["fornecedor_id"]

        # Caso queira alterar a categoria
        elif chave == "categoria_id":
        # Exibe lista de categorias cadastradas
            print("\n📋 Lista de categorias:")
            for categoria in sorted(categorias, key=lambda c: c["nome"]):
                print(f"ID: {categoria["id"]} - {categoria["nome"].title()}")

            categoria_id = input(f"\nDigite o ID da nova categoria do produto: {lista_produto["nome"].title()} (ou pressione Enter para manter o mesmo): ").strip()
            if not categoria_id:
                print(f"\n✅ O produto: {lista_produto["nome"].title()} teve a categoria mantida.")
                return
            try:
                categoria_id = int(categoria_id)
            except ValueError:
                print("\n⚠️ O valor não está na formatação correta.")
                return
            nome = lista_produto["nome"]
            preco = Decimal(lista_produto["preco"])
            quantidade = lista_produto["quantidade"]
            fornecedor_id = lista_produto["fornecedor_id"]

        # Caso queira alterar o fornecedor
        elif chave == "fornecedor_id":
        # Exibe a lista de fornecedores cadastrados
        
            print("\n📋 Lista de fornecedores:")
            for fornecedor in sorted(fornecedores, key=lambda c: c["nome"]):
                print(f"ID: {fornecedor["id"]} - {fornecedor["nome"].title()}")

            fornecedor_id = input(f"\nDigite o ID do novo fornecedor do produto: {lista_produto["nome"].title()} (ou pressione Enter para manter o mesmo): ").strip()
            if not fornecedor_id:
                print(f"\n✅ O produto: {lista_produto["nome"].title()} teve o fornecedor mantido.")
                return
            try:
                fornecedor_id = int(fornecedor_id)
            except ValueError:
                print("\n⚠️ O valor não está na formatação correta.")
                return
            nome = lista_produto["nome"]
            preco = Decimal(lista_produto["preco"])
            quantidade = lista_produto["quantidade"]
            categoria_id = lista_produto["categoria_id"]

        # Chama a função de editar do controller
        sucesso, mensagem = ProdutoController.editar_produto(nome, preco, quantidade, categoria_id, fornecedor_id, lista_produto)

        # Mostra a mensagem de sucesso no terminal
        if sucesso:
            if chave == "nome":
                print(mensagem)
                print(f"O produto teve o nome atualizado:\nDe: {lista_produto["nome"].title()}\nPara: {nome.title()}")
                return
            elif chave == "preco":
                print(mensagem)
                print(f"{lista_produto["nome"].title()} teve o preço atualizado:\nDe: {formatar_preco(float(lista_produto["preco"]))}\nPara: {formatar_preco(preco)}")
                return
            elif chave == "quantidade":
                print(mensagem)
                print(f"{lista_produto["nome"].title()} teve o estoque atualizado:\nDe: {lista_produto["quantidade"]}\nPara: {quantidade}")
                return
            elif chave == "categoria_id":
                print(mensagem)
                print(f"{lista_produto["nome"].title()} teve a categoria atualizada:\nDe: {buscar_nome(lista_produto["categoria_id"], categorias).title()}\nPara: {buscar_nome(categoria_id, categorias).title()}")
                return
            elif chave == "fornecedor_id":
                print(mensagem)
                print(f"{lista_produto["nome"].title()} teve o fornecedor atualizad:\nDe: {buscar_nome(lista_produto["fornecedor_id"], fornecedores).title()}\nPara: {buscar_nome(fornecedor_id, fornecedores).title()}")
                return
        else:
            print(mensagem)


        
                

