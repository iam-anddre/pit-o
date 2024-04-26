from tkinter import *
#existem varios estilos de butoes que podem ser apresentados no python, o 'flat' é o mais comum, o 'groove' é um pouco diferente, dura um pouco mais de tempo e tem o estilo 'solid' deixa meio que uma linha ao redor do botao, e tem o estilo 'raised' que deixa o botao um pouco saltado e tem o estilo 'sunken' que deixa o botao um pouco fundo e tem o estilo 'ridge' que deixa uma borda ao redor do botao

janela = Tk()
janela.title('Botao')
janela.geometry('300x300')

global contador
contador = 0

def executar():
    global contador

    texto_1 = 'numero impar: '
    texto_2 = 'numero par: '

    if (contador %2) == 0:
        resultado = texto_2 + str(contador)
        Label['text'] = resultado
        Label['fg'] = 'green'
    else:
        resultado = texto_1 + str(contador)
        Label['text'] = resultado
        Label['fg'] = 'red'

    contador += 1

botao= Label(janela, width=20, height=2, text='texto sera apresentado',relief='flat',fg='black',bg='white')
botao.grid(row=0,column=0, padx=10,pady=10)

botao= Button(janela,command=executar,width=10, height=2, text='clica aqui',relief='flat',fg='black',bg='white')
botao.grid(row=0,column=1, padx=5,pady=5)

janela.mainloop()