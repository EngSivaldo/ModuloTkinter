import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de Moedas")

#edicao de cores e tamanho
mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas",fg='blue', bg='red', width=50, height=10)
mensagem.pack()

mensagem2 = tk.Label(
    text="Selecione a moeda desejada", 
    fg='blue', 
    bg='gray', 
    width=50, 
    height=10, 
    padx=10, 
    pady=10
)
mensagem2.pack()

janela.mainloop()
