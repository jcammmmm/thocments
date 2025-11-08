Android Development 
====================================================================
> In this document I will put ideas about what means APIs, framework, Compatibility libraries, what becomes obsolete, and how Google manages the Android Project.

Android is Open Source
====================================================================

adb
--------------------------------------
The android debugging bridge source code is apparently hosted [here](https://cs.android.com/android/platform/superproject/+/android15-qpr2-release:packages/modules/adb/).


Android Versions
====================================================================
Because in the world not everyone is running the same version of android, which in turn could mean a different programming API, there are [libraries](https://developer.android.com/topic/libraries/support-library) (aka Android Suppor Library) that can bring the new API features to old API versions.

Overall the use case for this compatibility libraries is to offer backwards [compatibility](https://developer.android.com/topic/libraries/support-library) to support devices from broader variety of API versions.

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
