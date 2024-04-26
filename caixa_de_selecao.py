from tkinter.ttk import *
from tkinter import *


janela = Tk()

janela.title('Caixa de selecao')
janela.geometry('300x250')
janela.config(background='black')

label_nome = Label(janela, width=15, height=2, text='escolha', font='Arial 10')
label_nome.grid(row=0, column=0, padx=5, pady=5)

def obter():
    resultado = combo.get
    print(resultado)

botao = Button(janela,command=obter, width=10, height=1, text='resposta', bg='white')
botao.grid(row=2, column=0, padx=5, pady=20)

#definindo valores para combobox
combo = Combobox(janela)
combo['values'] = (1,2,3,4)
combo.current(0)

combo.grid(row=1, column=0, padx=5, pady=5)



janela.mainloop()