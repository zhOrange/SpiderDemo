import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup

class ABImages():
    def run(self, index):
        imagePath = "D:\\ABicons\\"
        url = 'http://sc.adminbuy.cn/icon/list_1_{}.html'.format(str(index))
        print(url)
        html = self.__request_images(url)
        if html:
            soup = BeautifulSoup(html, 'lxml')
            self.__saveImages(soup, imagePath)

    def __request_images(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        response = requests.get(url, headers = headers)
        try:
            if response.status_code == 200:
                return response.text.encode('iso-8859-1').decode('utf-8')
            else:
                return None
        except requests.RequestException:
            return None
    def __saveImages(self, soup, dirPath):
        if not soup:
            return
        originurl = 'http://sc.adminbuy.cn'
        items = soup.find(class_ = 'content').find('ul').find_all('li')
        for item in items:
            srcPath = item.find(class_ = 'fancybox').get('href')
            nameStr = item.find('p').string
            nameStr = nameStr.replace('/', '-')
            nameStr = nameStr.replace('\\', '-')
            imageContent = requests.get(originurl+srcPath)
            image = Image.open(BytesIO(imageContent.content))
            image.save(dirPath + nameStr + ".png")
