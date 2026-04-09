import urllib.request
import datetime
import json

client_id = '5hX4lwisxcBcdCaZ9SWz'
client_secret = '6yEEZCebEz'

def main():

    node = 'news'                                             # 크롤링할 대상
    srcText = input('검색어를 입력하세요: ')
    
                               