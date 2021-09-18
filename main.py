"""
Ensures that the LWJGL version is always the FAT version :)
"""

import hashlib
import os
import time
from shutil import copyfile

import psutil

JAR_PATH = (
    os.environ["JAR_PATH"]
    if "JAR_PATH" in os.environ
    else "~/Library/Application Support/gdlauncher_next/datastore/libraries/org/lwjgl/lwjgl/3.2.1/lwjgl-3.2.1.jar"
)


def main():
    """
    Makes 1-second loops to verify the moddedability of the LWJGL file
    """
    with open("lwjglfat.jar", "rb") as file:
        expected_md5 = hashlib.md5(file.read()).hexdigest()

    try:
        print("Starting. Use [^C] to quit.")
        while True:
            start = time.time()
            gdl_running = False

            # Detect if GDLauncher is running
            for proc in psutil.process_iter():
                try:
                    if proc.name() == "GDLauncher Helper":
                        gdl_running = True
                        break
                except (
                    psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess,
                ):
                    pass

            if not gdl_running:
                time.sleep(5)
                continue

            if os.path.exists(JAR_PATH):
                with open(JAR_PATH, "rb") as file:
                    md5 = hashlib.md5(file.read()).hexdigest()

                if md5 != expected_md5:
                    copyfile("./lwjglfat.jar", JAR_PATH)
            else:
                copyfile("./lwjglfat.jar", JAR_PATH)

            time.sleep(max(1 - (time.time() - start), 0))
    except KeyboardInterrupt:
        print("Quitting.")


if __name__ == "__main__":
    main()
