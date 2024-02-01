import requests
from bs4 import BeautifulSoup
import lxml


#url = "https://www.flipkart.com/intex-it-xm-bang-sufb-78-w-bluetooth-home-theatre/p/itm25359525afb95?pid=ACCF2WXKQFFKGFFY&lid=LSTACCF2WXKQFFKGFFYLQEBNO&marketplace=FLIPKART&store=0pm&srno=b_1_1&otracker=clp_omu_Best%2BOf%2BHeadphones%2B%2526%2BSpeakers_2_9.dealCard.OMU_elec-the-big-billions-days-23-store_elec-the-big-billions-days-23-store_VMX4T89UDQ3Q_6&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Best%2BOf%2BHeadphones%2B%2526%2BSpeakers_NA_dealCard_cc_2_NA_view-all_6&fm=neo%2Fmerchandising&iid=en_HA0JeheiKaAf6szXwBtw596A_NKW0eQed4-gXGD4emZzcmzCly5v_qb556GTlMNx-uNl2AKQXuDa42FBkoH18Q%3D%3D&ppt=clp&ppn=elec-the-big-billions-days-23-store&ssid=x0avzo7hls0000001697380181899"
def get_link_data(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8",
    }

    r= requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")


    name = soup.select_one(selector=".B_NuCI").getText()
    name = name.strip()
    price = soup.select_one(selector="._16Jk6d").getText()
    price = price.replace(",", "")
    price = float(str(price[1:]))
    images = soup.select('div img') 
    images_url = images[0]['src'] 
  
    return name ,price ,images_url


