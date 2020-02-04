# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:07:05 2019

@author: guyuj
"""
import requests
from bs4 import BeautifulSoup

try:
    r = requests.get( 'https://www.bilibili.com/ranking/bangumi/13/0/3')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text
except:
    print("false")
    
lst=[]
soup = BeautifulSoup(html, 'html.parser')
for title in soup.find_all('a'):
    if title.string != None:
        lst.append(title.string)
k=0
play=[]
view=[]
fav=[]
newlst = soup.find_all('i')
while k < len(lst):
    for i in range(len(newlst)):
        if newlst[i]["class"] == ['b-icon', 'play']:
            play.append(newlst[i].next_sibling)
        elif newlst[i]["class"] == ['b-icon', 'view']:
            view.append(newlst[i].next_sibling)
        elif newlst[i]["class"] == ['fav']:
            fav.append(newlst[i].next_sibling)
        if len(play)==k+1 & len(view) == k+1 & len(fav) == k+1:
            k=k+1

