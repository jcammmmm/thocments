import os
import datetime as time
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

"""
Returns
-------
str
  HTML written document url location
"""
def fill_content(foldername, filename, html_content):
  env = Environment(
    loader=FileSystemLoader('../assets'),
    autoescape=False,
    trim_blocks=True
  )

  # fill template with your post contents 
  post = env.get_template('layout.html').render(content=html_content)

  neat_post_loc = Path('../thocs/' + foldername + '/' + filename + '.html')
  open(neat_post_loc, 'w+', encoding='UTF-8').write(post)

  open(neat_post_loc, 'a').write('Generated with NeatPosts by TeraDigit a division of LogicFoundries </br>')
  open(neat_post_loc, 'a').write('Last updated: ' + str(time.datetime.now()))
  print(str(neat_post_loc) + ' written.')
  return os.path.join(os.getcwd(), neat_post_loc)