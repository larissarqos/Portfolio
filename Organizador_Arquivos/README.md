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
### 📌 Organizar por tipo de arquivo
Cria pastas para organizar os arquivos de acordo com a extensão, sendo:
- **Images:** .jpg, .png, .jpeg, .gif, .webp
- **Videos:** .mp4, .mkv, .mov, .flv
- **Documents:** .doc, .pdf, .txt, .docx, .ppt, .pptx, .zip
- **Music:** .mp3, .wav
- **Code:** .html, .css, .js, .py, .ipynb, .sql, .pbix
- **Excel:** .csv, .xls, .xlsx
- **Archives:** .zip, .rar
- **Others:** qualquer outro tipo não listado
  
--

### 📌 Organizar por data de criação
  Ex: Arquivos criados em `2024-10-01` são movidos para uma pasta chamada `2024-10-01`.

--

### 📌 Interface gráfica amigável
Ideal para usuários que não querem usar terminal.

***

<br>

## ✅ Produto Final

### 🟩 Executável
<p align="center">
  <img src="https://github.com/user-attachments/assets/4f7af924-baf8-4309-bf95-71c80a68708b" alt="img" width="600"/>
</p>

--

### 🟩 Interface
<p align="center">
  <img src="https://github.com/user-attachments/assets/788b7527-197a-4fc2-bedf-dbf397feec1d" alt="img" width="600"/>
</p>

--

### 🟩 Antes da Execução (organização por tipo de arquivo)
<p align="center">
  <img src="https://github.com/user-attachments/assets/5085441e-cb6d-46d5-93bf-f6fee8943294" alt="img" width="700"/>
</p>

--

### 🟩 Depois da Execução (organização por tipo de arquivo)
<p align="center">
  <img src="https://github.com/user-attachments/assets/8bcea14d-8515-4316-82a8-242469e6deea" alt="img" width="700"/>
</p>








