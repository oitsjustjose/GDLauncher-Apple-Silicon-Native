# LWJGL Watcher

This project is an "extension" of [tanmayb123's work](https://gist.github.com/tanmayb123/d55b16c493326945385e815453de411a) to get Minecraft (with LWJGL) running _natively_ on Apple Silicon Macs.

This repo is a compatibility helper for that project which adds support for GDLauncher, a popular modded minecraft launcher. In trying to add support for tanmayb123's work for GDLauncher I found that I had to replace the LWJGL3 jar file within the libraries of GDLauncher. However in doing so, GDLauncher would replace it with the correct jarfile every time a modpack is modified, updated or installed.

## Details

To get started, this application could've used WatchDog but it turns out that the way GDLauncher replaces the LWJGL file is not triggering WatchDog _at all_. Instead this program polls on varying intervals depending on the current environment. If GDLauncher is not running, this script does nothing until it starts running (because jar won't be modified by GDLauncher if it isn't running).

## Setup

### Getting Started

Begin by downloading this repo, either by cloning it or clicking the green `Code` button and selecting `Download As Zip`.

Once completed, you will need to unzip (if necessary) the repo folder and then `cd` into the directory. You will need to use the following command to prevent your modpacks from crashing as a result of Apple's macOS Quarantine system:

```bash
❯ xattr -r -d com.apple.quarantine ./lwjglfat.jar
❯ xattr -r -d com.apple.quarantine ./natives
```

Once done you can proceed to the next step

### Setting Up LWJGL Patcher

1. Open `com.oitsjustjose.lwjglpatcher.plist` in TextEdit and replace `YOU WILL NEED TO CHANGE THIS TO THE PATH YOU CLONED THIS TO` with the actual path where you downloaded this project.
2. Double-click `setup.command` and you should see it say "Done with setup!". If you do, close the Terminal window that was created and you should be good to go!
3. Proceed with using the Zulu Java version and the rest of the instructions [found here](https://gist.github.com/tanmayb123/d55b16c493326945385e815453de411a)!

### Setting Up Your Instance

For every instance you have, you will need to replace all the contents of your instance's `natives` folder with the ones in this repo. I made a small GIF tutorial below to show you how:

![https://dv2ls.com/f/1JnYzUY2N](https://dv2ls.com/f/1JnYzUY2N)

## Known Issues and Workarounds

### Game Crashes with LWJGL Errors

If you know for certain everything has been configured correctly (you have verified that the LWJGL jar-file is being replaced with `./lwjglfat.jar` and your natives folder has been patched by hand as per the instructions), try restarting your mac. I had this issue recently and a restart miraculously fixed it.
