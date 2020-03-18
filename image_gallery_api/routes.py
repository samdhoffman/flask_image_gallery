from flask import request, jsonify
from image_gallery_api import app, ma, db
from image_gallery_api.models import Image

# Image Schema
class ImageSchema(ma.Schema):
  class Meta:
    fields = ('id', 'img_id', 'width', 'height', 'url')

# Init schema --> Have to use image schema and images schemas to deal with one or many images
image_schema = ImageSchema()
images_schema = ImageSchema(many=True)

# Get All Images
@app.route('/image', methods=['GET'])
def get_images():
  all_images = Image.query.all()
  result = images_schema.dump(all_images)
  return jsonify(result)

# Get Single Image
@app.route('/image/<id>', methods=['GET'])
def get_image(id):
  image = Image.query.get_or_404(id)
  return image_schema.jsonify(image)

# Create an Image
@app.route('/image', methods=['POST'])
def add_image():
  img_id = request.json['img_id']
  width = request.json['width']
  height = request.json['height']
  url = request.json['url']

  new_image = Image(img_id, width, height, url)

  db.session.add(new_image)
  db.session.commit()
  
  return image_schema.jsonify(new_image)

# Update an Image
@app.route('/image/<id>', methods=['PUT'])
def update_image(id):
  image = Image.query.get_or_404(id)

  img_id = request.json['img_id']
  width = request.json['width']
  height = request.json['height']
  url = request.json['url']

  image.img_id = img_id
  image.width = width
  image.height = height
  image.uri = url

  db.session.commit()
  
  return image_schema.jsonify(image)

# Delte Image
@app.route('/image/<id>', methods=['DELETE'])
def delete_image(id):
  image = Image.query.get_or_404(id)
  db.session.delete(image)
  db.session.commit()

  return image_schema.jsonify(image)