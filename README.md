# flask_image_gallery
Image Gallery API using Flask

**Steps to Get Started**
1. Clone the project
2. Set up your database with the following steps:
  * While in the project's root directory, enter python interactive mode in your terminal by entering `python3`
  * Enter the following commands:
    1. `from image_gallery_api import db` (this will create a db.sqlite file in the image_gallery_api directory)
    2. `db.create_all()`
   
  * Optional: please note that if you want to work with the database while in the terminal, you will need to enter the following command to use the Image model:
   `from image_gallery_api.models import Image`
  * Exit interactive mode by typing `exit()`
  
3. While still in the root directory, create the `images.csv` file by running `python3 scripts/create_csv.py`
4. Populate the previously created database with the `images.csv` data by running `python3 scripts/db_insert.py`
5. Run `python3 run.py` to start the server and you are ready to go!
