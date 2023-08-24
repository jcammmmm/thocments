import os
import datetime as time
from jinja2 import Environment, FileSystemLoader

"""
Returns
-------
str
  HTML written document url location
"""
def fill_content(foldername, fonts_loc, html_content):
  env = Environment(
    loader=FileSystemLoader('../assets'),
    autoescape=False,
    trim_blocks=True
  )

  # hardcode font urls in css file
  css = env.get_template('layout.css').render(urlprefix=fonts_loc)
  # put your post contents in template
  post = env.get_template('layout.html').render(content=html_content, styles=css)

  foldername = '../thocs/' + foldername + '/main.html'
  open(foldername, 'w+', encoding='UTF-8').write(post)

  open(foldername, 'a').write('Generated with NeatPosts by TeraDigit a division of LogicFoundries </br>')
  open(foldername, 'a').write('Last updated: ' + str(time.datetime.now()))
  print(foldername + ' written.')
  return os.path.join(os.getcwd(), foldername)