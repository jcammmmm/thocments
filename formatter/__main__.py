import argparse

# from .indexgen import generate_index
from converter import to_html
from filltempl import fill_content
from rendermath import render_mathematics
from pathlib import Path

def main():
  parser = argparse.ArgumentParser(
    description="""
      Generate a neat web document from a Markdown file. By that, you have
      both of the two worlds: a simple text file, and also a neat displayed html page
      without to get messed with tags.
    """)
  parser.add_argument('foldername', help='markdown filename without extension')
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
  
  # Font location: development or production location
  fonts_loc = Path('../../assets/fonts/')

  # Convert Markdown with LaTeX typesets to HTML with LaTeX typesets
  if (args.i):
    html_content = generate_index()
  else:
    for p in Path('../thocs/' + args.foldername).iterdir():
      if (p.suffix == '.md'):
        # convert markdown content from 'p' to html
        html_content = to_html(p)
        # put the html formated content in our neat templates
        html_file_loc = fill_content(args.foldername, p.stem, html_content)

        # Convert HTML with LaTex typesets to pure HTML document with mathematics
        # if (not args.client_rendering):
        #   render_mathematics(html_file_loc);
    
if __name__ == '__main__':
  main()