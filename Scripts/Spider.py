from FilmsDouban import FilmsDouban
import requests
import time
from SeleniumDemo import SeleniumDemo
from ABImages import ABImages

if __name__ == '__main__':
    img = ABImages()
    for i in range(1, 15):
        time.sleep(1)
        img.run(i)