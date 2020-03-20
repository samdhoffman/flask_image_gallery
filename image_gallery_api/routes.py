from flask import request, jsonify
from image_gallery_api import app, ma, db
from image_gallery_api.models import Image

# Image Schema --> defines our output format for Marshmallow serialization
class ImageSchema(ma.Schema):
  class Meta:
    fields = ('id', 'img_id', 'width', 'height', 'url')

# Init schema --> Have to use image schema and images schemas to deal with one or many images
image_schema = ImageSchema()
images_schema = ImageSchema(many=True)

# Get All Images Paginated
@app.route('/image', methods=['GET'])
def get_images():
  page = request.args.get('page', 1, type=int)
  images = Image.query.paginate(page=page)
  result = images_schema.dump(images.items)
  return jsonify(images=result, pages=images.pages)

# Get Single Image
@app.route('/image/<id>', methods=['GET'])
def get_image(id):
  image = Image.query.get_or_404(id)
  return image_schema.jsonify(image)

# Get Images Filtered By Dimension
@app.route('/image/filter', methods=['GET'])
def get_images_by_dimension():
  queries = get_filter_queries(request.args)
  page = request.args.get('page', 1, type=int)
  images = Image.query.filter(*queries).paginate(page=page)
  result = images_schema.dump(images.items)
  return jsonify(images=result, pages=images.pages)

# Create an Image --> prob not needed but wanted to display functionality
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

# Update an Image --> prob not needed but wanted to display functionality
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

# Delete Image --> prob not needed but wanted to display functionality
@app.route('/image/<id>', methods=['DELETE'])
def delete_image(id):
  image = Image.query.get_or_404(id)
  db.session.delete(image)
  db.session.commit()

  return image_schema.jsonify(image)

# get width and height dimension options for filtering
@app.route('/dimensions', methods=['GET'])
def get_dimension_options():
  widths = [x.width for x in db.session.query(Image.width).distinct().order_by(Image.width.asc())]
  heights = [x.height for x in db.session.query(Image.height).distinct().order_by(Image.height.asc())]

  return jsonify(widths=widths, heights=heights)

def get_filter_queries(args):
  queries = []

  if args['width'] == "*":
    queries.append(Image.height == args['height'])
  elif args['height'] == "*":
    queries.append(Image.width == args['width'])
  else:
    queries.extend(Image.width == args['width'], Image.height == args['height'])

  return queries