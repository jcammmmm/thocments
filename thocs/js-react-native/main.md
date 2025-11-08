Working with React Native
====================================================================
> How to get started with React Native in linux without Android Studio bloatware. 

Installing
====================================================================
1. As expected, React Native needs the android emulator and the adb tool for development, so please 
refer to the android guide for that.
  1. [ ] Specific version of android is needed !
2. Install Java Development Kit v17 (I think  I wrote a guide for that).
   - Recommended by them somewhere in the docs.
3. Install Node v22 (I think I wrote a guide for that). 
4. To develop with React Native it is recommended to use Expo. Start a new Expo
project. Add the `--help` flag to watch other options like the interesting `--example`:

    npx create-expo-app@latest --example

5. Install Watchman. I spent a couple of hours trying to build it from source, but I was 
   unable. There was a problem with the _Folly_ dependency that was also built from source 
   and failed. Then I decided to install _Brew_ package manager and install Watchmman from
   there. It worked straigthfully.
   The Build setup includes to run an environment setup script for the build and running 
   the autogen.sh script that at the end fails. Test it with

    watchman --version

6. run your app in android
   1. Enable wifi debugging
   2. adb connect ip:port
   3. test your connection with `adb shell`
   4. npx expo run:android


Tracking log
====================================================================

References
====================================================================
[2]: https://facebook.github.io/watchman/docs/install#-building-from-source
