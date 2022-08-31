from tkinter import *

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

        # Adiciona uma imagem de fundo
        fundo = PhotoImage(file = 'Iamai.png')
        fundo1 = Label(janela, image = fundo)

        # Mensagem da Iamai
        label3 = Label(janela, text = f'Seja bem-vindo {nome}', font = 'Arial 40', bg = '#ffe6ff')

        # Aqui é onde o texto do usúario vai aparece quando ele digita
        usuario = StringVar()
        texto_usuario = Label(janela, textvariable = usuario, font = 'Arial 40', bg = '#66ccff')

        # Aqui é onde o usuário ira digita algo
        textbox = Entry(janela, font = 'Arial 40')

        # Função do botão enviar

        def enviar():
            global usuario
            usuario.set(textbox.get())

        # Botão de enviar mensagem
        botao1 = Button(janela, text = 'Enviar', command = enviar)

        # Colocando os objetos na tela
        fundo1.place(x=250, y=0)
        label3.place(x=252, y=0)
        texto_usuario.place(x=788, y=66)
        textbox.place(x=250, y=650, height=55, width=800)
        botao1.place(x=1050, y=650, height=55, width=102)

        janela.mainloop()

    elif len(nome) <= 5:
        erro.set('Erro seu nome\nprecisa ter no minimo\n6 caratecteris')

    else:
        erro.set('Erro sua senha está errada')

# criar a tela de login

janela1 = Tk()
janela1.iconbitmap('Iamai.ico')
janela1.title('Iamai')
janela1['bg'] = '#e65c00'
janela1.geometry('240x130+500+250')
janela1.resizable(True, True)

label1 = Label(janela1, text = 'Digite seu nome:', bg = '#e65c00') # criar uma label pendido para o usuário digita seu nome
nome_usuario = Entry(janela1) # Cria uma entrada para o usuário digita seu nome

label2 = Label(janela1, text = 'Digite sua senha:', bg = '#e65c00') # criar uma label pendido para o usuário digita sua senha
senha = Entry(janela1) # Cria uma entrada para o usuário digita sua senha

botao = Button(janela1, text = ('login'), command = tela_inicial) # criar um login

erro = StringVar()
mensagem_erro = Label(textvariable = erro, bg = '#e65c00')

# Colocando os objetos na tela

label1.grid(row = 0, column = 0)
nome_usuario.grid(row = 0, column = 1)
label2.grid(row = 1, column = 0)
senha.grid(row =1, column = 1)
botao.grid(row = 2, column = 1)
mensagem_erro.grid(row = 3, column = 1)

janela1.mainloop()