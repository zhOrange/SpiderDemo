import requests;
import re
import json

class DangBook:

    def work(self, page):
        url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-" + str(page)
        html = self.request_dang(url)
        items = self.parse_html(html)
        for item in items:
            #print(item)
            self.write_item_to_file(item)
    #获取response
    def request_dang(self, url):
        response = requests.get(url)
        try:
            if response.status_code == 200:
                return response.text
            else:
                return None
        except requests.RequestException:
            return None

    # 解析html
    def parse_html(self, html):
        pattern = re.compile('<li>.*?list_num.*?(\d+).*?"name".*?title="(.+?)".*?"star".*?target.*?>(\d+).*?publisher_info.*?title="(.*?)".*?publisher_info.*?<a.*?target.*?>(.*?)</a>.*?<span.*?price_n">&yen;(.*?)</span>.*?</li>',re.S)
        #pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src=".*?".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
        items = re.findall(pattern,html)
        for item in items:
            yield {
            'range': item[0],
            'title': item[1],
            'star':item[2],
            'author': item[3],
            'publisher':item[4],
            'price': item[5]
            }
    def write_item_to_file(self, item):
        print('开始写入数据 ====> ' + str(item))
        with open('booklist.txt', 'a', encoding='UTF-8') as f:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
            f.close()

# if __name__ == '__main__':
#     book = DangBook()
#     for i in range(10):
#         book.work(i)