
"""This file is used for populating sqlite3 db with photos Data and group Data"""

import sqlite3
import time
import flickrapi
import requests
import urllib
import json

api_key = u'3aad6f4e25e8f7c81bf7866d8517901b'
api_secret = u'be22bfff3db1e98f'
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
groups = ['80641914@N00', '906097@N21', '96035807@N00', '34427469792@N01', '16978849@N00']
for groupid in groups:
    photos = flickr.groups.pools.getPhotos(group_id=groupid)['photos']['photo']
    conn = sqlite3.connect('infilect_project/db.sqlite3')
    c = conn.cursor()
    columns = 'id, owner, secret, server, farm, title, ispublic, isfriend, isfamily, dateadded, ownername, groupid'
    for i in photos:
        data = (i['id'], i['owner'], i['secret'], i['server'], i['farm'], i['title'],
                i['ispublic'], i['isfriend'], i['isfamily'], i['dateadded'], i['ownername'], groupid)
        c.execute(
            f"insert into flickrdb_fphoto ({columns}) values (?,?,?,?,?,?,?,?,?,?,?,?)", data)
    conn.commit()
conn = sqlite3.connect('infilect_project/db.sqlite3')
c = conn.cursor()
for groupid in groups:
    link = f'https://api.flickr.com/services/rest/?method=flickr.urls.lookupGroup&api_key=febb2a6247e2bfe3935a3bdd0ceb07fc&url=https%3A%2F%2Fwww.flickr.com%2Fgroups%2F{urllib.parse.quote(groupid)}%2F&format=json&nojsoncallback=1'
    resp = requests.get(link)
    print(resp.content)
    groupname = str(json.loads(resp.content.decode('UTF-8'))['group']['groupname']['_content'])
    photocount = c.execute('SELECT COUNT(*) FROM FLICKRDB_FPHOTO WHERE GROUPID in (?)', (groupid, )).fetchone()[0]
    c.execute(f'INSERT INTO FLICKRDB_FGROUP (groupname, noofphotos, id) VALUES (?,?,?)', (groupname, photocount, groupid, ))
    conn.commit()
time.sleep(1)
conn.close()