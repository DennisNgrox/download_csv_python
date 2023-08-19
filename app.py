from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep


chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": "",
  "download.prompt_for_download": False,
})

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://statusinvest.com.br/acoes/busca-avancada")
sleep(3)

pesquisa_avancada = driver.find_element(By.XPATH, "//button[@class='find waves-effect waves-light btn btn-large btn-main fw-700  fs-3 pl-2 pr-2 pl-sm-3 pr-sm-3 tooltipped']")
pesquisa_avancada.click()
sleep(3)

download = driver.find_element(By.XPATH, "//a[@class='btn-download btn btn-main-green btn-small waves-effect waves-light']")
download.click()
sleep(5)

driver.close()

