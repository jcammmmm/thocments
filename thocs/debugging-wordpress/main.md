Debugging Media Wiki
====================================================================
> In this guide you will find how to install wordpress. In general is the same process that is it followed for Mediawiki. In my opinion is more easy to follow that setup. Basically the main diference is that here you download wordpress instead of mediawiki.


Installing Wordpress
==================================================================== 
Follow the same steps that you followed for wikimedia.
1. Install webserver `apache2`.
2. Install PHP.
3. Install database.
4. Setup database:
   
   CREATE DATABASE wordpress;
   CREATE USER 'worduser'@'localhost' IDENTIFIED BY 'database_password';
   GRANT ALL PRIVILEGES ON wordpress.* TO 'worduser'@'localhost' WITH GRANT OPTION;

5. Download and extract wordpress.
6. Go to localhost.
7. Follow the installation wizard, and provide the details of your database and user within it.
8. Done.


other
---------------------------------
This [documentation][1] 


Tracking log
====================================================================
### 240823
Installed yesterday.

References
====================================================================
[1]: http://urlsample.net
