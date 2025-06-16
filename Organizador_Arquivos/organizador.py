import os
import shutil
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from datetime import datetime as dt

# Mapeando as extensões de arquivos
def create_default_extensions_map():
    return {
        'Images': ['.jpg', '.png', '.jpeg', '.gif', '.webp'],
        'Videos': ['.mp4', '.mkv', '.mov', '.flv'],
        'Documents': ['.doc', '.pdf', '.txt', '.docx', '.ppt', '.pptx', '.zip'],
        'Music': ['.mp3', '.wav'],
        'Code': ['.html', '.css', '.js', '.py', '.ipynb', '.sql', '.pbix'],
        'Excel': ['.csv', '.xls', '.xlsx'],
        'Archives': ['.zip', '.rar'],
        'Others': []
    }

# Encontrar nome da pasta apropriada para extensão
def get_folder_for_extension(extension, extension_map):
    for folder, extensions in extension_map.items():
        if extension in extensions:
            return folder
    return 'Others'

# Mover o arquivo para a pasta apropriada
def move_file(file_path, folder_name, directory):
    folder_path = os.path.join(directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    new_path = shutil.move(file_path, folder_path)
    print(f'Moved {os.path.basename(file_path)} to {folder_path}')
    return new_path

# Organizar arquivos no diretório por tipo de extensão
def organize_by_extension(directory):
    extensions_map = create_default_extensions_map()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            extension = os.path.splitext(file_path)[1].lower()
            folder_name = get_folder_for_extension(extension, extensions_map)
            move_file(file_path, folder_name, directory)

# Organizar os arquivos no diretório por data de criação
def organize_by_date(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            created_at = dt.fromtimestamp(os.path.getctime(file_path))
            folder_name = created_at.strftime('%Y-%m-%d')
            move_file(file_path, folder_name, directory)

# Interface com Tkinter
def run_gui():
    def browse_directory():
        folder = filedialog.askdirectory()
        if folder:
            directory_var.set(folder)

    def execute_organization():
        directory = directory_var.get()
        method = method_var.get()

        if not directory:
            messagebox.showerror("Erro", "Por favor, selecione um diretório.")
            return

        if method == "Por Tipo de Arquivo":
            organize_by_extension(directory)
        elif method == "Por Data":
            organize_by_date(directory)
        else:
            messagebox.showwarning("Aviso", "Escolha um método válido.")
            return

        messagebox.showinfo("Concluído", f"Arquivos organizados com sucesso por: {method}")

    def sair():
        window.destroy()

    # Criando janela
    window = tk.Tk()
    window.title("Organizador de Arquivos")
    window.geometry("400x230")
    window.resizable(False, False)

    # Diretório
    directory_var = tk.StringVar()
    tk.Label(window, text="Selecione o diretório:").pack(pady=5)
    dir_frame = tk.Frame(window)
    dir_frame.pack()
    tk.Entry(dir_frame, textvariable=directory_var, width=40).pack(side=tk.LEFT, padx=5)
    tk.Button(dir_frame, text="Procurar", command=browse_directory).pack(side=tk.LEFT)

    # Opção de organização
    method_var = tk.StringVar()
    tk.Label(window, text="Escolha o método de organização:").pack(pady=10)
    ttk.Combobox(window, textvariable=method_var, values=["Por Tipo de Arquivo", "Por Data"], state="readonly").pack()

    # Botão de executar
    tk.Button(window, text="Organizar", command=execute_organization, width=10).pack(pady=20)
    btn_sair = tk.Button(window, text="Sair", fg="red", borderwidth=0, highlightthickness=0, cursor="hand2")
    btn_sair.pack(pady=5)
    btn_sair.config(command=sair)

    window.mainloop()

if __name__ == '__main__':
    run_gui()
