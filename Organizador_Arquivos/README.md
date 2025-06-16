<h1 align="center"> Organizador de Arquivos com Interface Gráfica </h1>

<br>

## 📃 Contexto 
Este projeto é uma aplicação em Python que organiza automaticamente os arquivos de um diretório com base em **dois critérios**:
- **Tipo de arquivo** (imagens, vídeos, documentos, etc.)
- **Data de criação** (organização por pastas com data)

Tudo isso com uma **interface gráfica simples**, feita com `Tkinter`, que permite selecionar a pasta e o método de organização com poucos cliques.

***

<br>

## 🛠️ Ferramentas e Tecnologias Utilizadas
**Python**
- **Tkinter** – Criação da interface gráfica
- **Shutil / OS** – Manipulação de arquivos e diretórios
- **Datetime** – Formatação de datas de criação

***

<br>

## 🎯 Motivação
Ao acumular arquivos em uma pasta (como a pasta *Downloads* ou *Área de Trabalho*), a organização pode se tornar um desafio. Este projeto foi criado para **automatizar** essa tarefa de forma prática e reutilizável, com foco em produtividade.

***

<br>

## 🖼️ Interface do Programa
A interface é simples e direta:

- Campo para escolher a pasta
- Menu para selecionar o método de organização
- Botões para **executar** ou **sair**

***

<br>

## 📍 Funcionalidades

- 📌 **Organizar por tipo de arquivo**  
  Ex: Imagens → `Images/`, Planilhas → `Excel/`, Códigos → `Code/`, etc.

- 📌 **Organizar por data de criação**  
  Ex: Arquivos criados em `2024-10-01` são movidos para uma pasta chamada `2024-10-01`.

- 📌 **Interface gráfica amigável**, ideal para usuários que não querem usar terminal.



## ▶️ Como Executar

1. Clone este repositório:
```bash
git clone https://github.com/seuusuario/organizador-arquivos.git
