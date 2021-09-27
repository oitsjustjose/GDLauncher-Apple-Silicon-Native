cd "`dirname \"$0\"`"

pip3 install -r requirements.txt

# Unload it if already loaded
launchctl list | grep com.oitsjustjose.lwjglpatcher && launchctl unload com.oitsjustjose.lwjglpatcher.plist 2>&1;
cp com.oitsjustjose.lwjglpatcher.plist ~/Library/LaunchAgents;

launchctl load com.oitsjustjose.lwjglpatcher.plist;

echo "Done with setup!"
exit