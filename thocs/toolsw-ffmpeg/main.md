Install
---------------------------------------
Download build: https://www.gyan.dev/ffmpeg/builds/
Extract. 
ffmpeg is located in 'bin' folder.
Add to PATH
Done!

Change encoding
--------------------------------------- 
$ ffmpeg -i "Homophonic Cipher - Brute Force count.mp4" -vf "transpose=1" "Homophonic Cipher - Brute Force count.mov"

Cut video in parts
--------------------------------------- 
There two ways this. This command will crop you `inputfile.mts` video file from `00:00:44` to `00:03:17` and will produce a new file named `outputfile.mp4`. Please note that `ffmpeg` will detect the file formats from the file name you provide after `-ss` and `-to` arguments:
```sh
$ ffmpeg -ss 00:00:44 -to 00:03:17 -i inputfile.mts -c copy outputfile.mp4
```
and this:
```sh
$ ffmpeg -i ger.mp4 -ss 0:0:22 -t 0:0:42 -vcodec copy -acodec copy outputvideo1a.mp4
$ ffmpeg -i ger.mp4 -ss 0:0:42 -t 0:1:00 -vcodec copy -acodec copy outputvideo1b.mp4
$ ffmpeg -i ger.mp4 -ss 0:1:00 -t 0:1:18 -vcodec copy -acodec copy outputvideo2a.mp4
$ ffmpeg -i ger.mp4 -ss 0:1:18 -t 0:1:36 -vcodec copy -acodec copy outputvideo2b.mp4
$ ffmpeg -i ger.mp4 -ss 0:1:36 -t 0:1:50 -vcodec copy -acodec copy outputvideo3a.mp4
$ ffmpeg -i ger.mp4 -ss 0:1:50 -t 0:2:03 -vcodec copy -acodec copy outputvideo3b.mp4
```
