# 📚 Sistema de Biblioteca

## Regras de Negócio

### Objetivo

Desenvolver um sistema de gerenciamento de biblioteca utilizando Python e Programação Orientada a Objetos (POO). O sistema deverá permitir o cadastro de livros e usuários, bem como o controle de empréstimos e devoluções.

---

# Funcionalidades

## Cadastro de Usuários

O sistema deverá permitir o cadastro de usuários da biblioteca.

Cada usuário deverá possuir, no mínimo:

* Nome
* Identificador único (ID)
* Email válido

Não será permitido cadastrar dois usuários com o mesmo ID.

---

## Cadastro de Livros

O sistema deverá permitir o cadastro de livros.

Cada livro deverá possuir:

* Título
* Autor
* Ano de publicação

Cada livro cadastrado ficará automaticamente disponível para empréstimo.

---

## Consulta do Acervo

O sistema deverá permitir visualizar:

* Todos os livros cadastrados;
* Livros disponíveis;
* Livros emprestados.

---

## Empréstimo de Livros

Um livro somente poderá ser emprestado quando estiver disponível.

Ao realizar um empréstimo, o sistema deverá:

* remover o livro da lista de disponíveis;
* adicionar o livro à lista de empréstimos;
* registrar a data do empréstimo;
* associar o livro ao usuário responsável pelo empréstimo.

Caso o livro não esteja disponível, o empréstimo deverá ser recusado.

---

## Devolução de Livros

Ao devolver um livro, o sistema deverá:

* remover o livro da lista de empréstimos;
* adicioná-lo novamente à lista de disponíveis;
* registrar a data da devolução (opcional).

Não será permitido devolver um livro que não esteja emprestado.

---

# Validações

O sistema deverá garantir que:

* um livro não seja cadastrado duas vezes;
* um usuário não seja cadastrado duas vezes;
* apenas livros existentes possam ser emprestados;
* apenas livros emprestados possam ser devolvidos.

---

# Estrutura Inicial

## Classe Book

Responsável por representar um livro.

### Atributos

* título
* autor
* ano

---

## Classe User

Responsável por representar um usuário.

### Atributos

* nome
* id
* livros emprestados

---

## Classe Library

Responsável por gerenciar todo o sistema.

### Atributos

* nome
* coleção de livros
* usuários cadastrados
* livros disponíveis
* livros emprestados

---

# Regras Gerais

* Um livro só pode estar em um estado:

  * disponível;
  * emprestado.

Nunca poderá estar nas duas listas simultaneamente.

---

# Regras de Integridade

Sempre que um livro for emprestado:

1. Deve existir na coleção.
2. Deve estar disponível.
3. Deve ser removido da lista de disponíveis.
4. Deve ser adicionado à lista de empréstimos.

Sempre que um livro for devolvido:

1. Deve estar emprestado.
2. Deve ser removido da lista de empréstimos.
3. Deve voltar para a lista de disponíveis.

---

# Casos de Teste

O projeto deverá possuir testes automatizados utilizando **pytest**.

Exemplos de testes:

* cadastrar um livro;
* cadastrar um usuário;
* impedir cadastro duplicado;
* verificar disponibilidade de um livro;
* emprestar um livro disponível;
* impedir empréstimo de livro indisponível;
* devolver um livro emprestado;
* impedir devolução de livro não emprestado.

---

# Objetivos de Aprendizagem

Este projeto tem como finalidade praticar:

* Programação Orientada a Objetos;
* Encapsulamento;
* Organização de código em módulos;
* Testes automatizados com pytest;
* Tratamento de exceções;
* Boas práticas de desenvolvimento;
* Modelagem de regras de negócio.

---

# Melhorias Futuras

* Persistência dos dados em JSON.
* Histórico de empréstimos.
* Controle de multas por atraso.
* Busca de livros por título ou autor.
* Interface gráfica.
* API utilizando FastAPI.
* Banco de dados relacional (SQLite ou PostgreSQL).
* Autenticação de usuários.
* Relatórios e estatísticas da biblioteca.
