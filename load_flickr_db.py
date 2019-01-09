import sqlite3

import flickrapi

api_key = u'3aad6f4e25e8f7c81bf7866d8517901b'
api_secret = u'be22bfff3db1e98f'
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
photos = flickr.groups.pools.getPhotos(group_id='80641914@N00')
conn = sqlite3.connect('infilect_project/db.sqlite3')
c = conn.cursor()
columns = 'id, owner, secret, server, farm, title, ispublic, isfriend, isfamily, dateadded, ownername'
photos = photos['photos']['photo']
for i in photos:
    data = (i['id'], i['owner'], i['secret'], i['server'], i['farm'], i['title'],
            i['ispublic'], i['isfriend'], i['isfamily'], i['dateadded'], i['ownername'])
    c.execute(
        f"insert into flickrdb_photo ({columns}) values (?,?,?,?,?,?,?,?,?,?,?)", data)
conn.commit()
