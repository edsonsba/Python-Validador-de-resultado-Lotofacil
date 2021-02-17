from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import warnings
import smtplib

warnings.filterwarnings("ignore")
warnings.warn("deprecated", DeprecationWarning)
chrome_options = Options()
chrome_options.add_argument("--headless")
pagina = webdriver.Chrome ('C:\\Users\\Edson\\Documents\\Python Scripts\\chromedriver.exe', chrome_options=chrome_options)

pagina.get("https://www.somatematica.com.br/lotofacilResultados.php?estatisticas=1")   
Sorteio = pagina.find_element_by_xpath("//*[@id='content']/section/table[1]/tbody/tr[2]/td/div").text
Concurso = pagina.find_element_by_xpath("//*[@id='content']/section/table[1]/tbody/tr[1]/td/div/strong").text

sorteio2 = Sorteio.replace("\n"," ")
lista = sorteio2.split(" ")
Aposta=['01','03','04','05','07','08','09','10','14','17','18','19','21','22','25']

result = list(set(Aposta) - set(lista))
resultado = 15 - len(result)

gmail_user = 'xxxxxxxxx'   # add user e-mail
gmail_password = 'xxxxxxx' # add senha e-mail
me = "xxxxxxxx" # add seu e-mail
you = "xxxxxxx" # add destinatario

msg = MIMEMultipart('alternative')
msg['Subject'] =  f" {resultado} acertos do {Concurso}"
msg['From'] = me
msg['To'] = you

text = f"Aposta, {Aposta}\nSorteio, {lista}"
part1 = MIMEText(text, 'plain')
msg.attach(part1)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
try:
    server.login(gmail_user, gmail_password)
    server.sendmail(me, you, msg.as_string())
    server.quit()
    print('E-mail enviado com sucesso!')
except:
    print('Não enviado...')