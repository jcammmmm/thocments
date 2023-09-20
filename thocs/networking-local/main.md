Intro
=====================================================================
When you self host a server and you did not configure an static IP address, after some time the address can change and lost the access to the server. In addition, it could be difficult to find the IP through your ISP modem configuration since those configuration could not be available. In this brief post I provide two ways on how you can retrieve the IP address from your server.

How to find every device on your LAN
=====================================================================
1. Install `nmap`. 
  ```sh
  sudo apt install nmap
  ```
2. 
  ```sh
  sudo nmap -sP 192.168.0.1/24
  ```



