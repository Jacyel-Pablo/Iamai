from tkinter import *
from os import getlogin
import chatterbot.preprocessors
from Iamai import iamai
from PIL import Image

# essa parte está em desenvolvimento a imagem de fundo
# ira se ajusta de acordo com o tamnho do monito
#altura1 = 0
#lagura1 = 0

#def ajustando_iamgem():
    #global altura1
    #global lagura1

    #janela_imagem = Tk()
    #lagura1 = janela_imagem.winfo_screenwidth()
   # altura1 = janela_imagem.winfo_screenheight()
  #  janela_imagem.destroy()
 #   janela_imagem.mainloop()

#ajustando_iamgem()

#Mundado a iamgem para o tamanho da tela

#abrir_imagem = Image.open('Iamai.png')

#largura2, altura2 = abrir_imagem.size

#nova_largura = lagura1 // 2

#nova_altura = altura1

#abrir_imagem = abrir_imagem.thumbnail((nova_largura, nova_altura), Image.LANCZOS)

#abrir_imagem.save('Iamai(1).png',
        #quality = 60,
        #exif = abrir_imagem.info.get('exif')

contagem = 0
def tela_inicial():
    global erro
    global janela1
    global nome_usuario
    global senha
    global usuario

    nome = nome_usuario.get().strip()
    senha1 = senha.get().strip()

    if senha1 == '123' and len(nome) >= 6:
        janela1.destroy()
        janela = Tk()
        janela.state('zoomed')
        janela.geometry('900x821')
        janela.iconbitmap('Iamai.ico')
        janela.title('Iamai')

        # altura é lagura do monitor
        altura = janela.winfo_screenheight()
        lagura = janela.winfo_screenwidth()
        lagura1 = (lagura / 2) - 400
        altura1 = (altura / 2) - 397

        # Adiciona uma imagem de fundo
        fundo = PhotoImage(file = 'Iamai.png')
        fundo1 = Label(janela, image = fundo)

        # Mensagem da Iamai
        iamai_text = StringVar()
        iamai_text.set(f'Seja bem-vindo {getlogin()}')
        mensagem_iamai = Label(janela, textvariable = iamai_text, font = 'Arial 40', bg = '#ffe6ff', bd = 1, relief='solid', anchor = 'w')

        # Aqui é onde o texto do usúario vai aparece quando ele digita
        usuario = StringVar()
        texto_usuario = Label(janela, textvariable = usuario, font = 'Arial 40', bg = '#66ccff', bd = 1, relief='solid', anchor = 'w')

        # Aqui é onde o usuário ira digita algo
        textbox = Entry(janela, font = 'Arial 40')

        # Função do botão enviar

        def enviar():
            global usuario
            global contagem

            usuario.set(textbox.get())
            text = textbox.get()

            iamai(text, iamai_text, contagem)
            contagem += 1

        # Botão de enviar mensagem
        botao1 = Button(janela, text = 'Enviar', command = enviar)

        # Colocando os objetos na tela
        fundo1.place(x=lagura1, y=altura1)
        mensagem_iamai.place(x=lagura1, y=66)
        texto_usuario.place(x=lagura1 + 535, y = 0)
        textbox.place(x=lagura1, y=650, height=55, width=800)
        botao1.place(x=lagura1 + 700, y=650, height=55, width=102)

        janela.mainloop()

    elif len(nome) <= 5:
        erro.set('Erro seu nome\nprecisa ter no minimo\n6 caratecteris')

    else:
        erro.set('Erro sua senha está errada')

def cadrasto():
    janela1.destroy()
    root = Tk()
    root.iconbitmap('Iamai.ico')
    root.geometry('500x500+500+250')
    root.title('Faça o cadrasto para usa o sistema Iamai')
    root['bg'] = '#e65c00'

    # Mensagem digite seu nome
    label3 = Label(root, text = 'Digite seu nome:', bg = '#e65c00')

    # entrada para o usuário digita o nome
    textbox1 = Entry(root)

    # Mensagem digite sua senha
    label4 = Label(root, text = 'Digite sua senha', bg = '#e65c00')

    # entrada de senha do usuário
    senha1 = Entry(root)

    # confimação da senha do usuário texto
    label5 = Label(root, text = 'Digite sua senha', bg = '#e65c00')

    # confimação da senha do usuário
    textbox2 = Entry(root)

    # botao de cadrasto
    botao_cadrasto1 = Button(root, text = 'Cadrasta')

    # Adicionado objetos na tela
    label3.place(x = 0, y = 0, width = 234)
    textbox1.place(x = 0, y = 21, height = 20, width = 234)
    label4.place(x = 0, y = 42, width = 234)
    senha1.place(x = 0, y = 63, height = 20, width = 234)
    label5.place(x = 0, y = 84, width = 234)
    textbox2.place(x = 0, y = 105, height = 20, width = 234)
    botao_cadrasto1.place(x = 60, y = 130)

    root.mainloop()

# criar a tela de login

janela1 = Tk()
altura = janela1.winfo_screenheight()
lagura = janela1.winfo_screenwidth()
altura /= 2
altura = int(altura)
lagura /= 2
lagura = int(lagura)
janela1.iconbitmap('Iamai.ico')
janela1.title('Iamai')
janela1['bg'] = '#e65c00'
janela1.geometry(f'240x130+{lagura - 120}+{altura - 65}') # +500+250
janela1.resizable(False, False)

label1 = Label(janela1, text = 'Digite seu nome:', bg = '#e65c00') # criar uma label pendido para o usuário digita seu nome
nome_usuario = Entry(janela1) # Cria uma entrada para o usuário digita seu nome
nome_usuario.focus()

label2 = Label(janela1, text = 'Digite sua senha:', bg = '#e65c00') # criar uma label pendido para o usuário digita sua senha
senha = Entry(janela1) # Cria uma entrada para o usuário digita sua senha

botao = Button(janela1, text = ('login'), command = tela_inicial) # criar um login

# Esse Botão leva o usuario para a tela de cadrasto
botao_cadrasto = Button(janela1, text = 'Cadraste-se', command = cadrasto)

erro = StringVar()
mensagem_erro = Label(textvariable = erro, bg = '#e65c00')

# Colocando os objetos na tela

label1.grid(row = 0, column = 0)
nome_usuario.grid(row = 0, column = 1)
label2.grid(row = 1, column = 0)
senha.grid(row =1, column = 1)
botao.grid(row = 2, column = 1)
botao_cadrasto.grid(row = 2, column = 0)
mensagem_erro.grid(row = 3, column = 1)

janela1.mainloop()