# CardMarket_scrap

Módulos Python:\
    - beautifulSoup4 (pip install beautifulsoup4)\
    - requests (pip install requests)

Web scrapping app that let's the user check if a given username in CardMarket site have the required cards of a given deck. Made for Commander decks.

Steps:\
Export txt file from Tappedout or create a txt file with the following format:\
[number of copies] [Card Name]\
Example:\
1 Acidic Soil\
1 Arcane Signet\
1 Bend or Break\
1 Blasphemous Act\
1 Burning Earth

Last line souldn't be an empty line.

Save the file under Decks dir.

In main change the following stuff:\
    f = open('Decks/[Deck name].txt','r')\
    TotalUrl = 'https://www.cardmarket.com/en/Magic/Users/[CardMarket user]/Offers/Singles?name=' + finalCard

Run\
\
\
What's missing:\
    - All deck formats\
    - User input\
    - More dynamic(deck choice based on dir content)\
    - Check if card that a user sells have a good price according to the avg?\
    - Total price sum of search\
    - Excel output ??\
    - Some sort of UI for programming muggles
