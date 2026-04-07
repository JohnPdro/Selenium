from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Faz com que o Chrome permaneça aberto mesmo após o fim do script
options = Options()
options.add_experimental_option("detach", True)

# 1 - Acessando o site
browser = webdriver.Chrome(options=options)
browser.get('https://registro.br')

# Define uma espera de até 15 segundos
wait = WebDriverWait(browser, 15)

# 2 - Lista de Domínios
domains = [
    'botscompython.com.br',
    'meta.com',
    'databot.com',
    'pythonbootcamp.com'
]

file = open('domains.txt', 'w', encoding='utf-8')

# 3 - Manipulando elementos
for domain in domains:
    elem = wait.until( # Espera até que o elemento 'is-avail-field' exista
        EC.element_to_be_clickable((By.ID, 'is-avail-field'))
    )
    elem.clear()
    elem.send_keys(domain)
    elem.send_keys(Keys.ENTER)
    time.sleep(5)
# 4 - Buscando informações
    results = browser.find_elements(By.TAG_NAME, 'strong')
    text = f'Domínio {results[1].text} está {results[2].text}\n'
    file.write(text)

file.close()
browser.close()

