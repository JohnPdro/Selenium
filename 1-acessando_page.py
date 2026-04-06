from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Faz com que o Chrome permaneça aberto mesmo após o fim do script
options = Options()
options.add_experimental_option("detach", True)

# 1 - Utilizando o WebDriver
browser = webdriver.Chrome(options=options)
browser.get('https://www.amazon.com.br')

# Define uma espera de até 15 segundos
wait = WebDriverWait(browser, 15)

# 2 - Acessando elementos em uma página
campo_busca = wait.until( # Espera até que o elemento 'twotabsearchtextbox' exista
    EC.element_to_be_clickable((By.ID, 'twotabsearchtextbox'))
)

campo_busca.send_keys('ps5')
campo_busca.send_keys(Keys.ENTER)