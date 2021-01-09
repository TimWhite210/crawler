import requests
from bs4 import BeautifulSoup
url='https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gda&tv=r20201203&st=env'
headers={
    'origin': 'https://googleads.g.doubleclick.net'
    'referer': 'https://googleads.g.doubleclick.net/'
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}
params={
    'xai': 'AKAOjssNmsB-5a04fuZtBcyhLE6Pnbd1j90A0aF55YAf1IwWO0p9IZh8uzT4qWGOeuzIX2QwelBzpayXtoj0SBw_KctnyUZN_LRAcbmjzFLqKQvEtQ4wOItruxMrlmQ'
    'sai': 'AMfl-YR0otZr_wJXTqovhXb3JOc_tKNkGce8xt77rbF7FLG218pQ_CbmHUEDcxF99eU5quXkxYjoJ1chI8Ad0aaaofe19-JYxuoQnUrjMK2MJQ'
    'sig': 'Cg0ArKJSzF47Y56Mh1YDEAE'
    'id': 'osdim'
    'mcvt': '1011'
    'p': '81,101,151.40625,859.421875''
    'mtos': '0,1011,1011,1011,1025'
    'tos': '0,1011,0,0,14'
    'v': '20210106'
    'bin': '7'
    'avms': 'nio'
    'bs': '0,0'
    'mc': '0.87'
    'if': '1'
    'app': '0'
    'itpl': '4'
    'adk': '2731441302'
    'rs': '2'
    'met': 'mue'
    'la': '0'
    'cr': '0'
    'osd': '1'
    'rst': '1610154512369'
    'dlt': '289'
    'rpt': '42'
    'isd': '0'
    'msd': '0'
    'r': 'v'
}
res=requests.get(url,headers=headers,params=params)
soup=BeautifulSoup(res.text,'html.parser')
print(soup)
