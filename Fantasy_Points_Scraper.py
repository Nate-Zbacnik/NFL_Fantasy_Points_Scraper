# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:31:28 2020

@author: Nate Z
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import string
import time
import random

table_list = [['Rank','Player', 'Team','Position','Points','Games','Avg','Season','Week']]

for season in range(2012,2020):
    for week in range(1,18):
        print(season,week) #always good to know how it's going
        
        # URL to format and Open
        url = r"https://www.fantasypros.com/nfl/reports/leaders/?year={season}&start={week}&end={week}"
        
        html = urlopen(url.format(season = season, week = week)) #open the URL
        
        soup = BeautifulSoup(html, 'html.parser') #extract
        
        table = soup.find('table')
        
        row_list = table.find_all('tr')[1:]
        
    
        for row in row_list:
            temp_row = row.get_text(';').split(';')
            temp_row.append(season)
            temp_row.append(week)
            table_list.append(temp_row)
        
        time.sleep(3+random.random()) #don't want to make requests too fast

for week in range(1,16):
    print(season,week) #always good to know how it's going
    
    # URL to format and Open
    url = r"https://www.fantasypros.com/nfl/reports/leaders/?year={season}&start={week}&end={week}"
    
    html = urlopen(url.format(season = 2020, week = week)) #open the URL
    
    soup = BeautifulSoup(html, 'html.parser') #extract
    
    table = soup.find('table')
    
    row_list = table.find_all('tr')[1:]
    

    for row in row_list:
        temp_row = row.get_text(';').split(';')
        temp_row.append(season)
        temp_row.append(week)
        table_list.append(temp_row)
    
    time.sleep(3+random.random()) #don't want to make requests too fast
    
player_df = pd.DataFrame(table_list[1:],columns = table_list[0])

player_df['Type'] = 'STD'

df = player_df[['Rank','Player','Team','Position','Points','Season','Week','Type']]

df = df[df['Week'].notnull()]
        
df.to_csv(r'C:\Users\Nate\.spyder-py3\CFB_Database\Fantasy_Points.csv', index = False)    