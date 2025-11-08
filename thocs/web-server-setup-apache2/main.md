INSTALL
===============================================================================
1. Update your package index:    
   ```sudo apt update``` 
2. Install the http server software:    
   ```sudo apt install apache2``` 
3. Verify that the server (process) is up and running:   
   ```sudo systemctl status apache``` 


## If host is Virtualbox
1. Go to settings or Devices toolbar
2. Select ```Network``` > ```Network Settings```
3. On ```Atached to ```, select ```Bridged Adapter```
4. Click on OK
5. Wait for the VM to take the changes.
6. Launch a terminal, then ```hostname -I```, one of the output addresses
   shall be your host ip.

## Add user to sudoers
1. Edit this file  ```/etc/sudoers```
2. Add a line referencing your user similar to the existing one for ```root```

## Install firewall manager
1. ```sudo apt update```
2. ```sudo apt install ufw```
3. ```sudo ufw app list```. List all the preset firewall configs.
5. ```sudo ufw allow WWW```
3. ```sudo ufw enable```
4. ```sudo ufw status```


## Install HTTP Server
1. ```$ su - ```. Please note the ```-``` this will retain the ```\usr\bin```
   path for the rooted user.
2. ```# apt update```
3. ```# apt install apache2```
4. ```# systemctl status apache2```
5. Open a web browser an go to ```localhost```
6. 


TROUBLESHOOTING
===============================================================================
# Linux Web server setup
If you are in windows, install VirtualBox and install Debian 11
