from bs4 import BeautifulSoup
import requests
import csv
import os

def bas_date_kmu():
    file_path = '1_dani_po_kmu/0_bazovi_dani.csv'
    if os.path.exists(file_path) == True:
        key = []
        category = []
        service = []
        link = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file_csv:
            reader = csv.reader(file_csv, delimiter=',')
            for col in reader:
                key.append(col[0])
                category.append(col[1])
                service.append(col[2])
                link.append(col[3])
    return key[1:], category[1:], service[1:], link[1:]


if __name__ == '__main__':
    main()
