from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc 

navegador = uc.Chrome()
navegador.get("https://www.olx.com.br/")
navegador.maximize_window()

botao_quero_clicar = navegador.find_element(By.CSS_SELECTOR, "button[data-ds-component='DS-Button']")
botao_quero_clicar.click()

# Aguarde até que o elemento esteja presente na página
anunciar_gratis = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.olx-button.olx-button--primary.olx-button--medium.olx-button--a.olx-header__desapegar-button")))
anunciar_gratis.click()

entrarnaconta = navegador.find_element(By.ID, "input-1").send_keys("rafaelbestoption@gmail.com")
continuar_entrar_na_conta = WebDriverWait(navegador,3).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.olx-button.olx-button--primary.olx-button--medium.olx-button--fullwidth")))
continuar_entrar_na_conta.click()

time.sleep(3)
selecionar_senha_entrar_na_conta = navegador.find_elements(By.CSS_SELECTOR, "div.sc-bWjmDF.jzEKvf")
for botao in selecionar_senha_entrar_na_conta:
    if "Senha" in botao.text:
        botao.click()
        break

senha_entrar_na_conta = navegador.find_element(By.ID, "password-input").send_keys("Guiomar1!")
continuar_senha_entrar_na_conta = WebDriverWait(navegador,3).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "olx-button.olx-button--primary.olx-button--medium.olx-button--fullwidth")))
continuar_entrar_na_conta.click()

time.sleep(5)
clicar_cloudflare = navegador.find_element(By.CSS_SELECTOR, "div#success span#success-text")

'''
Não foi aplicado    
clicar_cloudflare = WebDriverWait(navegador,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "success-circle")))
clicar_cloudflare.click()'''

time.sleep(10)