import tkinter as tk

janela = tk.Tk()

janela.title("Cotaçao de Moedas")

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text="Sistema de Busca de Cotaçao de Moedas", fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

moeda = tk.Entry()
moeda.grid(row=1, column=1)


#dicionario simula api moeda
dicionario_cotacoes = {
  'Dolar': 5.70,
  'Euro': 6.70,
  'Libra': 8.70,
  
}
#funcao que pega o texto do campo moeda ao clicar no botao
def buscar_cotacao():
  moeda_pesquisada = moeda.get()
  cotacao_moeda = dicionario_cotacoes.get(moeda_pesquisada)
  mensagem_resposta = tk.Label(text="Cotação não encontrada!")
  mensagem_resposta.grid(row=3, column=1)
  if cotacao_moeda:
    mensagem_resposta['text'] = f'Cotação do {moeda_pesquisada} é de {cotacao_moeda} $Reais'


botao = tk.Button(text="Buscar cotação!", command=buscar_cotacao)
botao.grid(row=3, column=0)

janela.mainloop()


