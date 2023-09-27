import hashlib

def compute_digest(path):
  m = hashlib.sha256()
  with open(path, 'rb') as f:
    while True:
      data = f.read(1000)
      if not data: break
      m.update(data)
  return m.hexdigest()
