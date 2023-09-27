import json
from datetime import date, datetime

"""
Parent class to make the serialization implementation more clearly.
"""
class Info:
  pass

"""
info = {
      'title': '',
      'descr': '',
      'showtoc': False,
      'pubdate': 
      'files': {
          # each post must have a main.md file
          'main': { 
            'lastupdate': str(datetime.today().isoformat()),
            'hashes': {
                'html': '84ec0588475f211f689bb31ebd0025b9e84c69999672250c024767b2fd366de7',
                'md': '84ec0588475f211f689bb31ebd0025b9e84c69999672250c024767b2fd366de7'
            }
          }
      }
    }
"""
class PostInfo(Info):
  def __init__(self, p):
    self.info_path = p.with_name('info.json')
    self.title = ''
    self.descr = ''
    self.showtoc = False
    self.pubdate = str(date.today()),
    self.files = {
        'main': File(str(datetime.today().isoformat()))
    }

    if self.info_path.exists():
      with open(self.info_path, 'rb') as f:
        post_info = json.loads(f.read())
        self.title = post_info['title']
        self.descr = post_info['descr']
        self.showtoc = post_info['showtoc']
        self.pubdate = post_info['pubdate']
        self.files = PostInfo.parse_files_dict(post_info['files'])

  """
  returns a dictionary containing the file digest
  """
  @staticmethod
  def parse_files_dict(post_info_files):
    files = {}
    for k, v in post_info_files.items():
      lastupdate = v['lastupdate']
      hash_html = v['hashes']['html']
      hash_md = v['hashes']['md']
      if k not in files:
        files[k] = File(lastupdate, hash_html, hash_md)
    return files

  """
  @param filestem: filename without extension
  @param hashes: an Hashes object
  @return: nothing
  """
  def update(self, filestem, hashes):
    self.files[filestem].hashes = hashes
    self.files[filestem].lastupdate = str(datetime.today().isoformat())

  """
  converts current object class to a python dictionary, in order to 
  serialize easily to json.
  """
  def as_dict(self):
    def to_dict(obj):
      ans = {}
      if isinstance(obj, Info):
        for k, v in obj.__dict__.items():
          ans[k] = to_dict(v)
        return ans
      elif isinstance(obj, dict):
        for k, v in obj.items():
          ans[k] = to_dict(v)
        return ans
      else:
        return obj
    out = to_dict(self)
    del out['info_path']
    return out

  """
  Writes current object state as a json file.
  """
  def write(self):
    print(json.dumps(self.as_dict(), sort_keys=False, indent=4))
    
class File(Info):
  def __init__(self, date, html_hash='¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?', md_hash='¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?'):
    self.lastupdate = date
    self.hashes = Hashes(html_hash, md_hash)

class Hashes(Info):
  def __init__(self, html_hash='¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?', md_hash='¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?'):
    self.html = html_hash
    self.md = md_hash