import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog

Hit_Int = 0
count = 0

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

f = open(file_path,'r')
for line in f:
    if line == '\n':
        break
    lineSplitted = line.split('1')
    card = lineSplitted[1].split('\\n')[0]
    card = card[1:int(len(card) - 1)]
    cardSplitted = card.split(' ')
    finalCard = ''
    i = 0
    for cardElem in cardSplitted:
        if finalCard == '':
            finalCard = cardSplitted[i]
        else:
            finalCard = finalCard + '+' + cardSplitted[i]
        i += 1
    #TotalUrl = 'https://www.cardmarket.com/en/Magic/Users/voodoo-pt/Offers/Singles?name=' + finalCard
    TotalUrl = 'https://www.cardmarket.com/en/Magic/Users/CardsCentral/Offers/Singles?name=' + finalCard

    page = requests.get(TotalUrl)

    soup = BeautifulSoup(page.content, "html.parser")

    Hits = soup.find("span", {"class": "total-count"})
    if Hits != None:
        Hit = Hits.contents[0]
        Hit_Int = int(Hit)

    if Hit_Int >= 1:
        Price = soup.find("span", {"class": "font-weight-bold color-primary small text-right text-nowrap"})
        Price_content = Price.contents[0]
        print(card + ' ' + Price_content + ' ' + TotalUrl)
        count += 1

    Hit_Int = 0

print('Total Cartas: ' + str(count))
    


    