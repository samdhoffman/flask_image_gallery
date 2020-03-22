from image_gallery_api.models import Image

def get_filter_queries(args):
  queries = [] 

  if args.get('width') == "*":
    queries.append(Image.width)
  else:
    queries.append(Image.width == args.get('width'))
  
  if args.get('height') == "*":
    queries.append(Image.height)
  else:
    queries.append(Image.height == args.get('height'))

  return queries