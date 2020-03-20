import requests
from bs4 import BeautifulSoup

class FilmsDouban:
    '''
    爬取豆瓣电影top250.
    '''
    def work(self, page):
        url = 'https://movie.douban.com/top250?start=' + str(page * 25) + '&filter='
        html = self.__requests_douban(url)
        if html:
            soup = BeautifulSoup(html, 'lxml')
            items = self.__save_to_excel(soup)

    def __requests_douban(self, url):
        #添加header，否则会返回 status_code = 418
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        response = requests.get(url, headers = headers)
        try:
            if response.status_code == 200:
                return response.text
            else:
                return None
        except requests.RequestException:
            return 
    
    def __save_to_excel(self, soup):
        #find:查找标签
        #get:获取标签属性
        items = soup.find(class_ ='grid_view').find_all('li')
        for item in items:
            item_title = item.find(class_ = 'title').string
            item_imgurl = item.find('img').get('src')
            item_score = item.find(class_ ='rating_num').string
            print(item_title, " ", item_score, " img = ", item_imgurl)
