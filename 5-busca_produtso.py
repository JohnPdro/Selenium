from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1 - Utilização do WebDriver
browser = webdriver.Chrome()
browser.get('https://www.amazon.com.br')

wait = WebDriverWait(browser, 15)

# 2 - Acessando elemento de pesquisa
elem = wait.until(
    EC.element_to_be_clickable((By.ID, 'twotabsearchtextbox'))
)
elem.send_keys('ps5')
elem.send_keys(Keys.ENTER)

# 3 - Encontrando os elementos de todos os resultados
element = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.s-main-slot.s-result-list.s-search-results.sg-row')
    )
)

# 4 - Encontrar informações dos produtos
items = element.find_elements(
    By.XPATH,
    './/div[@data-component-type="s-search-result"]'
)

print(len(items))

for item in items:
    title = ""
    price = ""
    link = ""
    img = ""

    try:
        title = item.find_element(By.TAG_NAME, 'h2').text
    except:
        pass

    try:
        link = item.find_element(By.CLASS_NAME, 'a-link-normal').get_attribute('href')
    except:
        pass

    try:
        price = item.find_element(By.CLASS_NAME, 'a-price').text.replace('\n', '.')
    except:
        pass

    try:
        img = item.find_element(By.CLASS_NAME, 's-image').get_attribute('src')
    except:
        pass

    print(f"Título: {title}")
    print(f"Preço: {price}")
    print(f"Link: {link}")
    print(f"Image: {img}")
    print('-' * 50)

browser.quit()