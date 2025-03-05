from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

navegador = webdriver.Chrome()
navegador.get("https://bestoptionnotebook.lojazap.com/")
navegador.maximize_window()

def pagina_iphones():
#selecionar um elemento na tela find_element() apenas um lemento e find_elements() vários elementos
    botao_comprar = navegador.find_element("class name","dropdown")
    botao_comprar.click()

    acessar_menu_de_categorias = WebDriverWait(navegador,3).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Iphones")))
    acessar_menu_de_categorias.click()

    produto = navegador.find_element(By.CLASS_NAME, "produto")
    produto.click()

    
    #extraindo o título, armazendando em uma varável e criando um arquivo txt com o w a opção de escrita nesse arquivo criado.
    extrair_titulo = navegador.find_element(By.CLASS_NAME, "title-icon").text
    extrair_descricao = navegador.find_element(By.CLASS_NAME, "descricao").text
    elementos_extraidos = [extrair_titulo , extrair_descricao]

    #extraidos e colocados em uma lista
    with open("informa.csv", "w", encoding= 'utf-8') as arquivo:
            arquivo.write("\n".join(elementos_extraidos))


def pagina_videogame():
    botao_comprar = navegador.find_element("class name","dropdown")
    botao_comprar.click()

    acessar_menu_de_categorias = WebDriverWait(navegador,3).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Vídeo Game")))
    acessar_menu_de_categorias.click()

    produto = navegador.find_element(By.CLASS_NAME, "produto")
    produto.click()

    extrair_titulo = navegador.find_element(By.CLASS_NAME, "title-icon").text
    extrair_descricao = navegador.find_element(By.CLASS_NAME, "descricao").text
    elementos_extraidos = [extrair_titulo , extrair_descricao]

    #extraidos e colocados em um dicionário de dados   
    elementos_extraidos = {'Título': extrair_titulo , 'Descrição': extrair_descricao}
    with open("informacao.csv", "w", encoding="utf-8") as arquivo:
        for chave, valor in elementos_extraidos.items():
            arquivo.write(f"{chave} : {valor}\n")

pagina_iphones()
pagina_videogame()
navegador.quit()
