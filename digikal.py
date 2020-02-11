import urllib.request
from urllib.error import HTTPError
import bs4 as bs
import lxml
import concurrent.futures 

source1 = 'dkp-1479322'
source2 = 'dkp-891419'
source3 = 'dkp-184483'


    
def getPrice(urlCode):
    source_url = 'https://www.digikala.com/product/{}'.format(urlCode)
    req = urllib.request.Request(source_url, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
    urlSource = urllib.request.urlopen(req).read()
    soup = bs.BeautifulSoup(urlSource, 'lxml')
    sellPrice = int(soup.find_all("div", class_ = 'c-product__seller-price-raw js-price-value')[0].string.strip().replace(',',''))
    try:
        originalPrice = int(soup.find_all("div", class_ = 'c-product__seller-price-prev js-rrp-price')[0].string.strip().replace(',',''))
    except:
        originalPrice = sellPrice
    if originalPrice != sellPrice:
        disc = ((originalPrice - sellPrice) / originalPrice)*100
        return source_url, sellPrice , originalPrice , disc

    
urlCodeList = ['dkp-1479322','dkp-891419','dkp-184483']

def testfunction(test):
    print(test)

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = executor.map(getPrice,urlCodeList)
        for i in result:
            if i:
                print(i)
# except HTTPError as err:
#     c = err.read()
#     print('error.')
#     with open('sss.html', 'wb') as ee:
#         ee.write(c)