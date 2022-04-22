import requests
from bs4 import BeautifulSoup




bitcoin_api_url = 'https://coinmarketcap.com/'
response = requests.get(bitcoin_api_url)
response_html = response.text
soup = BeautifulSoup(response_html, 'html.parser')
#info=list(soup.find_all("tr"))
print(list(info[1].find_all("p"))[1].get_text())
for tr in soup.find_all("tr"):

    #td=tr.find_all("td")
    info=list(tr)
    print(info[0].find_all("p")[0].get_text())
    # real_td=list(td)
    # if len(real_td)>0:
    #     #print(real_td[2])
    #     print(real_td[3]) 
