import markdown as md

'''
Translates a Markdown file to an HTML document.
'''
def to_html(md_filename):
  try:
    with open(md_filename, 'r', encoding='UTF-8') as input_file:
      md_doc = input_file.read()
  except FileNotFoundError:
    raise Exception('The file ' + md_filename + ' does not exist.')

  '''
  extensions var
    attr_list  : for inline attribute definitions
    toc        : table of contents
    tables     : generates html tables
    fenced_code: display codeblocks (https://python-markdown.github.io/extensions/fenced_code_blocks/)
  '''
  html_doc = md.markdown(
    md_doc, 
    extensions=['attr_list', 'toc', 'tables', 'fenced_code'], 
    output_format='html5', 
    tab_length=2)
  return html_doc
  