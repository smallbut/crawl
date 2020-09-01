import re
import time
import random

import HDR
import 입출력
import requests

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def 구동():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  return webdriver.Chrome(options=chrome_options)


def 빠른수프(주소, 태그, 속성="class", 속성값, findAll=False):
  bs = BeautifulSoup( requests.get(주소).text , "html.parser" )

  if findAll:
    zz = bs.findAll(태그, {속성:속성값})
  else:
    zz = bs.find(태그, {속성:속성값})

  return zz
