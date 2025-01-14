import time
import pyautogui 
import pandas

pyautogui.PAUSE = 0.5 # definição do tempo de espera entre as chamadas do pyautogui
pyautogui.FAILSAFE = True # para abortar a operação, colocar o ponteiro do mouse no canto superior esquerdo

# abrir o navegador 
pyautogui.hotkey('winleft', 'a') # atalho para abrir central de aplicativos no linux
time.sleep(1)
pyautogui.write("firefox")
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

# entrar no website
pyautogui.click(720, 90) # os valores em pixeis foram conseguidos através do arquivo teste.py    
pyautogui.typewrite('https://dlp.hashtagtreinamentos.com/python/intensivao/login', 0.005) # url utilizado para automação com um intervalo de atuação para não comprometer dados com a velocidade
pyautogui.press('enter') 

# fazer o login
pyautogui.click(900, 400)
pyautogui.write('pythonimpressionador@gmail.com')
pyautogui.press('tab')
pyautogui.write('sua senha')
pyautogui.press('tab')
pyautogui.press('enter')

# cadastrar produtos
tabela = pandas.read_csv('/home/nyelton-gomes-faustino/Área de trabalho/Main Py/Projeto1/produtos.csv') # variável tabela recebe o banco de dados de produtos.csv

for linha in tabela.index: # loop para leitura de todos os itens da tabela
    pyautogui.click(950,290)
    codigo = tabela.loc[linha, 'codigo'] # localização da infomação a partir da referência da linha e da chave 
    pyautogui.typewrite(str(codigo), 0.005) # escrita da informação encontrada na tabela 
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.typewrite(str(marca), 0.005)
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.typewrite(str(tipo), 0.005)
    pyautogui.press('tab')

    categoria = tabela.loc[linha, 'categoria']
    pyautogui.typewrite(str(categoria), 0.005)
    pyautogui.press('tab')

    custo = tabela.loc[linha, 'custo']
    pyautogui.typewrite(str(custo), 0.005)
    pyautogui.press('tab')

    custo = tabela.loc[linha, 'custo']
    pyautogui.typewrite(str(custo), 0.005)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan': # criação de uma verificação para validar se a informação da observação está vazia (nan) ou não
        pyautogui.typewrite(obs, 0.005)

    pyautogui.press('tab')
    pyautogui.press('enter') # envio do produto até o fim do loop com a última linha de dados da tabela