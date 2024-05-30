Install
===============================================================================
1. Update your package index:    
   ```sudo apt update``` 
2. Install the http server software:    
   ```sudo apt install apache2``` 
3. Verify that the server (process) is up and running:   
   ```sudo systemctl status apache``` 

HTTPs ports
===============================================================================
If your want that your webserver returns a page on _443_ port only add the following line to the `ports.config` file: `Listen 443`.

Basic configuration
===============================================================================
[Options](https://httpd.apache.org/docs/2.4/mod/core.html#options)
[AllowOverride](https://httpd.apache.org/docs/2.4/mod/core.html#allowoverride)
[Order](https://httpd.apache.org/docs/2.4/mod/mod_access_compat.html#order)
[Allow](https://httpd.apache.org/docs/2.4/mod/mod_access_compat.html#allow)

Basically with these configuration you can controll what is the behavior of the server when a page or folder is requested.
* Options:
	- Indexes: If the folder contents can be listed
	- FollowSymlinks: self explanatory
	- Includes
	- ExexCGI
* AllowOverride: If the .htaccess folder can override the previous configs.
* Order: Manages how _Allow_ is applied
* Allow: A soft kind of Firewall.

This was a configuration that worked fine on DigitalOcean _droplet_.

```xml
<Directory />
        Options FollowSymLinks
        AllowOverride None
        Require all denied
</Directory>

<Directory /usr/share>
        AllowOverride None
        Require all granted
</Directory>

<Directory /var/www/>
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
</Directory>

#<Directory /srv/>
#       Options Indexes FollowSymLinks
#       AllowOverride None
#       Require all granted
#</Directory>
```

Configure HTTPS
===============================================================================
1. Enable de required `ssl` and `rewrite` modules. As a side note, you can disable those modules with `a2dismod`
    ```sh
    sudo a2enmod ssl
    sudo a2enmod rewrite
    ```
2. If you tried previously to configure your server by adding a new listening port on `ports.conf` file, try to undo those changes and restart the module again.
3. Add the `allowOverride ALL` clause to your folder on `apache2.conf`.
4. Generate a certificate and key tuple with `OpenSSL`.
    ```sh
    openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out apache.crt -keyout apache.key
    ```
   The generator will request to you some information. The unique constraint here is that `FQDN` (Fully Qualified Domain Name) provided in this generator must be the same value under `ServerName` attribute in `apache2.conf` file.
5. Add another virtual host to your current site in `/etc/apache/sites-enabled/000-default.conf`:
    ```xml
    <VirtualHost *:443>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        SSLEngine on
        SSLCertificateFile /etc/apache2/certs/apache.crt
        SSLCertificateKeyFile /etc/apache2/certs/apache.key
    </VirtualHost>
    ```
    
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
1. Enable the `cgid` module, then restart the server:
  ```sh
  sudo a2enmod cgi
  systemctl restart apache2
  ```
2. You have to modify the `ScriptAlias` directive. Go to `/etc/apache2/` and throw this command `grep -rn . -e ScriptAlias`. From there you will see that this directive shoudl modified in `conf-available/serve-cgi-bin.conf`.
3. You should replace the entire `<IfDefine>` node with this:
```conf
<IfDefine ENABLE_USR_LIB_CGI_BIN>
  ScriptAlias /cgi-bin/ /var/www/html/cgi-bin/
  <Directory "/var/www/html/cgi-bin/">
          AllowOverride None
          Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
          Require all granted
  </Directory>
</IfDefine>
```

Troubleshoot
===============================================================================
OS Logs
---------------------------------------
* Here you can collect hints to fix the problem; check the server process status. The `--no-pager` flag will output everything in the terminal (no tail, less or top style output):
  ```sh
  sudo systemctl status apache2 -l --no-pager
  ```
* Get the OS process manager logs. Note that these are different from `error.log` and `access.log` from the server itself.
  ```sh
  sudo journalctl -u apache2.service --since today --no-pager
  ```
* Test your config file
  ```sh
  sudo apachectl configtest
  ```

Apache2 Logs
---------------------------------------
- `/var/log/apache2/error.log`
- `/var/log/apache2/acces.log`
  

Access errors
---------------------------------------
Your file when access from the client reports an _403 Forbiden_ error. This can be caused because your file has the wrong access flags. This can solve the error:
1. ```sudo chmod 644 filename.html ```
This will change from (no access):
```sh
-rw------- 1 jcammmmm jcammmmm 15406 May 13 19:33 favicon.ico
-rw-r--r-- 1 root     root     10749 May 14 12:52 index2.html
-rw------- 1 root     root       202 May 13 19:07 filename.html
```

to this (access):
```sh
-rw------- 1 jcammmmm jcammmmm 15406 May 13 19:33 favicon.ico
-rw-r--r-- 1 root     root     10749 May 14 12:52 index2.html
-rw-r--r-- 1 jcammmmm jcammmmm   202 May 13 19:07 filename.html
```

where
-rwxrwxrwx
0abcABCxyz

* abc are the permissions for file owner.
* ABC are the permissions for group owner
* xyx are the permissions for the other users.



