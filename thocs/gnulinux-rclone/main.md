Rclone Usage
====================================================================
> How to use Rclone. This tool synchronizes your folders .i.e it will left them equal. Supports several providers. In the following sections a quick setup is shared.


Usage
====================================================================
The basic command has the following structure. Note the `--dry-run` flag, since you can lost files in this syncing process, with this flag only the action that will be taken by rclone will be listed:
  
  rclone sync --dry-run SRC DST
  
`DST` is the folder that you want to be equal to `SRC`. That means that rclone will perform all the actions on `DST`. Please have special care here! If you want the reverse behavior, i.e. to update `SRC` according to `DST` this is the command:

  rclone sync --dry-run DST SRC
  
Again, please take care here. We recommend to try this before on test folders instead of you important ones. 
Together with this readme we provide an script to gently automate this task.

Before using rclone you need to configure it first. See next section.

Recommendations
---------------------------------------
We recommend to set a couple of aliases to perform this task with easeness in the future, for example:

~~~bash
alias syncnotes='rclone sync -v --dry-run /home/jcammmmm/Documents/notes NOTES:/root/NOTES'
alias syncnotesok='rclone sync -v /home/jcammmmm/Documents/notes NOTES:/root/NOTES'
~~~


Configuration
====================================================================
1. Create a new configuration. This means you will setup the tool to conect to you r storage, filesystem or cloud provider.

  rclone config
  
2. Follow the wizard. The wizard will depend on where you have your folders to sync. The following sections have more details. To start the wizard type `n` (New Remote)

   rclone> n

SFTP
---------------------------------------
At this time I suppose that an already SSH connection exits with key authentication.

1. Select SFTP storage, add the host, the username, and the server port

    rclone> 36
    rclone> 127.0.9.1
    rclone> jcammmmm
    rclone> 22
    
2. Then the prompts for password/key authentication details will follow. Left empty everything exept `Option key_file`, there you will put the path of the private key:
   
    rclone> /home/usern/.ssh/privkey
    
3. Done.
  

Installing
====================================================================
Symply `sudo apt install rclone`


Other
====================================================================
This [documentation][1] 


Tracking log
====================================================================
### 240825
This is the first time trying to work with this rclone

References
====================================================================
[1]: https://www.gnu.org/software/bash/manual/bash.html#Positional-Parameters
[2]: https://docs.docker.com/engine/reference/builder/#entrypoint
[3]: https://zookeeper.apache.org/doc/r3.9.1/javaExample.html
