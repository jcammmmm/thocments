Configure Python CGI
===============================================================================
This section will guide you on how to configure your web server to serve dynamic content throught an script that it is excuted after the request arrives to the server. The results produced by this script to the _standard output_ will be treated as the HTTP response. For that reason this script should provide as a minimum a content type declaration. This steps were obtained after reading [this.](https://httpd.apache.org/docs/2.4/howto/cgi.html)

Create a script then run
---------------------------------------
0. Locate your script interpreter. For this short guide I will use _Python_ programming language. In my case it is located at `usr/bin/python3`:
  ```sh
  which python3
  ```
1. Create a folder called `cgi-bin` under `/var/html/www/`. Inside of this new folder put the following perl script file. Note the _shebang_ definition:
  ```py
  #!/usr/bin/python3
  print("Content-type: text/html\n")
  print("<h1>Hello, World.</h1>")
  ```
2. Set execution rights for every user on the system since the server in its behalf will execute the script, not you:
  ```sh
  sudo chmod a+x first.py
  ```
3. Then from an HTTP client request this newly created script (if the server is at port 80) `http://localhost/cgi-bin/first.pl`. As you may be expected the script is downloaded. So we have to configure the server in order to execute the script in the server.

Configuring the Server
---------------------------------------
1. Enable the `cgi` module, then restart the server:
  ```sh
  sudo a2enmod cgi
  systemctl restart apache2
  ```
2. You have to modify the `ScriptAlias` directive. Go to `/etc/apache2/` and throw this command `grep -rn . -e ScriptAlias`. From there you will see that this directive shoudl modified in `conf-available/serve-cgi-bin.conf`.
3. You should replace the entire `<IfDefine>` node with this:
```html
<IfDefine ENABLE_USR_LIB_CGI_BIN>
  ScriptAlias /cgi-bin/ /var/www/html/cgi-bin/
  <Directory "/var/www/html/cgi-bin/">
          AllowOverride None
          Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
          Require all granted
  </Directory>
</IfDefine>
``` 
