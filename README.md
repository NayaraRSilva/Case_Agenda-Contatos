# 📆 Agenda de Contatos em Python

Este é um projeto simples em Python que permite adicionar, exibir, editar, remover e salvar contatos em uma agenda. Os dados são armazenados em um arquivo .json e a interação é feita via terminal.

## 📁 Arquivos

agenda.json: arquivo onde os contatos são salvos.

main.py: script principal com o código da agenda.

## 📌 Funcionalidades

## ✅ 1. Adicionar contato

O usuário informa nome, telefone e e-mail.

O contato é adicionado à lista atual.

## 📆 2. Exibir contatos

Lista todos os contatos armazenados na agenda.

## ✏️ 3. Editar contato

Permite alterar o telefone e o e-mail de um contato existente.

## 🗑 4. Remover contato

Remove um contato da agenda pelo nome.

## 📅 5. Salvar agenda

Salva todos os contatos no arquivo agenda.json.

## ❌ 6. Sair

Encerra o programa.

## 📂 Estrutura do Código

## 1. Lista agenda

agenda = []

Armazena todos os contatos como dicionários com nome, telefone e e-mail.

## 2. Funções principais

salvar_agenda(): salva os contatos no arquivo JSON.

carregar_agenda(): carrega os contatos salvos anteriormente.

adicionar_contato(nome, telefone, email): adiciona um novo contato.

exibir_contatos(): mostra todos os contatos cadastrados.

editar_contato(): permite editar um contato existente.

remover_contato(): exclui um contato da lista.

## 3. Laço principal (while True)

Exibe o menu e executa as funcionalidades de acordo com a escolha do usuário.

🧑‍💻 Feito com Python

Este projeto tem como objetivo praticar a lógica de programação, manipulação de arquivos JSON e a interação com o usuário via terminal.

