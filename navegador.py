import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import webbrowser
from tkinter import messagebox
from tkinter import scrolledtext

def open_url():
    url = url_entry.get()
    webbrowser.open_new(url)
    

def salvar_arquivo():
    conteudo = texto.get('1.0', tk.END)
    with open('bloco_de_notas_sans.txt', 'w') as arquivo:
        arquivo.write(conteudo)
    messagebox.showinfo("Bloco de Notas", "Arquivo salvo com sucesso!")

def abrir_arquivo():
    try:
        with open('bloco_de_notas_sans', 'r') as arquivo:
            conteudo = arquivo.read()
            texto.delete('1.0', tk.END)
            texto.insert(tk.END, conteudo)
    except FileNotFoundError:
        messagebox.showwarning("Bloco de Notas do Sans, você pode colocar suas senhas de banco e tudo de bom :)", "Arquivo não encontrado!")
def imprimir_texto():
    texto = "Clicar neste botão te enche de DETERMINAÇÃO!!!"
    label = tk.Label(root, text=texto)
    label.pack()


# Criar janela
root = tk.Tk()
root.title("Navegador do Sans sem vírus")


# Criar entrada para URL
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)


# Botão para abrir URL
open_button = tk.Button(root, text="""░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░
░█░░░░░░░░▀▄░░░░░░▄░
█░░▀░░▀░░░░░▀▄▄░░█░█
█░▄░█▀░▄░░░░░░░▀▀░░█
█░░▀▀▀▀░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░█
░█░░▄▄░░▄▄▄▄░░▄▄░░█░
░█░▄▀█░▄▀░░█░▄▀█░▄▀░
░░▀░░░▀░░░░░▀░░░▀░░░░""", command=open_url)
open_button.pack()


# Área para exibir conteúdo da página



texto = scrolledtext.ScrolledText(root, width=40, height=10)
texto.pack(expand=True, fill='both')

menu = tk.Menu(root)
root.config(menu=menu)
menu_arquivo = tk.Menu(menu)
menu.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=root.quit)
botao = tk.Button(root, text="DETERMINAÇÃO", command=imprimir_texto)
botao.pack()

# Iniciar loop da interface gráfica
root.mainloop()

# Criar um label com o texto desejado
texto1 = "Este é um exemplo de texto exibido com Tkinter."
label = tk.Label(root, text=texto1)
label.pack()

# Iniciar a janela
root.mainloop()




