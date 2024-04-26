from tkinter import *

janela=Tk()

#Label é 

janela.title('label')

janela.geometry('300x250')

Label_nome = Label(janela,width=10,height=2, text='nome: ', font=('Arial 15'), fg='red', padx=10)#serve para colocar uma caixa de texto dentro da janela
# wight é a largura da janela e height é a altura da janela
#font usa-se para alterar a fonte 
#fg é pra mudar a cor da fonte
#bg serve para mudar a cor de fundo da caixa de texto
#pady serve para add uma margem

Label_nome.grid(row=0, column=0)#serve para posicionar a caixa de texto da janela

Label_idade = Label(janela, width=10, height=2, text='idade: ', font=('Arial 15'),pady=10)
Label_idade.grid(row=1,column=0)

label_pais = Label(janela, width=10,height=2,text='pais', font=('Arial 15'), pady=10)
label_pais.grid(row=2,column=0)



janela.resizable(width=False,height=False)

janela.mainloop()