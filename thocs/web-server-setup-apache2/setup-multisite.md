Setup multisite
====================================================================
> How to configure multiple websites [1].

Installing
====================================================================
1. Copy the contents of your sites. Note: take care of your assets!

TODO el nombre de la carpeta es el nombre del dominio
```sh
sudo mkdir -p /var/www/landings/francarga/
sudo mkdir -p /var/www/landings/ismaelflorez/
...
sudo mkdir -p /var/www/landings/assets/
```

2. Take ownership

```sh
sudo chown -R $USER:$USER /var/www/landings
```

4. Create separate websites config

```sh
sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/francarga.conf
sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/ismaelflorez.conf
```

5. The default comments on the original `000-default.conf` files has insightful info the `ServeName` config added here.
Moreover bacause the domain that are acquired on internet always have _.com_, _.net_ etc, always in the HTTP request the host attribute you will find a host name with such kind of suffix e.g. _example.com_, _ismaelflorez.com_ etc. Following the comments addressed at the beginning of this paragraph you will note that in order to match the `<yoursite>.conf` file, you need to put under `ServerName` the string that will arrive in the request.

Edit the `francarga.conf` like this:
```xml
<VirtualHost *:80>
        ServerAdmin webmaster@francarga.com
        ServerName francarga
        ServerAlias www.francarga
        DocumentRoot /var/www/landings/francarga
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
Edit the `ismaelflorez.conf` like this:

```xml
<VirtualHost *:80>
        ServerAdmin webmaster@ismaelflorez
        ServerName ismaelflorez
        ServerAlias www.ismaelflorez
        DocumentRoot /var/www/landings/ismaelflorez
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

6. Activate the sites with `a2ensite`, check syntax and restart the server. The `a2ensite` (apache2 enable site) command add a symbolic link to the _enabled sites_ folder. 

```sh
sudo a2ensite ismaelflorez.conf 
sudo a2ensite francarga.conf 
sudo apache2ctl configtest
sudo systemctl restart apache2
sudo systemctl status apache2
```



Tracking log
====================================================================
### 2401002
This is the first time trying to work with php technology

References
====================================================================
[1]: https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-20-04
