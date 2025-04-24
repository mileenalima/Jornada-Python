# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pyautogui.write -> escrever um texto 
# pyautogui.click -> clicar com o mouse 
# pyautogui.press -> apertar uma tecla 
# pyautogui.hotkey -> apertar um atalho de teclado (Ctrl, C)


import pyautogui
import time 

pyautogui.PAUSE = 3
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


# Passo 2: Fazer login no sistema
 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# quero pausar por 3 segundos 
time.sleep(8)
pyautogui.click( x=400 , y= 372 )
pyautogui.write("mileenaliima@hotmail.com")
pyautogui.press("tab")
pyautogui.write("89865")

# apertar o botão de login 
pyautogui.click(x = 665 , y = 536 )
time.sleep(8)


# Passo 3: Importar a base de dados 
# pandas.read -> ler 
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)





linha = 0 
#para cada linha da minha tabela 
for linha in tabela.index:
    # selecionar o primeiro campo 
    pyautogui.click(x=413, y=261)
    # texto = string = str()
    # codigo 
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # custo 
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    #clicar no botão enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)




# Passo 5: Repetir o processo de cadastro até acabar os produtos 

