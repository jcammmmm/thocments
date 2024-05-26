Change GRUB boot order by hand
=================================================
> When you try to change the boot order the options provided in the _Sources_ section appear first. An approach that does not depend on additional software is easy to get after reading the `/etc/grub.d/README` file. In this short guide I will show how to change your boot order after following these instructions.

Files that will be edited
=================================================
* `/etc/grub.d`
* `/etc/default/grub`


Additional notes
=================================================
- If you have serveral distros, you should note that each distro (if you install everything in the same partition) will have its own `etc` folder, then you must the choose the correct one to make the changes.










Sources
=================================================
* An StackExchange [answer](https://superuser.com/questions/299058/change-the-order-of-all-boot-entries-in-grub2-not-just-the-first)
