Compiling Android from CLI
====================================================================
> In this guide you will find how to compile an android app from your terminal! Please go directly to the Tips section for a quick start.



REQUIREMENTS
====================================================================
- A linux machine (This was tested on Debian 11)
- Git: To clone the Android samples repo
- Android _Command Line Tools_: The tools to build the app
- Java: Download from [here](https://jdk.java.net/java-se-ri/17-MR1)
  * Just download, move to `/opt`, extract and add to the `PATH` in bashrc.
  
  
  
NOTES FOR LEARNING
====================================================================
Each android version is more complex than the previous. It is more easy to understand old java applications than newly developed Kotlin ones. There official unsupported repositories with old apps:

  - [sunflower](https://github.com/android/sunflower) shows a two screens (activities) app.
  - [widgets example](https://github.com/android/views-widgets-samples/) shows all the widgets but in one activity.
  
There is together with this main fail a `build.gradle` file with useful code to download dependencies.





BUILDING
====================================================================
For this steps the `gradlew build` does not work, instead use the `assembleDebug` task.
The two subsections below are independent from each other.


Running the minimal app
-----------------------
Here you will run the minimal android application. Since we are doing everything from terminal it is an excellent starting point.

1. Please download the minimal sample from [here](https://docs.gradle.org/current/samples/sample_building_android_apps.html)

2. Unzip an review the project contents:

   unzip sample_building_android_apps-kotlin-dsl.zip
   cd app


Running a fully fledged sample
------------------------------
Here you will run an application that implements some of the features of Android API .e.g. camera, widgets, etc.

1. Clone the repository:

   git clone https://github.com/android/user-interface-samples/tree/main
   
2. `cd` into one of the samples.

3. List tasks and install:
   
   ./gradlew tasks
   ./gradlew assembleDebug

   
   
   
   
DEPLOYING
====================================================================
The greater the version in the platform e.g. `platform-xx` the newest the Android API is. A newer Android API consumes more resouces and requires a better computer to emulate the device. In my case `platform-33` freezes my computer.  
In low specs computers is a good idea to use an older API e.g. `platform-25` and then modify the `targetSdk` attribute in `app/build.gradle` file, so you application will compile to an older platform.

To physical device via USB
--------------------------------------
3. Download _Command Line Tools_ only [here](https://developer.android.com/studio#command-tools). Then move the downloaded file to `/opt` folder, and finally extract (as always).

4. Install the _Command Line Tools_ by following this [guide](https://developer.android.com/tools/sdkmanager). Add the Command Line Tools to your path at the end of the `.bashrc` file:

   ~~~sh
   $ANDROID_HOME=/path/to/command/line/tools
   export PATH=$ANDROID_HOME:$PATH
   ~~~

5. Install the apk build tools with the newly installed `sdkmanager`
  
   sdkmanager "platform-tools" "platforms;android-33"

6. Enable USB Debugging in your phone. Click in 'OK' on the floating dialog that will appear in your phone.

7. Check that your device appears as `attached` after your issue `adb devices` command.

8. Enable install via USB in your phone. In Xiaomi you need an account! (What the fuck!!)

9. Install the apk in your phone, press _OK_ in the dialog that will appear in your phone:

   adb -d install app/build/outputs/apk/debug/app-debug.apk 

### USB Debugging
For ease the process

1. Always enable developer options by:
   - tapping the android version in config settings 
   
2. After you complete your session always
   - **disable dev options** after you complete your session disble it by moving the developer options enablement toggle
   - **enable again play protect**: _Google Play_ > _User Icon_ > _Play Protect_ > _Enable Disable_


To physical device via Wi-Fi
--------------------------------------
1. Enable WiFi debugging. The phone will let you know an ip:port and a 6 digit code
2. From client computer:
    
   adb pair ip.port
 
   Then type the 6 digit code as requested.
3. Connect (attach) to your phone:

   adb connect ip:port



To emulated device
--------------------------------------
This procedure will start from step 5 in previous section.

6. Install an Android platform system image:
   
   ~~~sh  
   sdkmanager "system-images;android-33;google_apis;x86_64"
   ~~~

   to remove an image:
   
   ~~~sh
   sdkmanager --uninstall "system-images;android-25;google_apis;x86"
   ~~~

   If you ommit the double quotes in _bash_ the command will behave different.


7. Create an _Android Virtual Device_ from the previous platform image. More details [here](https://developer.android.com/tools/avdmanager#commands_and_command_options)

   ~~~sh
   avdmanager create avd -n test -k "system-images;android-33;google_apis;x86_64"
   ~~~

   To delete and avd

   avdmanager delete avd -n test

8. List AVDs then start the virtual (emulated) device: 

   emulator -list-avds
   emulator -avd test 

9. List running devices (the emulator should appear in attached mode), then install the apk:
  
   adb devices
   adb install app/build/outputs/apk/debug/app-debug.apk 

   
For more information about the emulator see [this](https://developer.android.com/studio/run/emulator-commandline).

To Uninstall from terminal
---------------------------------
10. J:

   adb shell pm uninstall "com.example.android.text"
  
  
   
   
   
ADAPTING THE KOTLING TUTORIAL TO JAVA
====================================================================
The base app was taken from a gradle guide that you can find [here](https://docs.gradle.org/current/samples/sample_building_android_apps.html)
First I was looking for the `Text` class. I arrived to the following [page](https://developer.android.com/jetpack/androidx/releases/compose-material3). There you will see that is the _Material UI_ library, that belongs to the _JetPack_ libraries. Since the app in the tutorial uses a gui element based on the kotlin libraries, after doing a little research with a search engine we found this [page](https://developer.android.com/reference/com/google/android/material/packages). There we tracke down the most similar UI element to replace the `Text` from the most recent tutorial at the moment (January 2025). The best candidate was [MaterialTextView](https://developer.android.com/reference/com/google/android/material/textview/MaterialTextView).
When trying to implement the [`Modifier`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier) element, I found that in recent versions of Android (say 2021) there is this new pattern to introduce customization to UI elements through this `Modifier` element.
Now I have a problem trying to access by id the `MaterialTextView` element. This [page](https://developer.android.com/reference) at the end of the page, can help to understand the transtion between Java and Kotlin. For now my impression is that now everything must be done in Kotlin, because Java API is not supported anymore.
I was getting an error when the app tryed to parse the XML layout. I get the error after using `adb shell` and inside the shell issuing `logcat *:E` to log on the terminal all the errors. The error was that, the runtime did not find the `MaterialTextView` class from 


   


RUNNING TESTS
====================================================================
There are [two kind](https://developer.android.com/studio/test/command-line) of tests, normal tests and connected tests. The former are unit tests and the second are tests that needs a device or emulator running to be run (they called instrumented tests):

   ./gradlew test
   ./gradlew connectedAndroidTest
   
## Take the control
You can run the instrumented tests from the [cli](https://developer.android.com/studio/test/command-line#run-tests-with-adb). Please note that you need to install the tests apk (yes another apk is generated for instrumented tests) to be able to run the tests:

1. first get your instrumentation list. From there identify your app instrumented tests:

  adb shell pm list instrumentation

2. then run your tests

  adb shell am instrument -w com.google.samples.apps.sunflower.test/android.support.test.runner.AndroidJUnitRunner                                                                           
   
   
   
TOOLS
====================================================================
You can speed up your development process by adding this to your `.bashrc`:


Assisted Debugging
---------------------------------
There are two ways to visually debug, with the classic `jdb` cli:

  jdb -attach localhost:1234
  
Withing the jdb session you can add breakpoints like this:

  stop in com.google.samples.apps.sunflower.PlantListActivity.onCreate

Or with vscode through (Java Debug Plugin)[https://open-vsx.org/extension/vscjava/vscode-java-debug] (also needs this [Java Language support](https://open-vsx.org/extension/redhat/java) plugin:

~~~json
   {
      "request": "attach",
      "hostName": "localhost",
      "port": 1234,
      "sourcePaths": ["/home/jcammmmm/repo.o/sunflower/app/src/main/java/"]
   }
~~~


Compile, Run and forward the Java Debug Wire Protocol
-----------------------------------------------------
In the following command you should place one of the activities from `Manifiest.xml` file.

~~~sh 
arun() {
  # from 'build.gradle'
  APP_ID=$1
  # from 'AndroidManifiest.xml'
  MAIN_ACTIVITY=$2
  # by looking at folder structure
  APP_FOLDER=$3
  # from 'AndroidManifiest.xml'
  PACKAGE=$4
  
  if [[ -z $APP_ID ]] then
    APP_ID="com.google.samples.apps.sunflower"
  fi
  if [[ -z $MAIN_ACTIVITY ]] then
    MAIN_ACTIVITY="PlantListActivity"
  fi
  if [[ -z $APP_FOLDER ]] then
    APP_FOLDER="app"
  fi
  if [[ -z $PACKAGE ]] then
    PACKAGE=$APP_ID
  fi
  
  echo app id: $APP_ID
  echo main activity class: $MAIN_ACTIVITY
  echo app folder root: $APP_FOLDER
  echo package name: $PACKAGE
  
  ./gradlew assembleDebug
  # When you uninstall and then install (not reinstall -r)
  # the OS does not remember that you already installed and 
  # will request from you to tap on 'accept', which is a waste
  # of time when you can omit that option
  # adb shell pm uninstall $PACKAGE
  adb install -r $APP_FOLDER/build/outputs/apk/debug/$APP_FOLDER-debug.apk
  # Accept to install this harmful app
  adb shell input tap 295 2228
  # am : activity manager
  adb shell am start -a android.intent.action.MAIN -n $APP_ID/$PACKAGE.$MAIN_ACTIVITY
  adb shell input tap 100 100
  
  # enable debugging
  PID=$(adb shell ps | grep sunflower | cut -d' ' -f5)
  adb forward tcp:1234 jdwp:$PID
}
~~~

Launch dev terminals
---------------------------------   
To select text press shift while select, then Ctrl + Shift + C

Moreover, add the following to the bashrc [4]:

~~~sh
   tmx () {
      tmux new-session -d -s ANDROID_DEV
      tmux new-window -n emulator
      tmux new-window -d -n src1
      tmux new-window -d -n src2
      tmux new-window -d -n compile
      tmux new-window -d -n logs
      tmux attach-session -d -t ANDROID_DEV
   }
~~~

Back quick in time
---------------------------------
Copy and paste the following script to your bashrc:

~~~sh
ttravel() {
   git checkout main
   commits=$(git log --reverse --pretty=oneline | cut -d' ' -f1)
   pos=$(($(< CURR_V)))
   i=0
   echo "===========================> moving to v$pos"
   for h in $commits; 
   do  
     i=$((i + 1))
     if [[ $i -eq $pos ]]; then
       git checkout $h
       break
     fi
   done
   pos=$((pos + 1))
   echo $pos > CURR_V
}
~~~


   
Logging
---------------------------------
Log strings in code with:

   Log.i("XXX", "buahahahahhahhahahaha!")
   
then filter the logs with:
   
   adb logcat -v color
   adb logcat *:E
   adb logcat MyActivity:I MyApp:D *:S
   adb logcat -v brief -v color -s ActivityManager:* XXX:*
   adb logcat -v brief -v color -s ActivityManager:* XXX:* AndroidRuntime:*
   adb logcat -v brief -v color -s RV:* AndroidRuntime:*

Import this to print out object attributes:

~~~groovy
   // https://mvnrepository.com/artifact/org.apache.commons/commons-lang3
   implementation 'org.apache.commons:commons-lang3:3.7'
~~~
   
log attributes with:

~~~java
   Log.i("XXX", ReflectionToStringBuilder.toString(actionBar, ToStringStyle.MULTI_LINE_STYLE));
~~~
   
log stacktrace with one of these two:^

~~~java
   Arrays.toString(Thread.currentThread().getStackTrace()).replace( ',', '\n' )
   Log.d("XXX", org.apache.commons.lang3.exception.ExceptionUtils.getStackTrace(new Exception()));
~~~

More details [here](https://developer.android.com/tools/logcat#filteringOutput).   
   
   
   
   
TROUBLESHOOTING
====================================================================
If your emulator does not start:

1. list packages

  adb shell cmd package list packages -3 -f

2. clean start
  
  emulator -avd test -wipe-data
   
   
   
   
TRACKING
====================================================================
- 250615: Reviewing again for ReactNative purposes
- 250609: Reviewing this text as reference to work with React-Native-Expo.
- 250412: Java application code assisted debugging with jdb and vscode. The objective is to debug the tests!
- 250212: Reading about databinding clases that are autogenerated  
- 250206: I can compile the minimal app in Java!
- 250203: Working in the Android tutorial but in Java
- 250201: Getting the base project to run.
- 250117: Initial version
- 250118: Added steps for deploy on virtual device.

References
====================================================================
[1]: https://www.gnu.org/software/bash/manual/bash.html#Positional-Parameters
[2]: https://docs.docker.com/engine/reference/builder/#entrypoint
[3]: https://zookeeper.apache.org/doc/r3.9.1/javaExample.html
[4]: https://stackoverflow.com/questions/48997929/how-do-i-create-a-tmux-session-with-multiple-windows-already-opened
