from selenium import webdriver
import time
import csv
from unidecode import unidecode

driver = webdriver.Chrome(r'C:\Users\jean.santos\Desktop\chrome\chromedriver.exe')

driver.get('https://www.marabraz.com.br/nossaslojas/')

element_list = driver.find_elements_by_class_name('list-item')

v = driver.find_element_by_xpath('//*[@id="lojas"]/div[2]/div[2]/div[1]')
buttons = v.find_elements_by_class_name('bx-pager-item')

with open ('dados_marabraz.csv', 'w') as d:
    for i in range(0,len(element_list)):
        buttons[i].click()
        for loja in element_list[i].find_elements_by_class_name('item'):
            loja = loja.text.split('\n')
            loja = [unidecode(row.upper().strip()) for row in loja if row.upper().strip() not in 
                    ['ABERTO AGORA','TEL:','COMO CHEGAR:','CLIQUE AQUI']]
            if len(loja) > 4:
                d.write("|".join(loja[:3])+ "|" + ",".join(loja[3:]) + '\n')

            else:
                d.write("|".join(loja) + '\n')
        time.sleep(1)
