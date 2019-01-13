#!/usr/bin/env python
# coding: utf-8

# In[139]:


from selenium import webdriver
import time
from unidecode import unidecode


# In[140]:


driver = webdriver.Chrome('C:/Users/Jean/Documents/Python Scripts/chromedriver.exe')


# In[141]:


driver.get('https://www.marabraz.com.br/nossaslojas/')


# In[142]:


texto = driver.find_elements_by_class_name('list-item')


# In[143]:


ind = driver.find_elements_by_class_name('item')


# In[144]:


but = driver.find_element_by_xpath('//*[@id="lojas"]/div[2]/div[2]/div[1]')


# In[145]:


button = but.find_elements_by_class_name('bx-pager-item')


# In[149]:


for i in range(0,len(texto)):
    button[i].click()
    for loja in texto[i].find_elements_by_class_name('item'):        
        loja = loja.text.split("\n")
        loja = [unidecode(jea.upper().strip()) for jea in loja if jea.upper().strip()not in 
                    ['ABERTO AGORA','TEL:','COMO CHEGAR:','CLIQUE AQUI','FECHADO AGORA']]
        if len(loja) > 4:
            print("|".join(loja[:3]) + "|" + ",".join(loja[3:]) +"\n")
                  
        else:
            print("|".join(loja)+'\n')
                
        
    time.sleep(1)


# In[ ]:





# In[107]:


driver.quit()


# In[ ]:





# In[ ]:




