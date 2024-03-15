import pyautogui
import pandas
import time

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("microsoft edge")
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=881, y=353)
pyautogui.write("nicolasbetim014@gmail.com")
pyautogui.press("tab")
pyautogui.write("urubu0898")
pyautogui.press("tab")
pyautogui.press("enter")
tabela = pandas.read_csv("produtos.csv")
print(tabela)
for linhas in tabela.index:
    pyautogui.click(x=795, y=242)
    codigo = tabela.loc[linhas, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linhas, "marca"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linhas, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linhas, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linhas, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linhas, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linhas, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    