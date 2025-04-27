
# Jedi Security Toolkit
# Full Python Script (Master Version 1.0)

import os
import sys
import subprocess
import socket
import random
import string
import time
from datetime import datetime

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import colorama
except ImportError:
    install("colorama")
    import colorama

try:
    import requests
except ImportError:
    install("requests")
    import requests

try:
    import scapy.all as scapy
except ImportError:
    install("scapy")
    import scapy.all as scapy

colorama.init(autoreset=True)

if not os.path.exists("results"):
    os.makedirs("results")

banner = colorama.Fore.GREEN + """
====================================
        Jedi Security Toolkit
====================================
 Domains: jedi-sec.com | jedi-sec.us | jedi-sec.cloud | jedi-sec.online | jedi-sec.me

 Choose your weapon wisely.
"""

# (Functions inserted here based on earlier exports...)
