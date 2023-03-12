import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog

Hit_Int = 0
count = 0
TotalPrice = 0
DecimalPrice = 0
LowestPriceCheck = False

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

print('1) Search Commander Deck')
print('2) Search Commander Deck with lowest price check')
print('3) Search Normal Deck - not implemented')
#print('3) Search Commander Deck')

Choice = int(input())
if Choice == 1 or Choice == 2:
    print('Insert CardMarket user: ')
    UserName = input()  #Username example: CardsCentral, voodoo-pt

if Choice == 2:
    LowestPriceCheck = True

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
        
    TotalUrl = 'https://www.cardmarket.com/en/Magic/Users/' + UserName + '/Offers/Singles?name=' + finalCard

    page = requests.get(TotalUrl)

    soup = BeautifulSoup(page.content, "html.parser")

    Hits = soup.find("span", {"class": "total-count"})
    if Hits != None:
        Hit = Hits.contents[0]
        Hit_Int = int(Hit)

    if Hit_Int >= 1:
        Price = soup.find("span", {"class": "font-weight-bold color-primary small text-right text-nowrap"})
        Price_content = Price.contents[0]
        PriceContentString = Price_content.split(' ')[0]
        PriceContentString = PriceContentString.replace(',','.')
        TotalPrice += float(PriceContentString)
        if not LowestPriceCheck:
            print(card + ' ' + Price_content + ' ' + TotalUrl)
        else:
            PriceCheckUrl = 'https://www.cardmarket.com/en/Magic/Products/Search?idCategory=0&idExpansion=0&searchString=' + card +'&idRarity=0&sortBy=price_asc&perSite=30'
            page = requests.get(PriceCheckUrl)
            soup = BeautifulSoup(page.content, "html.parser")
            
            LowestPrice = soup.find("div", {"id": "productRow364044"})
            print('Card: ' + card + '| User Price:  ' + Price_content + '| Lowest Price: ' + LowestPrice + '| Url: ' + TotalUrl)
            
            
        count += 1

    Hit_Int = 0

print('Total Cartas: ' + str(count))
print('Preço total: ' + str(TotalPrice) + '€')
    


    