<h1 align="center">Download de arquivo CSV de uma página de Investimentos</h1>
  <br>
  <br>

<h3>Automação: <br>
  - abre a página <br>
  - Acessa a aba necessária <br>
  - realiza o download do arquivo CSV <br>
</h3>
<h1></h1>
<br>
<h5>OBS:</h5>

O download será salvo automaticamente na pasta "Downloads", caso queira editar o caminho, altere:
```bash
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": "",
  "download.prompt_for_download": False,
})
```
Para:

```bash
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": "<YOUR_PATH>",
  "download.prompt_for_download": False,
})
```

<h5>Altere o YOUR_PATH, caso utilize windows, não se esqueça de escapar as \ ou utilizar r antes do caminho, exemplo:</h5>
<h5>r"C:\Path" ou "C:\\Path"</h5>

<br>



<h3>Como Utilizar:</h3>


```
# Clonar esse repositório
$ git clone https://github.com/DennisNgrox/download_csv_python

# Acessar repositório
$ cd download_csv_python

# Instalar dependencias
$ pip install -r requirements.txt 

# Executar programa create_api.py
$ python.exe app.py
```
