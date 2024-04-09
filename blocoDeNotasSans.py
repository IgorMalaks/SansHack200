import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

def salvar_arquivo():
    conteudo = texto.get('1.0', tk.END)
    with open('bloco_de_notas.txt', 'w') as arquivo:
        arquivo.write(conteudo)
    messagebox.showinfo("Bloco de Notas", "Arquivo salvo com sucesso!")

def abrir_arquivo():
    try:
        with open('bloco_de_notas.txt', 'r') as arquivo:
            conteudo = arquivo.read()
            texto.delete('1.0', tk.END)
            texto.insert(tk.END, conteudo)
    except FileNotFoundError:
        messagebox.showwarning("Bloco de Notas do Sans, você pode colocar suas senhas de banco e tudo de bom :)", "Arquivo não encontrado!")

# Criar a janela principal
janela = tk.Tk()
janela.title("Bloco de Notas do Sans coloque suas senhas de banco aqui :)")

# Criar uma área de texto com rolagem
texto = scrolledtext.ScrolledText(janela, width=40, height=10)
texto.pack(expand=True, fill='both')

# Criar um menu
menu = tk.Menu(janela)
janela.config(menu=menu)
menu_arquivo = tk.Menu(menu)
menu.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=janela.quit)

# Iniciar a janela
janela.mainloop()
