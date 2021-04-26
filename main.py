from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def gooogle_url(keyword):
    url = 'https://www.google.com/search?q='+keyword+'&tbm=isch'
    print(url)
    return url

def google_image(keyword, num_of_image):
    print("1")
    response = urlopen(Request(gooogle_url(keyword), headers={'User-Agent': 'Mozilla/5.0'}))
    soup = BeautifulSoup(response, 'html.parser') 
    print(soup)
    images = soup.find_all("div", attrs={'class':'islrc'})
    print(images)
    print(len(images))
    for i in range(0, num_of_image):
        print('{}: {}'.format(i+1, images[i]['src']))

google_image('dog', 4)

# 구글은 동적페이지라 sellenium 써야된단다... 그냥시험끝나고합시다