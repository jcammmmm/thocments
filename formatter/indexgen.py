import xml.etree.ElementTree as ET
from datetime import date
from yaml import load

def generate_index():
  posts_idx = open('index.yaml', 'r').read()
  try:
      from yaml import CLoader as Loader
  except ImportError:
      from yaml import Loader

  idx_data = load(posts_idx, Loader=Loader)
  html_idx = ET.Element('div')
  title = ET.SubElement(html_idx, 'h2')
  title.text = 'Recent Posts'
  for post in idx_data:
    entry = ET.SubElement(html_idx, 'div')
    entry.set('class', 'post-listing-entry')
    # title
    title = ET.SubElement(entry, 'h3')
    title.text = post['title']
    title.set('id', post['nameid'])
    title.set('class', 'post-listing-title')
    # date https://docs.python.org/3/library/datetime.html#examples-of-usage-datetime
    postingDate = str(post['postingDate'])
    year = int(postingDate[0:4])
    month = int(postingDate[4:6])
    day = int(postingDate[6:])
    postingDate = date(year, month, day)
    publishDate = ET.SubElement(entry, 'i')
    publishDate.text = postingDate.strftime('%B %Y, %A %d.')
    ET.SubElement(entry, 'br')
    # thumbnail
    img = ET.SubElement(entry, 'img')
    img.set('src', post['thumbnail'])
    # description
    descr = ET.SubElement(entry, 'p')
    descr.text = post['description']
    descr.set('class', 'post-listing-descr')
    # repourl
    repourl = ET.SubElement(entry, 'a')
    repourl.text = 'Read more... '
    repourl.set('href', post['previewURL'])

  ET.indent(html_idx)
  return ET.tostring(html_idx, encoding='unicode')




