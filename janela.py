from tkinter import *

janela = Tk()

janela.iconphoto(False, PhotoImage(file='python-logo.png'))#Serve para colocar a logo da janela

janela.title('Ola mundo') #serve para colocar o titulo

janela.geometry('300x250') #serve para definir o tamanho da janela. O primeiro valor é a largura e o segundo valor é a altura

janela.config(background='black') #serve para alterar algumas configurações da janela e usa a tag background para mudar o fundo

janela.resizable(width=False,height=False)#Assim nao é possivel alterar o tamanho da janela

janela.mainloop() #serve para manter a janela aberta ate o usuario fechar e SEMPRE tem que ter isso no final do codigo