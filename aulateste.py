import tkinter as tk
from tkinter import ttk

# Cria uma nova janela principal
janela = tk.Tk()
janela.title("Cotação de Moedas")
janela.configure(bg='black')  # Configura a cor de fundo da janela

# Configura a linha 0 da grade para expandir proporcionalmente
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

# Cria um estilo para os widgets
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14), background="black", foreground="white")
style.configure("TEntry", font=("Helvetica", 14))
style.configure("TButton", font=("Helvetica", 14))

# Cria um rótulo com texto, cor de fundo e de texto, largura e altura especificadas
mensagem = ttk.Label(
    janela,
    text="Sistema de Busca de Cotação de Moedas",
    style="TLabel",
    anchor="center"
)
mensagem.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)

# Cria um segundo rótulo com texto simples
mensagem2 = ttk.Label(
    janela,
    text="Selecione a moeda desejada",
    style="TLabel"
)
mensagem2.grid(row=1, column=0, sticky='e', padx=10, pady=10)

# Cria uma entrada de texto
moeda = ttk.Entry(janela)
moeda.grid(row=1, column=1, sticky='w', padx=10, pady=10)

# Cria um botão para buscar a cotação
botao = ttk.Button(janela, text="Buscar")
botao.grid(row=2, column=0, columnspan=2, pady=10)

# Cria um rótulo para mostrar o resultado da cotação
resultado = ttk.Label(janela, text="", style="TLabel")
resultado.grid(row=3, column=0, columnspan=2, pady=10)

# Inicia o loop principal da janela, permitindo que ela responda a eventos
janela.mainloop()