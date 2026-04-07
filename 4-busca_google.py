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

# 1 - Termo de pesquisa
term = input('Digite o que deseja:\n')

# 2 - Iniciando o Driver
browser = webdriver.Chrome(options=options)
browser.get('https://www.google.com.br/')

# Define uma espera de até 15 segundos
wait = WebDriverWait(browser, 15)

# 3 - Encontrando o elemento
elem = wait.until( # Espera até que o elemento "//textarea[@aria-label='Pesquisar']" exista
    EC.element_to_be_clickable((By.XPATH, "//textarea[@aria-label='Pesquisar']"))
)

# 4 - Enviando termo para pesquisa
elem.send_keys(term)
elem.send_keys(Keys.ENTER)

# 5 - Retornando a Qtd de Registros
time.sleep(2)
results = browser.find_element(By.ID, 'result-stats').text
print(f'Foram encontrados {results}')

browser.quit()