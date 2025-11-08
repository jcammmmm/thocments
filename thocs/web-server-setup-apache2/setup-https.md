Intro
===============================================================================
> In this guide you will configure you Apache2 web server to serve pages with HTTPs. For those who likes to understand, please follow _Configuring and invalid self-signed certificate_ if you want a quick 100% working setup please refer to _The easiest way_.

The Easiest Way
===============================================================================
Just use [Let's Encrypt](https://letsencrypt.org/getting-started/) [Cert Bot](https://certbot.eff.org/instructions)


Configuring and invalid self-signed certificate
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
3. Add the `allowOverride ALL` clause to your folder on `apache2.conf`. From a clean installation, this:
    ```
    <Directory /var/www/>
            Options Indexes FollowSymLinks
            AllowOverride None
            Require all granted
    </Directory>
    ```
    changes to:
    ```
    <Directory /var/www/>
            Options Indexes FollowSymLinks
            AllowOverride All
            Require all granted
    </Directory>
    ```
4. Generate a certificate and key tuple with `OpenSSL`.
    ```sh
    openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out apache.crt -keyout apache.key
    ```
   The generator will request to you some information. The unique constraint here is that `FQDN` (Fully Qualified Domain Name) provided in this generator must be the same value under `ServerName` attribute in `/etc/apache2/sites-avilable/yoursite.conf` file.
   After following the CLI wizard you will get two files: `apache.crt` and `apache.key`.
5. Create this folder:
   ```
   sudo mkdir /etc/apache2/certs
   ```
   Then move the certificate and the private key to that folder
   ```
   sudo mv apache.crt /etc/apache2/certs/apache.key
   sudo mv apache.crt /etc/apache2/certs/apache.crt
   ```
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
    
Remove this, is auto configured by the module
    If you want that your webserver returns a page on _443_ port only add the following line to the `ports.config` file: `Listen 443`.



