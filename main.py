import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}


def buscaritem(busca):
    url = (f'https://www.google.com/search?q={busca}&source=lnms&tbm=shop&')
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    itemname = soup.find_all(class_='sh-np__product-title translate-content')
    lojas = soup.find_all(class_='E5ocAb')
    precos = soup.find_all(class_='T14wmb')
    links = soup.find_all(class_='shntl sh-np__click-target')

    lojatranfer = ['Loja']
    itemtranfer = ['item']
    precotranfer = ['Preço']
    linktransfer =['link']

    for items in itemname:
        itemtranfer.append(items.get_text())
    for loja in lojas:
        lojatranfer.append(loja.get_text())
    for preco in precos:
        precotranfer.append(preco.get_text()[:10])
    for link in links:
        linktransfer.append('https://www.google.com'+link.get('href'))

    data = list(zip(itemtranfer, lojatranfer, precotranfer, linktransfer))

    df = pd.DataFrame(data)
    #print(df)
    caminho = os.getcwd()
    df.to_excel(fr'{caminho}/Orçamento de {item}.xlsx', index=False)
    print('orçamento completo')

choice = 's'
while choice == 's' or 'S':
    choice = input('nova busca ? (S)/(N) ')
    if choice == 's' or choice == 'S':
        item = input('Qual item deseja buscar ? ')
        buscaritem(item)
    else:
        break
