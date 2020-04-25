import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, ImageColorGenerator
import numpy
import PIL.Image as Image
import jieba
import sys
import re

class BiliBiliDM:
    def run(self, bvNum):
        url = "https://www.bilibili.com/video/BV" + bvNum
        html = self.__getHtml(url)
        if not html:
            return
        cid = self.__getCid(html)
        if not cid:
            return
        dmText = self.__getDM(cid)
        if not dmText:
            return
        wordList = self.__getwordlist(str(dmText))
        resImage = self.__getwordCloud(wordList, "res/naruto.png")
        resImage.save("cloud.png")
        resImage.show()

        

    def __getHtml(self, targeturl):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        response = requests.get(targeturl, headers = headers)
        response.encoding = 'utf-8'
        try:
            if response.status_code == 200:
                return response.text
            else:
                return None
        except requests.RequestException:
            return None
    def __getCid(self, html):
        return re.findall(r'cid=(\d+)&', html)[0]
    def __getDM(self, cidNum):
        url = 'http://comment.bilibili.com/' + str(cidNum) + '.xml'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        response = requests.get(url, headers = headers)
        try:
            if response.status_code == 200:
                content = response.content
                content = str(content, 'utf-8')
                soup = BeautifulSoup(content, 'lxml')
                results = soup.find_all('d')
                dmText = [result.text for result in results]
                return dmText
            else:
                return None
        except requests.RequestException:
            return None
    def __getwordlist(self, dmText):
        words = jieba.lcut(dmText)
        spaceWords = " ".join(words)
        return spaceWords
    def __getwordCloud(self, wordlist, imagePath):
        mask_pic = numpy.array(Image.open(imagePath))
        color_func = ImageColorGenerator(mask_pic)
        wordcloud = WordCloud(font_path="res/zhsword.ttf", mask=mask_pic, color_func=color_func).generate(wordlist)
        return wordcloud.to_image()
        