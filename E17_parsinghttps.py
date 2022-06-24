import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def parsing_https(url):
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')
    return soup


if __name__ == "__main__":
    ur = 'https://www.dolarhoy.com/'
    soup = parsing_https(ur)

    price = soup.find_all('span', attrs={'class': 'price'})
    # price = soup.find_all('h3', attrs={'class': 'post-full-price'})
    # Devuelve una lista que contiene todos los h1 que sean clasificados con el attrs

    # prices = soup.h1.string
    # esta es otra forma de sacar el primer h1 e imprimirlo con el .string
    dollar = []
    if len(price) > 0:
        for item in price:
            dollar.append(item.text.strip())
            # print(item.text)
    else:
        print("No prices found")
    print(dollar)

    '''
    #Me saco los titulos
    name = soup.find_all('h4')
    nombres = ['Fecha']
    for nombre in name:
        nombres.append(nombre.text.strip())
        nombres.append('')
    print(nombres)
    
    # Hace el compra-venta
    cv = ['']
    for i in range(4):
        cv.append("Compra")
        cv.append("Venta")
    cv.append("Compra")
    print(cv)
    '''

    with open('index.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        '''
        writer.writerow(nombres)
        writer.writerow(cv)
        '''
        writer.writerow([datetime.now()] + dollar)

