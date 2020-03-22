import user_info
import requests
import os
import json
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

mode = os.getenv('ENV')
key = os.getenv('API_KEY')
api_url = os.getenv('TESTING_API_URL') if (mode != 'prod') else os.getenv('PROD_API_URL')
api_version = os.getenv('API_VERSION')

headers = {
  'Content-Type': 'application/json',
  'auth-token': key
}

usernames = user_info.USERNAMES

for username in usernames:
  URL = 'https://leetcode.com/' + username
  page = requests.get(URL)

  soup = BeautifulSoup(page.content, 'html.parser')

  mydivs = soup.find("div", {"class": "response-container"})
  ngInitTag = mydivs['ng-init']
  tags = ngInitTag.split('pc.init(')[1]
  ranks_array = []

  try:
    ranks = tags.split('[[')[1].split(']]')[0]
    formatted_ranks = '[[' + ranks + ']]'
    temp_ranks_array = eval(formatted_ranks)
    for rank in temp_ranks_array:
      ranks_array.append(rank[0])
  except IndexError:
    ranks_array = []

  body = {
    'ranks': ranks_array
  }
  url = api_url + api_version + '/users/' + username + '/ranks'
  req = requests.post(url, data=json.dumps(body), headers=headers)
  print((username, ranks_array))