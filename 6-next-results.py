from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

with open('data_amazon.json', 'w', encoding='utf-8') as f:
    json.dump([], f, ensure_ascii=False)

def write_json(new_data, filename='data_amazon.json'):
    with open(filename, 'r+', encoding='utf-8') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4, ensure_ascii=False)

browser = webdriver.Firefox()

try:
    # 1 - Abrindo a Amazon
    browser.get('https://www.amazon.com.br')
    time.sleep(3)

    # 2 - Campo de pesquisa
    elem = browser.find_element(By.ID, 'twotabsearchtextbox')
    elem.send_keys('ps5')
    elem.send_keys(Keys.ENTER)
    time.sleep(3)

    isNextDisabled = False

    while not isNextDisabled:
        element = browser.find_element(
            By.CSS_SELECTOR,
            'div.s-main-slot.s-result-list.s-search-results.sg-row'
        )
        time.sleep(2)

        items = element.find_elements(
            By.XPATH,
            './/div[@data-component-type="s-search-result"]'
        )

        print(f'Quantidade de itens encontrados na página: {len(items)}')

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
            print(f"Imagem: {img}")
            print('-' * 50)

            write_json({
                "title": title,
                "price": price,
                "link": link,
                "image": img
            })

        try:
            next_btn = browser.find_element(By.CLASS_NAME, 's-pagination-next')
            next_class = next_btn.get_attribute('class')

            if 's-pagination-disabled' in next_class:
                isNextDisabled = True
            else:
                next_btn.click()
                time.sleep(3)

        except Exception as e:
            print("Erro ao tentar avançar para a próxima página:", e)
            isNextDisabled = True

except Exception as e:
    print("Ocorreu um erro:")
    print(e)

input("Pressione ENTER para fechar o navegador...")
browser.quit()