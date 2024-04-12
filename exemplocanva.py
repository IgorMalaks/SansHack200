import tkinter as tk

def desenhar_circulo():
    canvas.create_oval(50, 50, 150, 150, fill="blue")  # Desenha um círculo azul

def desenhar_retangulo():
    canvas.create_rectangle(200, 50, 300, 150, fill="red")  # Desenha um retângulo vermelho

def limpar_canvas():
    canvas.delete("all")  # Limpa tudo no canvas

# Cria a janela principal
root = tk.Tk()
root.title("Exemplo de uso do Canvas")

# Cria o widget Canvas
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

# Cria botões para desenhar diferentes formas
btn_circulo = tk.Button(root, text="Desenhar Círculo", command=desenhar_circulo)
btn_circulo.pack()

btn_retangulo = tk.Button(root, text="Desenhar Retângulo", command=desenhar_retangulo)
btn_retangulo.pack()

btn_limpar = tk.Button(root, text="Limpar Canvas", command=limpar_canvas)
btn_limpar.pack()

# Inicia o loop principal da aplicação
root.mainloop()
