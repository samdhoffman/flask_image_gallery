# This file will be responsible for running our application

from image_gallery_api import app

# Run server
if __name__ == '__main__':
  app.run(debug=True)