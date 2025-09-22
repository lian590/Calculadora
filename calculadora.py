import tkinter as tk
from PIL import Image, ImageTk  # importando o Pilloww


# cria a janela 
janela = tk.Tk()
janela.title("Calculadora simples")
janela.geometry("360x480")


# Define o icone da janela 
icon =Image.open("logo.png")
icon = icon.resize((32, 32))
janela.iconphoto(False, ImageTk.PhotoImage(icon))


# Campo de entrada no display
entrada = tk.Entry(janela, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Funçao dos botoes
def adicionar(valor):
    entrada.insert(tk.END, valor)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

def limpar():
    entrada.delete(0, tk.END)



# Criando os botoes baseiado em matriz

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), 
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), 
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), 
    ('C', 5, 0),
]



for (texto, linha, coluna) in botoes:
    if texto == '=':
        cmd = calcular
    elif texto == 'C':
        cmd = limpar
    else:
        cmd = lambda x=texto: adicionar(x)


    tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18), command=cmd)\
    .grid(row=linha, column=coluna, padx=5, pady=5)
    


# Inicia o loop da inteface
janela.mainloop()