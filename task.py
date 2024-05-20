import requests
from bs4 import BeautifulSoup
chart_range = ['1', '2', '3']
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

startNum = 1
for num in chart_range:
    site = f'https://genie.co.kr/chart/top200?ditc=D&ymd=20240520&hh=12&rtm=Y&pg={num}'
    request = requests.get(site, headers=header)
    # print(request)
    soup = BeautifulSoup(request.text, 'html.parser')
    titles = soup.findAll('a', {'class': 'title ellipsis'})
    artist = soup.findAll('a', {'class': 'artist ellipsis'})

    for i, (t,a) in enumerate(zip(titles, artist)):
        title = t.text.strip()
        artist = a.text.strip().split('\n')[0]
        print(f'{i+startNum}위. {title} - {artist}')
    startNum += 50