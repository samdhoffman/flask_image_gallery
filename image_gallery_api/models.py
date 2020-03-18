from image_gallery_api import db

# Image Class/Model
class Image(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  img_id = db.Column(db.Integer)
  width = db.Column(db.Integer)
  height = db.Column(db.Integer)
  url = db.Column(db.String(100), unique=True, nullable=False)

  # constructor for Image class
  def __init__(self, img_id, width, height, url):
    self.img_id = img_id
    self.width = width
    self.height = height
    self.url = url

  # how our Image resource object is printed/represented in terminal output
  def __repr__(self):
    return f"Image('{self.img_id}', '{self.url}', '{self.height}', '{self.width}')"