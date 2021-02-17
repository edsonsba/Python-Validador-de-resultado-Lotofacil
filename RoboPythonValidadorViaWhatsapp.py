#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import warnings
import smtplib
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

options = Options()
options.add_argument("--user-data-dir=chrome-data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome('C:\\Users\\Edson\\Documents\\Python Scripts\\chromedriver.exe', options=options)
driver.maximize_window()
driver.get('https://web.whatsapp.com')  # Already authenticated
time.sleep(20)

driver.find_element_by_xpath("//*[@title='+55 19 99931-4547']").click()
driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(f" Oi Edson, tudo bem contigo ?\nRobôEdy aqui passando para dizer o resultado da lotofacil do {Concurso}, você teve {resultado} de acertos \nNúmerios sorteados {lista}")
driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
time.sleep(10)
driver.close()


# In[ ]:




