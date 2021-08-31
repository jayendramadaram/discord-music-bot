import urllib.request
from bs4 import BeautifulSoup
import re
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=hey+there")
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
print("https://www.youtube.com/watch?v=" + video_ids[0])
# for i in tag:
#     print()
#     print()
#     print()
#     print(i.get('href'))
print()
print()
# print(tag.get('href'))
