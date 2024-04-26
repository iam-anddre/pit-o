from tkinter import*

conemetro = Tk()

conemetro.title()
conemetro.geometry('300x200')
conemetro.config(background='black')
conemetro.resizable(width=FALSE, height=FALSE)

global tempo
global rodar
global contador
global limitador

limitador = 59

tempo = "00:00:00"
rodar = False
contador = -5



def inciar():
    global tempo
    global contador
    global limitador

    if rodar:
        if contador <= -1:
            inicio = 'Começando em ' +str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10'

        else:
            label_tempo['font'] = 'Times 50 bold'
            temporaria =str(tempo)
            h,m,s = map(int, temporaria.split(":"))
            h = int(h)
            m = int(m)
            s = int(contador)

            if (s >= limitador):
                contador = 0
                m += 1
            
            s = str(0)+str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)

            temporaria = str(h[-2:])+":" + str(m[-2:])+":" + str(s[-2:])
            label_tempo['text'] = temporaria
            tempo = temporaria


        label_tempo.after(1000,inciar)
        contador +=1

def start():
    global rodar
    rodar = True
    inciar()

def pausar():
    global rodar
    rodar = False

def reiniar():
    global contador
    contador = 0
    global tempo
    tempo = "00:00:00"
    label_tempo['text'] = tempo




# LABELS------------------------------
label_app = Label(conemetro, text='Conometro', font=('Arial 10'), bg='black', fg='white')
label_app.place(x=20, y=5)

label_tempo = Label(conemetro, text=tempo, font=('Times 50 bold'), bg='black', fg='blue')
label_tempo.place(x= 20,y=25)

# Botoes-----------------------------------------
botao_iniciar = Button(conemetro, command=start, text=('Iniciar'), width=10, height=2, bg='black', fg='white', font=('Ivy 8 bold'))
botao_iniciar.place(x=20, y=130)

botao_pausar = Button(conemetro, command=pausar, text=('Pausar'), width=10, height=2, bg='black',fg='white', font=('Ivy 8 bold'))
botao_pausar.place(x=105, y=130)

botao_reiniciar = Button(conemetro,command=reiniar, text=('Reiniciar'), width=10, height=2, bg='black',fg='white', font=('Ivy 8 bold'))
botao_reiniciar.place(x=190, y=130)


conemetro.mainloop()