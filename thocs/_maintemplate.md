Debugging Media Wiki
====================================================================
> Here I document the quick process to get running the wikimedia project on your local quickly.

Installing
====================================================================

Other
====================================================================
To build and image from a Container file description (_Dockerfile_):
1. Clone this repository `https://github.com/31z4/zookeeper-docker`
2. Go to `3.9.1` or your desired version.
3. Then throw `sudo podman build -t zookeeper:3.9.1 .` in the console.
4. Voila! your image was build.

other
---------------------------------
This [documentation][1] 


Other
====================================================================

Tracking log
====================================================================
### 240816
This is the first time trying to work with php technology

References
====================================================================
[1]: https://www.gnu.org/software/bash/manual/bash.html#Positional-Parameters
[2]: https://docs.docker.com/engine/reference/builder/#entrypoint
[3]: https://zookeeper.apache.org/doc/r3.9.1/javaExample.html
