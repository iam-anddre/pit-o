from tkinter import *
janela=Tk()
janela.title('Entry')
janela.geometry('350x250')
janela.config(background='gray')

#Entry sereve para colocar as caixas de entradas

# para desativar uma entry, coloca na entry desejavel a variavel ('state='disable')

#funcao

def obter():
    nome = entry_nome.get()
    idade = entry_idade.get()
    pais = entry_pais.get()

    label_nome_re['text'] = nome
    label_idade_re['text'] = idade
    label_pais_re['text'] = pais

    entry_nome.delete(0, END)
    entry_idade.delete(0, END)
    entry_pais.delete(0, END)

#Nome--------------------------------------------------
label_nome = Label(janela, width=10, font=('Arial 10'),text=('Nome'), anchor='w')
label_nome.grid(row=0, column=0, padx=5, pady=5,sticky='NSEW')
entry_nome = Entry(janela, width=10, font=('Arial 10'))
entry_nome.grid(row=0, column=1, padx=5, pady=5)

#Idade-------------------------------------------------
label_idade = Label(janela, width=10, font=('Arial 10'), text=('Idade'), anchor='w')
label_idade.grid(row=1,column=0, padx=5,pady=5,sticky='NSEW')
entry_idade = Entry(janela, width=10, font=('Arial 10'))
entry_idade.grid(row=1, column=1, padx=5, pady=5)

#Pais---------------------------------------------------
label_pais = Label(janela, width=10, text=('Pais'), font=('Arial 10'), anchor='w')
label_pais.grid(row=2, column=0, padx=5, pady=5,sticky='NSEW')
entry_pais =  Entry(janela, width=10, font=('Arial 10'))
entry_pais.grid(row=2, column=1,padx=5,pady=5)

# Resposta-----------------------------------------------
label_nome_re = Label(janela, width=10, font=('Arial 10'),text=(''), anchor='w')
label_nome_re.grid(row=0, column=2, padx=5, pady=5,sticky='NSEW')

label_idade_re = Label(janela, width=10, font=('Arial 10'), text=(''), anchor='w')
label_idade_re.grid(row=1,column=2, padx=5,pady=5,sticky='NSEW')

label_pais_re = Label(janela, width=10, text=(''), font=('Arial 10'), anchor='w')
label_pais_re.grid(row=2, column=2, padx=5, pady=5,sticky='NSEW')

botao= Button(janela,command=obter,width=10, height=2, text='ver dados',relief='flat',fg='black',bg='white')
botao.grid(row=3,column=0, padx=5,pady=20)

janela.mainloop()