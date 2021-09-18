# LWJGL Watcher

This project is an "extension" of [tanmayb123's work](https://gist.github.com/tanmayb123/d55b16c493326945385e815453de411a) to get Minecraft (with LWJGL) running _natively_ on Apple Silicon Macs.

This repo is a compatibility helper for that project which adds support for GDLauncher, a popular modded minecraft launcher. In trying to add support for tanmayb123's work for GDLauncher I found that I had to replace the LWJGL3 jar file within the libraries of GDLauncher. However in doing so, GDLauncher would replace it with the correct jarfile every time a modpack is modified, updated or installed.

## Details

To get started, this application could've used WatchDog but it turns out that the way GDLauncher replaces the LWJGL file is not triggering WatchDog _at all_. Instead this program polls on varying intervals depending on the current environment. If GDLauncher is not running, this script does nothing until it starts running (because jar won't be modified by GDLauncher if it isn't running).

## Setting Up This Tool

### TODO

## Setting Up GDLauncher

To get set up with GDLauncher, it's actually surprisingly straight forward!! Begin by downloading this repo, either by cloning it or clicking the green `Code` button and selecting `Download As Zip`.

Once completed, you will need to unzip (if necessary) the repo folder and then `cd` into the directory. You will need to use the following command to prevent your modpacks from crashing as a result of Apple's macOS Quarantine system:

```bash
❯ xattr -r -d com.apple.quarantine ./lwjglfat.jar
❯ xattr -r -d com.apple.quarantine ./natives
```

Finally, you will need to replace all the contents of your instance's `natives` folder with the ones in this repo. I made a small GIF tutorial below to show you how:

![https://cleanshot-cloud-fra.s3.eu-central-1.amazonaws.com/media/581/9cuKxOLgqDJ8ibQ4JA72iIOp82TSajeZLKSYPUL6.gif?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaDGV1LWNlbnRyYWwtMSJHMEUCIQCsAJRjBXbWPF4psTo731EfirzU%2Byi5v1TUpDKRKp3F8wIgf2A7D8XT%2B9VjFupS8pQC5e8XL9x%2F%2Bel7z17Yb8XtVyMqqAIIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw5MTk1MTQ0OTE2NzQiDHDW9ig0lJDAfdvKgSr8Afz7zTyO7Povs9BIZJVZaIPMcRUIhq1I5ySlshrNGL1Ry5GevoMKa5U%2F9es%2B03gUrMis6NlifA2Olh6yfHyrgK9V6kVIff0mW9%2BogHwJ4jVjwpNG5BAG%2FOkPP5spFmVmqsUL1Uze1QcGOkRzODVMEkIEDgdCEzy5SPkHIR%2FHirSKo9DOcQgI5zSb4pMRRsrbSl0FpZ0f8cGOc2FkFKid86Wpx1xPRJfJ8ppGLQeOiSuYzUlSo71SGwGx6tBnH1QTCz8ZbCD6V2Ej%2BS4ZrpA4yH9KxhqBCA1Uo5n%2BkypgBP6AFmtZynM5Z1AV1vi%2B%2FdwQuNsXfVoLg6YPYULzDjCDqpeKBjqaAeAiEgzew41nXU4BtMU4%2BiIGT%2FsZ1Oza2SLWwGKdrK2L81dcig3SaPRPbR1BIAc%2FTsSoYVW2R55ZVU223k0iJqBXoFlL%2F0YTV8rCtVWz2c6suBW2iQ9Qz8YIs9W9KSXfvQ52ZR1BYM9Nr2aXeH1s4dIYMhlBF4pDFO4rbKU7xR%2Bn3ybtzoCWxYgl9LEdXinmUihDnxA5vAmvPMI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIA5MF2VVMNBCG2T26E%2F20210918%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20210918T125623Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Signature=69caf2eda1d5cec68369c385d3ef60d9bae92beb82181d09b4e3f68554a185f1](https://cleanshot-cloud-fra.s3.eu-central-1.amazonaws.com/media/581/9cuKxOLgqDJ8ibQ4JA72iIOp82TSajeZLKSYPUL6.gif?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaDGV1LWNlbnRyYWwtMSJHMEUCIQCsAJRjBXbWPF4psTo731EfirzU%2Byi5v1TUpDKRKp3F8wIgf2A7D8XT%2B9VjFupS8pQC5e8XL9x%2F%2Bel7z17Yb8XtVyMqqAIIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw5MTk1MTQ0OTE2NzQiDHDW9ig0lJDAfdvKgSr8Afz7zTyO7Povs9BIZJVZaIPMcRUIhq1I5ySlshrNGL1Ry5GevoMKa5U%2F9es%2B03gUrMis6NlifA2Olh6yfHyrgK9V6kVIff0mW9%2BogHwJ4jVjwpNG5BAG%2FOkPP5spFmVmqsUL1Uze1QcGOkRzODVMEkIEDgdCEzy5SPkHIR%2FHirSKo9DOcQgI5zSb4pMRRsrbSl0FpZ0f8cGOc2FkFKid86Wpx1xPRJfJ8ppGLQeOiSuYzUlSo71SGwGx6tBnH1QTCz8ZbCD6V2Ej%2BS4ZrpA4yH9KxhqBCA1Uo5n%2BkypgBP6AFmtZynM5Z1AV1vi%2B%2FdwQuNsXfVoLg6YPYULzDjCDqpeKBjqaAeAiEgzew41nXU4BtMU4%2BiIGT%2FsZ1Oza2SLWwGKdrK2L81dcig3SaPRPbR1BIAc%2FTsSoYVW2R55ZVU223k0iJqBXoFlL%2F0YTV8rCtVWz2c6suBW2iQ9Qz8YIs9W9KSXfvQ52ZR1BYM9Nr2aXeH1s4dIYMhlBF4pDFO4rbKU7xR%2Bn3ybtzoCWxYgl9LEdXinmUihDnxA5vAmvPMI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIA5MF2VVMNBCG2T26E%2F20210918%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20210918T125623Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Signature=69caf2eda1d5cec68369c385d3ef60d9bae92beb82181d09b4e3f68554a185f1)
