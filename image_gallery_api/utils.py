from image_gallery_api.models import Image

def get_filter_queries(args):
  queries = []

  if args['width'] == "*":
    queries.append(Image.height == args['height'])
  elif args['height'] == "*":
    queries.append(Image.width == args['width'])
  else:
    queries.extend([Image.width == args['width'], Image.height == args['height']])

  return queries