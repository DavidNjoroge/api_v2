from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url='http://www.bbc.co.uk/sport/football/scores-fixtures'

def livescore():
    print('start loading')
    
    uClient = uReq(my_url)
    page_html=uClient.read()
    uClient.close()
    print('finnished loading')
    page_soup = soup(page_html,"html.parser")

    li=page_soup.findAll("li",{"class":"gs-u-pb-"})

    matches_list=[]
    for match in li:
        col=match.findAll("span",{"class":"gs-u-display-none"})
        matchDict={"home":col[0].text,"away":col[1].text}
        matches_list.append(matchDict)

    print(matches_list)
    return matches_list