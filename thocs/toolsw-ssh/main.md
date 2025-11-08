# Using SSH
> Common tasks with SSH 

## Configure SSH server for ssh access
1. Generate Keys in the client computer.
2. Access the server by any mean
3. Copy the public key to `authorized-keys` file in your server's user folder:
   
   ~~~sh
   vim ~/.ssh/authorized-keys
   Ctrl + V
   :wq
   ~~~

   Please note that if you plan to log in with user `myuser`, you should paste the
   public key in the server under this route `/home/myuser/.ssh/authorized-keys` 

4. Test your acess:
   ~~~
   ssh -i yourprivatekeyfile myuser@149.233.39.12
   ~~~

## How to clone a repo the hard (easy) way
### Windows
1. Check if you have the following OpenSSH tools:
    ```
    ssh-keygen
    ssh-agent
    ssh-add
    ```
2. Open a CMD and generate a pair of keys with ssh-keygen.
3. On the same terminal start the `ssh-agent` in background:
    ```powershell
    $ eval $(ssh-agent)
    : Agent pid 97280
    ```
    
4. Then add your private key to the ssh client:
    ```
    ssh-add ~/.ssh/rsa_id.ppk
    ```
5. Clone your git repo providing an SSH url:
   ```
   git clone ssh:\\url.toyour.repo
   ```
6. If your want to push your changes, verify that the remote is point with an ssh URL e.g. `git@github.com:<username>/<repository>`

## Linux
