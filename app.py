from bs4 import BeautifulSoup
import os

BASE_URL = "wget 'https://www.amazon.in/s?rh=n%3A976419031%2Cn%3A!976420031%2Cn%3A1389401031'"

def getContent():
  stream = os.popen(BASE_URL)
  print('print next')
  op = stream.read()
  print(op)
  

getContent()

