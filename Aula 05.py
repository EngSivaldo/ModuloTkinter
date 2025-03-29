import tkinter as tk

# Cria uma nova janela principal
janela = tk.Tk()

# Define o título da janela(tela principal)
janela.title("Cotação de Moedas")


# Configura a linha 0 da grade para expandir proporcionalmente com a tela
janela.rowconfigure(0, weight=1)

# Configura as colunas 0 e 1 da grade para expandir proporcionalmente com a tela
janela.columnconfigure([0, 1], weight=1)

# Cria um rótulo com texto, cor de fundo e de texto, largura e altura especificadas
mensagem = tk.Label(
    text="Sistema de Busca de Cotação de Moedas", 
    fg='white', 
    bg='black', 
    width=35, 
    height=5
)
# Posiciona o rótulo na/ linha 0,/ coluna 0,/ ocupando duas colunas /expandindo em todas as direções( sticky='nsew')
mensagem.grid(row=0, column=0, columnspan=2, sticky='nsew')

# Cria um segundo rótulo com texto simples
mensagem2 = tk.Label(text="Selecione a moeda desejada", fg='red', 
    bg='blue',)
# Posiciona o segundo rótulo na linha 1, coluna 0
mensagem2.grid(row=1, column=0, sticky='nsew')

# Cria uma entrada de texto
moeda = tk.Entry()
# Posiciona a entrada de texto na linha 1, coluna 1
moeda.grid(row=1, column=1)


def buscar_cotacao():
    pass


botao = tk.Button(text="buscar cotacao", command=buscar_cotacao)
botao.grid(row=3, column=1)


# Inicia o loop principal da janela, permitindo que ela responda a eventos
janela.mainloop()









# Explicação das mudanças e funções:
# Importação do módulo tkinter:

# import tkinter as tk: Importa o módulo tkinter e o renomeia como tk para facilitar o uso.
# Criação da janela principal:

# janela = tk.Tk(): Cria uma nova instância da janela principal.
# Definição do título da janela:

# janela.title("Cotação de Moedas"): Define o título da janela como "Cotação de Moedas".
# Configuração da grade:

# janela.rowconfigure(0, weight=1): Configura a linha 0 para expandir proporcionalmente.
# janela.columnconfigure([0, 1], weight=1): Configura as colunas 0 e 1 para expandir proporcionalmente.
# Criação e posicionamento do primeiro rótulo:

# mensagem = tk.Label(...): Cria um rótulo com texto, cores, largura e altura especificadas.
# mensagem.grid(row=0, column=0, columnspan=2, sticky='nsew'): Posiciona o rótulo na linha 0, coluna 0, ocupando duas colunas e expandindo em todas as direções.
# Criação e posicionamento do segundo rótulo:

# mensagem2 = tk.Label(text="Selecione a moeda desejada"): Cria um segundo rótulo com texto simples.
# mensagem2.grid(row=1, column=0): Posiciona o segundo rótulo na linha 1, coluna 0.
# Criação e posicionamento da entrada de texto:

# moeda = tk.Entry(): Cria uma entrada de texto.
# moeda.grid(row=1, column=1): Posiciona a entrada de texto na linha 1, coluna 1.
# Início do loop principal:

# janela.mainloop(): Inicia o loop principal da janela, permitindo que ela responda a eventos.