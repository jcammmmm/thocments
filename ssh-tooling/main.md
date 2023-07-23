# How to clone a repo the hard (easy) way
## Windows
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

## Linux