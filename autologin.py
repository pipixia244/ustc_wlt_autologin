import requests
from bs4 import BeautifulSoup
import urllib.parse
USERNAME=xxxxxx
PASSWORD=xxxxxx

choice=1
url='http://wlt.ustc.edu.cn/cgi-bin/ip'
open_url='http://wlt.ustc.edu.cn/cgi-bin/ip?cmd=set&url=URL&type={}&exp=0&go=+%BF%AA%CD%A8%CD%F8%C2%E7+'.format(str(choice))

session = requests.Session()
ret = session.get(url=url, allow_redirects=False)

rettext = ret.text
rettext = rettext.encode('ascii','ignore').decode('utf-8','ignore')
soup = BeautifulSoup(rettext, 'html.parser')
token = soup.find("input", {"name": "ip"})['value']
print(token)

ret = session.get(url="http://wlt.ustc.edu.cn/cgi-bin/ip?cmd=login&url=URL&ip={}&name={}&password={}&go=%B5%C7%C2%BC%D5%CA%BB%A7".format(token, USERNAME, urllib.parse.quote(PASSWORD)))
ret = session.get(open_url)