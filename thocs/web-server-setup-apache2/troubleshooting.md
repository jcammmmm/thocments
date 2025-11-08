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
