# -TorNet-installer-v1.15-

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](#)

**This tool has been created to simplify the TorNet deafult installation: using python it automatically installs pip (if it's missing from the user's device), TOR, TorNet and bypasses the "Externally managed device error" that can be encountered with the newest versions of sudo. It also makes sure that every piece of software is up-to-date and that there are no missing dependencies, nor syntaxt errors.**

---

# This current version is for Ubuntu/Debian-based distributions.
You must also have python 3 installed.

**-How to install python 3:**

-Start off by using: ```sudo apt update```, if any updates are available type this command: ```sudo apt upgrade``` to install them.

-Install python 3: ```sudo apt install python3```

-Verify the installation with: ```python3 --version```

---

# How to use this program:
-Once you verified that you have Python 3, download inst_deb.py from the releases section, and place it in Home/User...

-Open your terminal and use: ```python3 instdeb.py```

-You will be prompted to insert your password and the installation will begin.

# How to use TorNet:
-At the end of installation it will start automatically, however you can use:                                                           
```sudo tornet --interval (Seconds that pass between tor refresh) --count (How many times tor will refresh)``` to start tornet anytime.

Example: ```sudo tornet --interval 10 --count 0 ```                                                                               
If count is set to 0, the program will go on until the terminal window is closed...
Please note that the shorter the interval is, the slower your wifi connection will become.

# Service not found error:

If you receive the error:  ```sh: 1: service: not found``` instead of using the tornet command, launch the installer again.
(If Tor and TorNet are pre-installed the installer will just find the current errors, check for updates and start tornet)

This installer is kinda pointless ngl...you can just use commands to install tornet....

[![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](#)
