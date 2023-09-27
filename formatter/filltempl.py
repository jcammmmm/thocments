import os
import datetime as time
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from digest import compute_digest

"""
Returns
-------
str
  HTML written document url location
"""
def fill_and_write_content(p, html_content):
  env = Environment(
    loader=FileSystemLoader('../assets'),
    autoescape=False,
    trim_blocks=True
  )

  # fill template with your post contents 
  post = env.get_template('layout.html').render(content=html_content)

  neat_post_loc = get_write_path(p)
  open(neat_post_loc, 'w+', encoding='UTF-8').write(post)

  open(neat_post_loc, 'a').write('Generated with NeatPosts by TeraDigit a division of LogicFoundries </br>')
  open(neat_post_loc, 'a').write('Last updated: ' + str(time.datetime.now()))
  print(str(neat_post_loc) + ' written.')

  # compute hashes to keep everything in order
  hash_md = compute_digest(p)
  hash_html = compute_digest(neat_post_loc)
  return hash_md, hash_html

def get_write_path(p):
  return p.with_name(p.stem + '.html')