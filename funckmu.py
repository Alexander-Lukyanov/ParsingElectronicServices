from bs4 import BeautifulSoup
import requests
from basic_func import *
import csv
import os

def profayl_posl():
   key, category, service, link = bas_date_kmu()
   count = len(key)
   file_path = '1_dani_po_kmu/1_profayl_po_posluhakh.csv'
   if os.path.exists(file_path) == False:
      with open(file_path, mode='w', newline='', encoding='utf-8') as f:
          writer = csv.writer(f)
          writer.writerow(('Код послуги', 'Категорія послуги', 'Відповідальний орган', 'Коротка назва послуги',
                           'Повна назва послуги', 'Пов’язані послуги', 'Опис послуги', 'Найменування дії (суб послуги) 1',
                           'Спосіб електронної ідентифікації дії 1', 'Посилання на дію (суб послугу) 1', 'Найменування дії (суб послуги) 2',
                           'Спосіб електронної ідентифікації дії 2', 'Посилання на дію (суб послугу) 2', 'Як отримати послугу 1',
                           'Як отримати послугу 2', 'Вартість послуги 1', 'Вартість послуги 2', 'Строки надання послуги',
                           'Результат послуги', 'Нормативна база'))
   for i in range(0, count):
       nom1 = 0 # Номер послуги для опису її отримання, а також номер способу електронної ідентифікації
       nom2 = 0 # Номер послуги для опису її вартості
       pn = '' # Повна назва послуги
       pname = '' # Пов’язані послуги
       ou = '' # Опис послуги
       url1 = '' # Посилання на дію (суб послугу) 1
       url2 = '' # Посилання на дію (суб послугу) 2
       nurl1 = '' # Найменування дії (суб послуги) 1
       nurl2 = '' # Найменування дії (суб послуги) 2
       ei1 = '' # Спосіб електронної ідентифікації дії 1
       ei2 = '' # Спосіб електронної ідентифікації дії 2
       op1 = '' # Як отримати послугу 1
       op2 = '' # Як отримати послугу 2
       snp = '' # Строки надання послуги
       vp1 = '' # Вартість послуги 1
       vp2 = '' # Вартість послуги 2
       rp = '' # Результат послуги
       vor = '' # Відповідальний орган
       norm = '' # Нормативна база
       ss = requests.Session()
       html = ss.get(link[i]).text
       soup = BeautifulSoup(html, 'lxml')
       pn = soup.find(class_='page-content news__wrapper').find('p').text.strip()
       h_all = soup.find(class_='page-content news__wrapper').find_all('h2')
       h = soup.find(class_='page-content news__wrapper').find('h2')
       ht = h.text.strip()
       for tx in h_all:
           if ht == 'Опис послуги':
               p = h.find_next_sibling("p")
               for i1 in range(0, 12):
                   st1 = str(p)[0:3]
                   st2 = str(p)[3:12]
                   if ((st1 == '<p>' or st1 == '<ul' or st1 == '<p ') and st2 != '<a class='):
                       ou = ou + p.text.strip() + '\n'
                   else:
                       break
                   p = p.find_next_sibling()
               ou = ou.strip()
           if ht == 'Як отримати послугу?':
               p = h.find_next_sibling("p")
               for i1 in range(0, 10):
                   st1 = str(p)[0:3]
                   if st1 == '<p>':
                       op1 = op1 + p.text.strip() + '\n'
                   else:
                       break
                   p = p.find_next_sibling()
               op1 = op1.strip()
           if (ht == 'Як отримати послугу' and nom1 == 0):
               p = h.find_next_sibling("p")
               for i1 in range(0, 10):
                   st1 = str(p)[0:3]
                   if (st1 == '<p>' or st1 == '<p '):
                       op1 = op1 + p.text.strip() + '\n'
                   else:
                       break
                   p = p.find_next_sibling()
               nom1 = 1
               op1 = op1.strip()
           elif (ht == 'Як отримати послугу' and nom1 == 1):
               p = h.find_next_sibling("p")
               for i1 in range(0, 10):
                   st1 = str(p)[0:3]
                   st2 = str(p)[3:12]
                   if (st1 == '<p>' and st2 != '<a class='):
                       op2 = op2 + p.text.strip() + '\n'
                   else:
                       break
                   p = p.find_next_sibling()
               nom1 = 2
               op2 = op2.strip()
           if (ht == 'Строки надання послуги' or ht == 'Строк надання послуги'):
               p = h.find_next_sibling("p")
               for i1 in range(0, 10):
                   st1 = str(p)[0:3]
                   if (st1 == '<p>' or st1 == '<p '):
                       snp = snp + p.text.strip() + '\n'
                   else:
                      break
                   p = p.find_next_sibling()
               snp = snp.strip()
           if ht == 'Вартість послуг':
               p = h.find_next_sibling("p")
               for i1 in range(0, 10):
                   st1 = str(p)[0:3]
                   if (st1 == '<p>' or st1 == '<p '):
                       vp1 = vp1 + p.text.strip() + '\n'
                   else:
                       break
                   p = p.find_next_sibling()
               vp1 = vp1.strip()
           if (ht == 'Вартість послуги' and nom2 == 0):
               p = h.find_next_sibling("p")
               for i1 in range(0, 10):
                   st1 = str(p)[0:3]
                   if st1 == '<p>':
                       vp1 = vp1 + p.text.strip() + '\n'
                   else:
                       break
                   p = p.find_next_sibling()
               nom2 = 1
               vp1 = vp1.strip()
           elif (ht == 'Вартість послуги' and nom2 == 1):
               p = h.find_next_sibling("p")
               for i1 in range(0, 10):
                   st1 = str(p)[0:3]
                   if st1 == '<p>':
                       vp2 = vp2 + p.text.strip() + '\n'
                   else:
                       break
                   p = p.find_next_sibling()
               nom2 = 2
               vp2 = vp2.strip()
           if ht == 'Результат послуги':
               p = h.find_next_sibling("p")
               for i1 in range(0, 10):
                   st1 = str(p)[0:3]
                   if (st1 == '<p>' or st1 == '<p '):
                       rp = rp + p.text.strip() + '\n'
                   else:
                       break
                   p = p.find_next_sibling()
               rp = rp.strip()
           if ht == 'Відповідальний орган':
               p = h.find_next_sibling("p")
               for i1 in range(0, 10):
                   st1 = str(p)[0:3]
                   if (st1 == '<p>' or st1 == '<p '):
                       vor = vor + p.text.strip() + '\n'
                   else:
                       break
                   p = p.find_next_sibling()
               vor = vor.strip()
           if ht == 'Нормативна база':
               p = h.find_next_sibling("p")
               for i1 in range(0, 10):
                   st1 = str(p)[0:3]
                   if (st1 == '<p>' or st1 == '<p '):
                       norm = norm + p.text.strip() + '\n'
                   else:
                       break
                   p = p.find_next_sibling()
               norm = norm.strip()
           h = h.find_next_sibling('h2')
           if h == None:
               break
           ht = h.text.strip()

       url = soup.find(class_='page-content news__wrapper').find_all('a', class_='online-mss-btn')
       i1 = 0
       for ur in url:
           if i1 == 0:
               url1 = ur.get('href')
               nurl1 = ur.text
               i1 = i1 + 1
           elif i1 == 1:
               url2 = ur.get('href')
               nurl2 = ur.text

       p = soup.find(class_='page-content news__wrapper').find_all('p')
       nom1 = 0
       for tx in p:
           st1 = tx.text[0:32]
           if (st1 == 'Спосіб електронної ідентифікації' and nom1 == 0):
               ei1 = tx.text[34:].strip()
               nom1 = 1
           elif (st1 == 'Спосіб електронної ідентифікації' and nom1 == 1):
               ei2 = tx.text[37:].strip()
       pvz1 = soup.find(class_='sidebar').find(class_='title')
       st1 = pvz1.text.strip()
       if st1 == 'Пов’язані послуги:':
           pvz2 = soup.find(class_='sidebar').find('ul').find_all('a')
           for pvz in pvz2:
               pname = pname + pvz.text.strip() + '\n'
           pname = pname.strip()
       with open(file_path, mode='a', newline='', encoding='utf-8') as f:
           writer = csv.writer(f)
           writer.writerow((key[i], category[i], vor, service[i], pn, pname, ou, nurl1, ei1, url1, nurl2,
                            ei2, url2, op1, op2, vp1, vp2, snp, rp, norm))
   return


def napovnennya_posl():
   key, category, service, link = bas_date_kmu()
   count = len(key)
   file_path = '1_dani_po_kmu/2_napovnennya_posluhy.csv'
   if os.path.exists(file_path) == False:
      with open(file_path, mode='w', newline='', encoding='utf-8') as f:
          writer = csv.writer(f)
          writer.writerow(('Код послуги', 'Категорія послуги', 'Коротка назва послуги',
                           'Перелік заголовків послуги', 'Число заголовків послуги', 'Посилання на сторінку послуги'))
   for i in range(0, count):
       ss = requests.Session()
       html = ss.get(link[i]).text
       soup = BeautifulSoup(html, 'lxml')
       zagl = ''
       l = 0
       h_all = soup.find(class_='page-content news__wrapper').find_all('h2')
       for tx in h_all:
           zagl = zagl + tx.text.strip() + '\n'
           l = l + 1
       zagl = zagl.strip()
       with open(file_path, mode='a', newline='', encoding='utf-8') as f:
           writer = csv.writer(f)
           writer.writerow((key[i], category[i], service[i], zagl, l, link[i]))


if __name__ == '__main__':
    main()
