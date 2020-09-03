import json
import requests
import time
import locale
import configparser
import mysql.connector as mariadb
import datetime

config = configparser.ConfigParser()
config.read('config.ini')

statusURL = config.get('CONFIG', 'statusURL')

dbhost = config.get('DATABASE', 'STATS_DB_HOST')
db = config.get('DATABASE', 'STATS_DB_NAME')
dbuser = config.get('DATABASE', 'STATS_DB_USER')
dbpass = config.get('DATABASE', 'STATS_DB_PASSWORD')


dateStr=datetime.datetime.now()
dateStr=f'{dateStr:%Y-%m-%d-%h-%m}'

query="select date(a.Datetime) as 'Date', sum(a.Mons_all) as 'Mons_all', sum(a.MonsIV) as 'MonsIV', round(100*sum(a.MonsIV)/sum(a.Mons_all),1) as  'pctIV' , sum(a.Iv100) as 'Iv100', sum(a.Iv0) as 'Iv0' from stats_area a where a.RPL = 1440 and date(a.Datetime) = curdate() - interval 1 day;"
mariadb_connection = mariadb.connect(host=dbhost, user=dbuser, database=db, password=dbpass)
cursor = mariadb_connection.cursor()
cursor.execute(query)

for Date, Mons_all, MonsIV, pctIV, Iv100, Iv0 in cursor:

    dateStr="{}".format(Date)
    monsallStr="{}".format(Mons_all)
    monsivStr="{}".format(MonsIV)
    pctivStr="{}".format(pctIV)
    iv100Str="{}".format(Iv100)
    iv0Str="{}".format(Iv0)

    data = {
                "username": "StatsReport for "+dateStr+"",
                "avatar_url": "https://i.imgur.com/I4s5Z43.png",
                "embeds": [
                {
                "title": "",
                "url": "",
                "color": 8965375,
                "description": "**Mons scanned:**  "+monsallStr+" \n **IV mons:** "+monsivStr+" \n **%IV:** "+pctivStr+" \n **Hundos:** "+iv100Str+" \n **Ubernoob:** "+iv0Str+"",
                "image":
                {
        "url": ""
                }
        }]
                }

    result = requests.post(statusURL, json=data)
    print(result)
    time.sleep(1)

query="select date(a.Datetime) as 'Date', a.Area, a.Mons_all, a.MonsIV, round(100*a.MonsIV/a.Mons_all,1) as  'pctIV' , a.Iv100, a.Iv0 from stats_area a where a.RPL = 1440 and date(a.Datetime) = curdate() - interval 1 day order by a.Area;"
mariadb_connection = mariadb.connect(host=dbhost, user=dbuser, database=db, password=dbpass)
cursor = mariadb_connection.cursor()
cursor.execute(query)

for Date, Area, Mons_all, MonsIV, pctIV, Iv100, Iv0 in cursor:

    dateStr="{}".format(Date)
    areaStr="{}".format(Area)
    monsallStr="{}".format(Mons_all)
    monsivStr="{}".format(MonsIV)
    pctivStr="{}".format(pctIV)
    iv100Str="{}".format(Iv100)
    iv0Str="{}".format(Iv0)

    data = {
                "username": "StatsReport for "+areaStr+" on "+dateStr+"",
                "avatar_url": "https://i.imgur.com/I4s5Z43.png",
                "embeds": [
                {
                "title": "",
                "url": "",
                "color": 8965375,
                "description": "**Mons scanned:**  "+monsallStr+" \n **IV mons:** "+monsivStr+" \n **%IV:** "+pctivStr+" \n **Hundos:** "+iv100Str+" \n **Ubernoob:** "+iv0Str+"",
                "image":
                {
        "url": ""
                }
        }]
                }

    result = requests.post(statusURL, json=data)
    print(result)
    time.sleep(1)


mariadb_connection.close()
