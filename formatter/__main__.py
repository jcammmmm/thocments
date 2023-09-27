import argparse

# from .indexgen import generate_index
from converter import to_html
from filltempl import fill_and_write_content
from filltempl import get_write_path
from rendermath import render_mathematics
from pathlib import Path
from os import remove
from postinfo import PostInfo
from postinfo import Hashes

def main():
  parser = argparse.ArgumentParser(
    description="""
      Generate a neat web document from a Markdown file. By that, you have
      both of the two worlds: a simple text file, and also a neat displayed html page
      without to get messed with tags.
    """)
  parser.add_argument('foldername', help='markdown filename without extension', nargs='*')
  # parser.add_argument('-r', '--client-rendering', action='store_true', 
    # help="""
    #   Indicates if neatpost LaTeX mathematics shall be renderend on the web browser.
    #   If not provided as argument, the neatposts mathematics in LaTeX are converted
    #   to CHTML on the server, speeding up the page loading for the final user.
    # """)
  parser.add_argument('-i', action='store_true', 
    help="""
      Flag that indicates that a toc-index web page will be generated provided
      the index.yaml post resources definition file. This package will look
      automatically for this file in the folder where the package was called.
    """)
  # parser.add_argument('-p', action='store_true', 
  #   help="""
  #     Flag that indicates that fonts location are in a remote server. If not HTTP
  #     remote location is defined with argument -l, this remote location defaults
  #     to: https://jcamilo.co/fonts/cmuserif/
  #   """)
  # parser.add_argument('-l', metavar='fontloc',
  #   help="""
  #     an HTTP url that points to the computer modern fonts location.
  #   """)
  args = parser.parse_args()
  if len(args.foldername) == 0:
    print('Please provide a foldername, the following are available:')
    for p in Path('../thocs/').iterdir():
      print('* ' + p.stem)
    return
    
  # Font location: development or production location
  fonts_loc = Path('../../assets/fonts/')
  # Convert Markdown with LaTeX typesets to HTML with LaTeX typesets
  if (args.i):
    html_content = generate_index()
  else:
    # for each post from the command line
    for folder in args.foldername:
      success = True
      post_path = Path('../thocs/' + folder)
      post_info_path = post_path.joinpath('info.json')
      post_info = PostInfo(post_info_path)
      for p in post_path.iterdir():
        if (p.suffix == '.md'):
          # convert markdown content to html, then check for post
          # description
          html_content = to_html(p)
          if (p.stem == 'main'):
            htmlparser = Parser()
            htmlparser.feed(html_content)
            if len(htmlparser.descr) == 0:
              print("WARNING: Please provide a title and a description to your post with '>>'.\nWARNING: Exiting now. No output was produced.")
              success = False
              break
            post_info.title = htmlparser.title
            post_info.descr = htmlparser.descr
          # put the html formated content in our neat templates then
          # compute hashes
          try:
            hash_md, hash_html = fill_and_write_content(p, html_content)
          except Exception as e:
            print(e)
            success = False
            break
          # update the file metadata
          post_info.update(p.stem, Hashes(hash_html, hash_md))

      # if not success remove every generated file
      if success:
        post_info.write()
      else:
        for p in post_path.iterdir():
          if (p.suffix == '.md'):
            try: 
              remove(get_write_path(p))
            except:
              pass
    # Convert HTML with LaTex typesets to pure HTML document with mathematics
    # if (not args.client_rendering):
    #   render_mathematics(html_file_loc);


from html.parser import HTMLParser

class Parser(HTMLParser):
    def __init__(self):
      self.title = ''
      self.descr = ''
      self.titlepos = 0
      self.blockquopos = 0
      self.paragrpos = 0
      self.currtag = ''
      super().__init__()

    def handle_starttag(self, tag, attrs):
        self.currtag = tag
        if tag == 'h1':
          self.titlepos += 1
        if tag == 'blockquote':
          self.blockquopos += 1
        if tag == 'p' and self.blockquopos == 1:
          self.paragrpos += 1

    def handle_data(self, data):
      if self.currtag == 'h1' and self.titlepos == 1:
        self.title = data
        self.titlepos += 1
        return
      if self.currtag == 'p' and self.paragrpos == 1:
        self.descr = data
        self.blockquopos += 1
        return

if __name__ == '__main__':
  main()