import tkinter as tk

janela = tk.Tk()

#titulo da janela
janela.title("Cotação de Moedas")

#criar objeto
mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas")
#coloca msg na janela do tkinter
mensagem.pack()


#criar objeto
mensagem2 = tk.Label(text="Selecione a moeda desejada")
#coloca msg na janela do tkinter
mensagem2.pack()



janela.mainloop()

