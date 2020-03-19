import csv

# Used to create csv file from pastebin images raw string data
images = """https://picsum.photos/id/12/300/200
https://picsum.photos/id/434/300/200
https://picsum.photos/id/966/300/200
https://picsum.photos/id/637/300/200
https://picsum.photos/id/180/300/200
https://picsum.photos/id/342/300/200
https://picsum.photos/id/467/300/200
https://picsum.photos/id/389/300/200
https://picsum.photos/id/525/300/200
https://picsum.photos/id/385/300/200
https://picsum.photos/id/256/100/100
https://picsum.photos/id/70/100/100
https://picsum.photos/id/844/100/100
https://picsum.photos/id/130/100/100
https://picsum.photos/id/328/100/100
https://picsum.photos/id/886/100/100
https://picsum.photos/id/218/100/100
https://picsum.photos/id/29/100/100
https://picsum.photos/id/639/100/100
https://picsum.photos/id/396/100/100
https://picsum.photos/id/20/250/250
https://picsum.photos/id/925/250/250
https://picsum.photos/id/872/250/250
https://picsum.photos/id/629/250/250
https://picsum.photos/id/1074/250/250
https://picsum.photos/id/341/250/250
https://picsum.photos/id/267/250/250
https://picsum.photos/id/1021/250/250
https://picsum.photos/id/928/250/250
https://picsum.photos/id/238/250/250
https://picsum.photos/id/385/400/200
https://picsum.photos/id/319/400/200
https://picsum.photos/id/1059/400/200
https://picsum.photos/id/71/400/200
https://picsum.photos/id/637/400/200
https://picsum.photos/id/118/400/200
https://picsum.photos/id/634/400/200
https://picsum.photos/id/1065/400/200
https://picsum.photos/id/1073/400/200
https://picsum.photos/id/323/400/200
https://picsum.photos/id/660/300/300
https://picsum.photos/id/511/300/300
https://picsum.photos/id/339/300/300
https://picsum.photos/id/693/300/300
https://picsum.photos/id/198/300/300
https://picsum.photos/id/964/300/300
https://picsum.photos/id/59/300/300
https://picsum.photos/id/160/300/300
https://picsum.photos/id/737/300/300
https://picsum.photos/id/891/300/300"""

data = images.splitlines()

with open('/Users/sam/Sites/image_gallery_api/data/images.csv', 'w', newline='') as csvfile:
    header = ['images']
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)

    for image in data:
        csv_writer.writerow([image])


# Used in python interactive mode to add csv images to db
with open('/Users/sam/Sites/image_gallery_api/data/images.csv','r', newline='') as csvfile:
    next(csvfile)
    
    csv_reader = csv.reader(csvfile)
    
    START_INDEX = 25
    
    for row in csv_reader:
        cur_img_url = row[0]
        vals = cur_img_url[START_INDEX:]
        
        # get id, width, and height from url
        img_data = tuple([int(x) for x in vals.split('/')])
        
        img_for_db = Image(img_id=img_data[0],width=img_data[1],height=img_data[2],url=cur_img_url)
        
        # db available in interacitve mode after importing
        db.session.add(img_for_db)
        db.session.commit()
