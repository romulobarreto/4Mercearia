# 📦 Projeto Mercearia - Documentação

## 📌 Visão Geral
Este sistema tem como objetivo gerenciar uma mercearia de forma simples utilizando o padrão MVC.  
Os dados serão armazenados em arquivos JSON.

---

## 📂 Entidades e Estruturas de Dados

### 🛒 Produto
Armazena as informações dos produtos vendidos na mercearia.

- **Atributos:**
  - `id`: Identificador único do produto
  - `nome`: Nome do produto
  - `preco`: Preço unitário
  - `quantidade`: Quantidade em estoque
  - `categoria_id`: Referência à categoria do produto
  - `fornecedor_id`: Referência ao fornecedor

- **Regras de Negócio:**
  - O preço deve ser maior que zero.
  - Não pode haver dois produtos com o mesmo nome.
  - Não pode excluir um produto se ele estiver registrado em alguma venda.

---

### 📁 Categoria
Cada produto pertence a uma categoria (exemplo: Bebidas, Laticínios, Higiene).

- **Atributos:**
  - `id`: Identificador único da categoria
  - `nome`: Nome da categoria

- **Regras de Negócio:**
  - Não pode haver categorias duplicadas.
  - Não pode excluir uma categoria se houver produtos nela.

---

### 🚚 Fornecedor
Armazena informações sobre os fornecedores dos produtos.

- **Atributos:**
  - `id`: Identificador único do fornecedor
  - `nome`: Nome do fornecedor
  - `telefone`: Contato do fornecedor

- **Regras de Negócio:**
  - O telefone deve ter um formato válido (exemplo: (XX) XXXXX-XXXX).
  - Não pode haver dois fornecedores com o mesmo nome.

---

### 🏪 Venda / Caixa
Gerencia as vendas realizadas na mercearia.

- **Atributos:**
  - `id`: Identificador único da venda
  - `produtos`: Lista de produtos vendidos (com quantidade e preço unitário)
  - `total`: Valor total da venda
  - `data`: Data da venda

- **Regras de Negócio:**
  - Ao vender um produto, deve diminuir a quantidade em estoque.
  - O valor total deve ser a soma dos preços dos produtos vendidos.

---

## 📊 Relatórios
O sistema precisa gerar os seguintes relatórios:
1. **Produtos mais vendidos**
2. **Produtos com estoque baixo**
3. **Vendas realizadas em um período específico**
4. **Total arrecadado em um período específico**

---

## 📁 Estrutura do Projeto (Padrão MVC)


---

## ⚡ Funcionalidades Essenciais

- **Cadastrar, editar e excluir produtos**
- **Cadastrar, editar e excluir categorias**
- **Cadastrar, editar e excluir fornecedores**
- **Registrar vendas**
- **Gerar relatórios**

---

## 🛠️ Tecnologias e Ferramentas
- **Linguagem**: Python  
- **Armazenamento**: JSON  
- **Padrão Arquitetural**: MVC  
- **Interface**: Terminal  

---
