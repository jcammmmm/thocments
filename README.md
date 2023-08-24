# About 
This python module will transform your markdown documents that contains mathematics into html. Its design
has in mind to be minimalistic and aestetically academic.

MD format was chose since one wants to focus on document text content a not in the tags.

It relies in the following awesome software tools:
- [MathJax](http://docs.mathjax.org/en/latest/) LaTeX to MathML processor.
- [Python-Markdown](https://python-markdown.github.io/) Markdown to html processor.
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) Template engine.
- [Computer Modern Fonts](https://www.checkmyworking.com/cm-web-fonts/).
- [Setuptools](https://setuptools.pypa.io/en/latest/#) Build backend.

# How to run #
## Correctly ##

  1. cd neatposts
  2. pip install --editable .
  3. cd your/post/location
  4. python3 -m neatposts <md_filename_no_extension>

## Legacy

  1. python3 -m venv ./env
  2. source env/bin/activate
  3. pip install -r requirements.txt
  4. deactivate

# Packaging
- [Official python guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Build Backend](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)