from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep

# Definindo opções de desativar o prompt de Download
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": "",
  "download.prompt_for_download": False,
})

# Executar Chrome utilizando as opções acima
driver = webdriver.Chrome(options=chrome_options)

# Acessando Site
driver.get("https://statusinvest.com.br/acoes/busca-avancada")
sleep(3)

# Clicando no botão pesquisar
pesquisa_avancada = driver.find_element(By.XPATH, "//button[@class='find waves-effect waves-light btn btn-large btn-main fw-700  fs-3 pl-2 pr-2 pl-sm-3 pr-sm-3 tooltipped']")
pesquisa_avancada.click()
sleep(3)

# Clicando no botão Download
download = driver.find_element(By.XPATH, "//a[@class='btn-download btn btn-main-green btn-small waves-effect waves-light']")
download.click()
sleep(5)

# Fechando Driver
driver.close()

