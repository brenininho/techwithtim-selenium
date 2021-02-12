import ipdb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions

chromeOptions = ChromeOptions()
chromeOptions.add_argument("--window-size=1300,1000")

PATH = "./chromedriver"
driver = webdriver.Chrome(PATH, chrome_options=chromeOptions)

driver.get("https://www.techwithtim.net/")

# ipdb.set_trace()
pesquisa = driver.find_element_by_name("s")
pesquisa.send_keys("tutorial")
pesquisa.send_keys(Keys.RETURN)
articles = driver.find_elements_by_tag_name("article")
for i, article in enumerate(articles):
    descricao = article.find_element_by_tag_name("p").text
    print("")
    print(f"{i + 1} {descricao}")

while True:
    escolha = int(input(f'escolha um assunto: '))

    if escolha > len(articles):
        print(f'Escolha um número de 1 a {len(articles)}')
    else:
        article_escolhido = articles[escolha - 1]
        print(article_escolhido.find_element_by_tag_name("p").text)
        break

article_pergunta = input("deseja saber mais sobre o assunto (sim/não)?").lower()

if article_pergunta == "sim":
    article_escolhido.find_element_by_tag_name("a").click()

