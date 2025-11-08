Debugging Media Wiki
====================================================================
> Here I document the quick process to get running the wikimedia project on your local quickly.

Installing
====================================================================
It seems that debian has a good integrations with the _Apache_ web server and _PHP_ setup. A very long time ago I tried to setup PHP an took a lot of time.
1. Install the dependencies such as the installation manual states.
  
   sudo apt-get install apache2 mariadb-server php php-intl php-mbstring php-xml php-apcu php-curl php-mysql

2. When you run this in Debian 12, automatically will setup the apache2 server to server pages from `/var/www/html`, will configure the PHP to work together with the webserver and will bring up the _MariaDB_ database empty. Easy.

3. Clone the _mediawiki_ project directly into the `/var/www/html` folder.

   git clone https://github.com/wikimedia/mediawiki

4. PHP uses a software called _Composer_ manage PHP dependencies. Its just an standalone executable. Just download it and put inside your mediawiki local py.

   wget -cO - https://getcomposer.org/composer-2.phar > composer.phar

5. Install the dependencies:

   php composer.phar install

6. Setup the database as the per documetnation docs:
 
    ```
    CREATE DATABASE my_wiki;
    CREATE USER 'wikiuser'@'localhost' IDENTIFIED BY 'database_password';
    GRANT ALL PRIVILEGES ON my_wiki.* TO 'wikiuser'@'localhost' WITH GRANT OPTION;
    ```
7. go to `http://localhost/mediawiki` and follow the screens.

8. The `LocalSettings.php` file is downloaded. Then move it to your repository at `/var/www/html/mediawiki`, and enable it following the skin page instructions to the `LocalSettings.php` file.

9. Install a skin. Just follow the docs [here](https://www.mediawiki.org/wiki/Skin:Vector/2022). This is the summary of the commands:

   curl -O http://yourskin
   cd /var/www/html/w/skins
   cp ~/Downloads .
   tar -xvf yourskin
   echo >> wfLoadSkin( 'Vector' );

10. Done!
   


Login Details
---------------------------------
Database:
user: wikiuser
pass: datatbase-password
Wiki:
user: jcammmmm
pass: firstfourontherow+mayusbelow



other
---------------------------------
This [documentation][1] 


Other
====================================================================

Tracking log
====================================================================
### 240816
This is the first time trying to work with php technology

References
====================================================================
[1]: http://urlsample.net
