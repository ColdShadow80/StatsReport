import json
import requests
import time
import locale
import configparser
import mysql.connector as mariadb
import datetime

config = configparser.ConfigParser()
config.read('config.ini')

device_statusURL = config.get('DEVICE-STATUS-CONFIG', 'device_statusURL')

dbhost = config.get('DATABASE', 'STATS_DB_HOST')
db = config.get('DATABASE', 'STATS_DB_NAME')
dbuser = config.get('DATABASE', 'STATS_DB_USER')
dbpass = config.get('DATABASE', 'STATS_DB_PASSWORD')

dateStr=datetime.datetime.now()
dateStr=f'{dateStr:%Y-%m-%d-%h-%m}'


query="select DEVICE.name as origin,if(a.lastProtoDateTime='','Unknown',time_format(a.lastProtoDateTime,'%H:%i')) as lastProtoDateTime from trs_status a left join settings_device DEVICE on a.device_id=DEVICE.device_id where (a.lastProtoDateTime < now() - interval 10 minute or a.lastProtoDateTime = '') order by a.device_id;"
mariadb_connection = mariadb.connect(host=dbhost, user=dbuser, database=db, password=dbpass)
cursor = mariadb_connection.cursor()
cursor.execute(query)

for origin,lastProtoDateTime in cursor:

    originStr="{}".format(origin)
    protoStr="{}".format(lastProtoDateTime)

    data = {
                "username": "Alert >10min no data!!",
                "avatar_url": "https://www.iconsdb.com/icons/preview/red/exclamation-xxl.png",
                "embeds": [
                {
                "title": "",
                "url": "",
                "color": 16711680,
                "description": "__**"+originStr+"**__ last data at "+protoStr+"",
                "image": 
                {
        "url": ""
                }
        }]
                }

    result = requests.post(device_statusURL, json=data)
    print(result)
    time.sleep(1)


mariadb_connection.close()
