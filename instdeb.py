###################################################
import os #this is essential if we want to run cmds!
# The purpose of this Python script is to automate the installation process of tornet, 
# some errors are automatically resolved by this script 
# (I'll try to find and implement more fixes in the future.)
# Just type "Python3 (this scipt's name).py" to begin installation.

# Don't have python3? run the following commands:
#
# "$ sudo apt update" (If there is an update available, use "$ sudo apt upgrade")
# "$ sudo apt install python3"
# "$ python --version" (Check if you have the right vers.)
#
#
# Go to line 38 to edit count and interval :)
## if count is set to 0 tornet will reload endlessly.
## interval between tor reloads is set to 15s normally.
## Lower interval = less stable connection and slower wifi.

print("") #leaving empty spaces for more order :)
print("")
print("Make sure you set up your browser proxy settings correctly.")
print("must-have settings: Manual proxy conf. ; Socks host (127.0.0.1) ; Port (9050) ; Socks v5 ; DNS active")
print("") #leaving empty spaces for more order :)
print('''\033[93m\033[1mWARNING! THIS SCRIPT WILL EXECUTE <--BREAK-SYSTEM-PACKAGES> 
DUE TO SOME ISSUES WITH EXTERNALLY MANAGED ENVIROMENTS! 
(This happens if you have downloaded the latest version of sudo)''')
print("") #leaving empty spaces for more order :)
print("DOWNLOAD THE ALTERNATIVE VERSION ON GITHUB IF YOU THINK THAT YOU WILL NOT.") 
print("ENCOUNTER ANY EXTERNAL ENVIROMENT-RELATED ERROR.")
print("")
print("") #leaving empty spaces for more order :)


#####################################
### ACTUAL COMMANDS ARE DOWN HERE ###
#####################################


cmd = "sudo apt install tor && sudo apt install python3-pip && sudo pip install tornet --break-system-packages && sudo systemctl start tor && tornet --auto-fix  && clear && sudo tornet --interval 15 --count 0"

#view tornet official github page for cmd list (https://github.com/ByteBreach/tornet) 
returned_value = os.system(cmd)  # returns the exit code in unix
instoutput = returned_value
print("")
print("[Tornet Auto-fix performed! (cmd: tornet --auto-fix)]")
print("") #leaving empty spaces for more order :)
print('Output (OS.system returned value):', instoutput)
print("")

### Once everything is installed you can launch tornet through any terminal (Doesn't have to be root) ###

