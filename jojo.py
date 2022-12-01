from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import csv
import time
st = time.time()

f=open('JoJo.txt', 'r')
final_arr = []
for i in f.readlines():
    i_og = i
    if('The' in i):
        i = i.split()
        l = len(i[0])
        i = i[1]+' '+i[0][:l-1]
    i = i.split()
    i = '_'.join(i)
    text = requests.get('https://jojowiki.com/'+i).text
    soup = BeautifulSoup(text,'lxml')
    try:
        ns = soup.find('div', {'data-source':'namesake'}).text
        ns = ns.strip()
        ns = ns.split()
        ns = ns[1:]
        ns = ' '.join(ns)
        print(i_og+' - '+ns)
    except:
        print(i_og + " - Couldn't find")
        ns = 'Error'
    final_arr.append([i_og,ns])
with open('stands.csv','w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Name', 'Namesake'])
    csvwriter.writerows(final_arr)
et = time.time()
elapsed = et-st
print('Took ' + elapsed + ' seconds')