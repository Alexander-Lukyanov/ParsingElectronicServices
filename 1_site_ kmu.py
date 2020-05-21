from bs4 import BeautifulSoup
import requests
import csv
import os

# ============== Завантаження базових значень з порталу КМУ =================

def main():
   ss = requests.Session()
   html = ss.get('https://www.kmu.gov.ua/ua/servicesfilter').text
   soup = BeautifulSoup(html, 'lxml')
   kat_name = []
   id1 = []
   file_path = '1_dani_po_kmu/0_bazovi_dani.csv'
   if os.path.exists(file_path) == False:
      with open(file_path, mode='w', newline='', encoding='utf-8') as f:
          writer = csv.writer(f)
          writer.writerow(('№ п/п', 'Категорія послуги', 'Назва послуги', 'Посилання на сторінку порталу КМУ'))
   spis1 = soup.find(class_="nav nav-tabs").find_all('li')
   for st in spis1:
       st1 = st.get('name')
       st2 = st.get('id')
       if st1:
           kat_name.append(st1)
           id1.append(st2)
   i = i1 = 0
   for st1 in id1:
       n = soup.find(id=st1).find(class_='list hidden-lg hidden-md hidden-sm').find_all('span')
       l = soup.find(id=st1).find(class_='list hidden-lg hidden-md hidden-sm').find_all('a')
       max1 = len(l)
       for i2 in range(0, max1):
           nazv1 = n[i2].text.strip()
           link1 = l[i2].get('href')
           with open(file_path, mode='a', newline='', encoding='utf-8') as f:
               writer = csv.writer(f)
               writer.writerow((i+1, kat_name[i1], nazv1, link1))
           i = i + 1
       i1 = i1 + 1

if __name__ == '__main__':
    main()

