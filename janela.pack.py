#o pack coloca cada widget em cima do outro

from tkinter import *

janela=Tk()

janela.title('pack')
janela.geometry('300x300')

label_nome=Label(janela, width=10, height=2, text='Nome')
label_nome.pack()

label_idade=Label(janela, width=10, height=2, text='Idade')
label_idade.pack()

label_pais=Label(janela, width=10, height=2, text='Pais')
label_pais.pack()

janela.mainloop()