#grip organiza os widget em forma de tabela, divido em ROW (LINHA) e COLLUMN (COLUNA)

from tkinter import *

janela=Tk()

janela.title('Grid')
janela.geometry('300x300')

label_nome=Label(janela, width=10, height=2, text='Nome')
label_nome.grid(row=1, column=1)
nome=Label(janela, width=10, height=2, text='dede')
nome.grid(row=1, column=2)

label_idade=Label(janela, width=10, height=2, text='Idade')
label_idade.grid(row=2, column=1)
idade=Label(janela, width=10, height=2, text='18')
idade.grid(row=2, column=2)

label_pais=Label(janela, width=10, height=2, text='pais')
label_pais.grid(row=3, column=1)
pais=Label(janela, width=10, height=2, text='Brazil')
pais.grid(row=3, column=2)

janela.mainloop()