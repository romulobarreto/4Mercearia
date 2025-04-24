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
  - Não pode excluir um fornecedor se houver produtos associados a ele.

---

### 👤 Cliente
Armazena informações dos clientes da mercearia.

- **Atributos:**
  - `id`: Identificador único do cliente
  - `nome`: Nome do cliente
  - `cpf`: CPF do cliente
  - `telefone`: Telefone para contato
  - `endereco`: Endereço do cliente

- **Regras de Negócio:**
  - O CPF deve ter um formato válido.
  - Não pode haver dois clientes com o mesmo CPF.
  - O telefone deve seguir um padrão válido.

---

### 👨‍💼 Funcionário
Armazena informações dos funcionários da mercearia.

- **Atributos:**
  - `id`: Identificador único do funcionário
  - `nome`: Nome completo do funcionário
  - `cpf`: CPF do funcionário
  - `telefone`: Telefone para contato
  - `cargo`: Cargo do funcionário
  - `salario`: Salário do funcionário

- **Regras de Negócio:**
  - O CPF deve ter um formato válido.
  - Não pode haver dois funcionários com o mesmo CPF.
  - O salário deve ser maior que zero.

---

### 🏪 Venda / Caixa
Gerencia as vendas realizadas na mercearia.

- **Atributos:**
  - `id`: Identificador único da venda
  - `produtos`: Lista de produtos vendidos (com quantidade e preço unitário)
  - `total`: Valor total da venda
  - `data`: Data da venda
  - `cliente_id`: Referência ao cliente (opcional)
  - `funcionario_id`: Referência ao funcionário que realizou a venda

- **Regras de Negócio:**
  - Ao vender um produto, deve diminuir a quantidade em estoque.
  - O valor total deve ser a soma dos preços dos produtos vendidos.
  - Uma venda pode ser feita para um cliente não cadastrado.

---

## 📊 Relatórios
O sistema precisa gerar os seguintes relatórios:
1. **Relatório geral de vendas**
   - Lista de todas as vendas com detalhes completos
   
2. **Relatório de vendas por data**
   - Vendas filtradas por período específico
   
3. **Relatório de produtos mais vendidos**
   - Ranking dos produtos por quantidade total vendida
   
4. **Relatório de clientes que mais compraram**
   - Ranking dos clientes por valor total gasto ou número de compras
   
5. **Controle de produtos em estoque**
   - Lista de produtos com estoque atual, alertas para produtos com estoque baixo

- **Requisitos de Exportação:**
  - Todos os relatórios devem ser exibidos no terminal
  - Todos os relatórios devem ter a opção de serem exportados para Excel

---

## 📁 Estrutura do Projeto (Padrão MVC)

### 📂 Models
- `produto.py`: Classe Produto
- `categoria.py`: Classe Categoria
- `fornecedor.py`: Classe Fornecedor
- `cliente.py`: Classe Cliente
- `funcionario.py`: Classe Funcionario
- `venda.py`: Classe Venda

### 📂 Views
- `produto_view.py`: Interface para operações de produtos
- `categoria_view.py`: Interface para operações de categorias
- `fornecedor_view.py`: Interface para operações de fornecedores
- `cliente_view.py`: Interface para operações de clientes
- `funcionario_view.py`: Interface para operações de funcionários
- `venda_view.py`: Interface para caixa e vendas
- `relatorio_view.py`: Interface para geração de relatórios
- `menu_view.py`: Menu principal do sistema

### 📂 Controllers
- `produto_controller.py`: Lógica para gerenciar produtos
- `categoria_controller.py`: Lógica para gerenciar categorias
- `fornecedor_controller.py`: Lógica para gerenciar fornecedores
- `cliente_controller.py`: Lógica para gerenciar clientes
- `funcionario_controller.py`: Lógica para gerenciar funcionários
- `venda_controller.py`: Lógica para gerenciar vendas
- `relatorio_controller.py`: Lógica para gerar relatórios

### 📂 DAOs
- `produto_dao.py`: Acesso a dados de produtos
- `categoria_dao.py`: Acesso a dados de categorias
- `fornecedor_dao.py`: Acesso a dados de fornecedores
- `cliente_dao.py`: Acesso a dados de clientes
- `funcionario_dao.py`: Acesso a dados de funcionários
- `venda_dao.py`: Acesso a dados de vendas

### 📂 Utils
- `validacoes.py`: Funções para validação de dados
- `formatacao.py`: Funções para formatação de dados
- `exportacao.py`: Funções para exportação de relatórios para Excel
- `gerador_id.py`: Funções para gerar IDs únicos

---

## ⚡ Funcionalidades Essenciais

- **Cadastrar, editar e excluir produtos**
- **Cadastrar, editar e excluir categorias**
- **Cadastrar, editar e excluir fornecedores**
- **Cadastrar, editar e excluir clientes**
- **Cadastrar, editar e excluir funcionários**
- **Registrar vendas (caixa)**
- **Controlar estoque de produtos**
- **Gerar relatórios com opção de exportação para Excel**

---

## 🛠️ Tecnologias e Ferramentas
- **Linguagem**: Python  
- **Armazenamento**: JSON  
- **Padrão Arquitetural**: MVC  
- **Interface**: Terminal
- **Bibliotecas**: 
  - `pandas`: Para manipulação de dados e exportação para Excel
  - `re`: Para validações usando expressões regulares
  - `datetime`: Para manipulação de datas
  - `json`: Para armazenamento e leitura de dados

---

## 🔄 Fluxos Principais

### 🛒 Fluxo de Venda
1. Selecionar produtos e quantidades
2. Opcionalmente, vincular a um cliente cadastrado
3. Registrar funcionário que realizou a venda
4. Finalizar venda e atualizar estoque
5. Emitir comprovante no terminal

### 📊 Fluxo de Relatório
1. Selecionar tipo de relatório
2. Definir parâmetros (período, filtros)
3. Visualizar no terminal
4. Opcionalmente, exportar para Excel
