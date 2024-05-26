Usage  
===========================================================
Edit the YAML files in each language. Then execute the provided python script as follows:

Linux/Debian
---------------------------------------
1. Create your environment if you did not create already one:
	```$ python3 -m venv env```
2. Activate your environment:    
	```$ source env/bin/activate```
3. Install script dependencies:
	```pip install -r requirements.txt```
4. Run the script:
	```python3 multiform-gen.py```
5. Look for output results in ```../cv``` folder.
6. Deactivate your environment:    
	```$ deactivate```





TODO
===========================================================
Reimplement the markdown to html converter in JS
  - https://github.com/showdownjs/showdown#who-uses-showdown-or-a-fork   
  - https://github.com/markdown-it/markdown-it#authors   
  - https://github.com/markedjs/marked   

Since Python parser I feel is not as popular as the JS alternatives:   
  * You need to put your bulleted text after a new line.
  * You cannot create bulleted lists if they are indented. For example   
    this bullet list will not will render as html.
  * Most of the time you need to end each paragraph with three spaces.