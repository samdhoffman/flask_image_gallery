# This script can be used to add csv images to db
import csv
import sqlite3

conn = sqlite3.connect('./image_gallery_api/db.sqlite')
cur = conn.cursor()

with open('./data/images.csv','r', newline='') as csvfile:
    next(csvfile)
    
    csv_reader = csv.reader(csvfile)
    
    # TODO: make dynamic
    START_INDEX = 25
    
    for row in csv_reader:
        cur_img_url = row[0]
        vals = cur_img_url[START_INDEX:]
        
        # get id, width, and height from url
        img_data = tuple([int(x) for x in vals.split('/')])
        img_id=img_data[0]
        width=img_data[1]
        height=img_data[2]
        url=cur_img_url
        to_db = (img_id, width, height, url)
        cur.execute("INSERT INTO image (img_id, width, height, url) VALUES (?, ?, ?, ?);", to_db)
        conn.commit()

    conn.close()
     