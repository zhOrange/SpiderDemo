from FilmsDouban import FilmsDouban
import requests
import time
from SeleniumDemo import SeleniumDemo
from ABImages import ABImages
from BiliBiliDM import BiliBiliDM

if __name__ == '__main__':
    '''
    main.
    '''
    # img = ABImages()
    # for i in range(1, 15):
    #     time.sleep(1)
    #     img.run(i)
    dm = BiliBiliDM()
    dm.run("1Y4411L7d9")