from image_gallery_api.models import Image

def get_filter_queries(args):
  queries = []

  if args.get('width') == "*":
    queries.append(Image.height == args.get('height'))
  elif args.get('height') == "*":
    queries.append(Image.width == args.get('width'))
  else:
    queries.extend([Image.width == args.get('width'), Image.height == args.get('height')])

  return queries