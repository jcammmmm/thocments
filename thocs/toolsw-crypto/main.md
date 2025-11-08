Tools for cryptography
====================================================================
> Here I left how to encrypt / decrypt a file thorugh CLI in a symple way. Please note that this will not provide secure communications i.e. eavesdropping and interceptation, just information encryption.

Options
====================================================================
There are two options, password managers and CLI encryption tools. 

CLI 
---------------------------------
The most common options in linux are `OpenSSL` and `GPG`. For simplicity we will use simetric encryption, that will require only a password. In addtion there are serveral ciphers, but _AES_ is recommended
  
  - `DES`: Not recommended, break can be possible.
  - `3DES`: To apply 3 times DES, but also has its flaws. 
  - `CAMELLIA`: Unpopular in my opinion
  - `AES`: POpular

AES
---------------------------------
As a block cipher, it has serveral modes of operation. Because we are interested both in `OpenSSL` and `GPG`, the only mode common between the two is `CFB`. It seems that `GPG` only supports that mode.

### OpenSSL
* Encryption 

  openssl aes-256-cbc -e -in nbookmark.txt -out nbookmark.txt.ssl

* Decryption
  
  openssl aes-256-cbc -d -in nbookmark.txt.ssl

### GPG
* Encryption

  gpg -c nbookmark.txt
  
* Decryption

  gpg -d nbookmark.txt.gpg

Because with gpg is unclear which algorithm is being used and which mode (and also from the docs, the output says that uses AES256 but the docs says AES128) it is prefferred the openssl version.

#### Risks
- You password file could be corrupted by an attacker. The same happens with a password manager database.
- It is easy to corrupt your encrypted file, or forget something and lost everything by doing this by hand.

Password Managers
---------------------------------
As today the best open source password manager in linux is KeePassXC. It is based on the original Keepass software only available in Windows. 

Keepass is not recommended becasuse the database file is not an open standard and could be subject to changes at any time, meaning that you can corrupt you password database. 
  

Tracking log
====================================================================
### 241002
Init

References
====================================================================
[1]: https://example.org
