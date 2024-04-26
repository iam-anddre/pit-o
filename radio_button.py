from tkinter import *

janela = Tk()

janela.title('primeiro botao radio')
janela.geometry('300x200')

def obter():
    resultado = radio_1.get()
    print(resultado)

selecionado_1 = IntVar()
selecionado_2 = BooleanVar()
selecionado_3 = StringVar()

radio_1 = Radiobutton(janela, text='Primeiro', value=1)
radio_1.grid(row=0, column=0)

radio_2 = Radiobutton(janela, text='Segundo', value=2)
radio_2.grid(row=1, column=0)

radio_3 = Radiobutton(janela, text='Terceiro', value=3)
radio_3.grid(row=2, column=0)



janela.mainloop()