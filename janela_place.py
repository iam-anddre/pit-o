#diferenças entre o place, pack e grid
# place usa coordenadas absolutas em pixels usando a variavel X(horizontal) e Y (vertical)

# pack coloca os widgets em um dos lados

# grid coloca os widgets em uma grade semelhante a uma planilha

from tkinter import *

janela = Tk()

janela.title('Place')

janela.geometry('300x300')

label_nome=Label(janela, width=10, height=2, text='Nome')
label_nome.place(x=10, y=10)
nome=Label(janela, width=10, height=2, text='Dede')
nome.place(x=69, y=10)


label_idade=Label(janela, height=2, width=10, text='Idade')
label_idade.place(x=10,y=60)
idade=Label(janela, height=2, width=10, text='XVIII')
idade.place(x=69,y=60)

label_pais=Label(janela, width=10, height=2, text='Pais')
label_pais.place(x=10,y=120)
pais=Label(janela, width=10, height=2, text='Brazil')
pais.place(x=69,y=120)

janela.mainloop()