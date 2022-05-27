#!/usr/bin/env python3

import re
import sys
import os
import requests as r
import urllib.request
import wget

filedir = os.path.join( "video" )

LINK = input( "Enter video url here >>>\n" )

try:
    html = r.get(LINK)
except r.ConnectionError as e:
    print("Error in connecting")
except r.Timeout as e:
    print("Timeout")
except r.RequestException as e:
    print("Invalid URL")
except (KeyboardInterrupt, SystemExit):
    print("System has quit")
    sys.exit(1)
except TypeError:
    print("Video seems to be private ")
else:
    print("\n")
    print("Video Quality:Normal " )
    print("[+] Starting Download")
    try:
        url=re.search( 'hd_src:"(.+?)"',html.text)[1]
        print("Find the HD quality")
    except:
        url=re.search( 'sd_src:"(.+?)"',html.text)[1]
        print("Find the SD quality")


    print( "Downloading the video ........." )
    urllib.request.urlretrieve( url, "Video.mp4")
    print("\n")
    print("Video downloaded")
