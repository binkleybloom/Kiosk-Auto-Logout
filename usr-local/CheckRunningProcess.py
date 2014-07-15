#! /usr/bin/python

"""
This script watches a specific process "appname" for a specific user "username", and logs the user out when the process exits.
Tim Schutt, taschutt@syr.edu
July, 2014
"""

import os, subprocess, sys, time

appname = "Microsoft Remote Desktop" # set to the name of the app you wish to monitor
username = "test" # set to the shortname of the kiosk user

def processrunning():
  cmd = ["/usr/bin/pgrep", appname]
  proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  (output, error_output) = proc.communicate()
  return output

def main():
  if processrunning():
    time.sleep(1)
    main()
  else:
    os.system("/usr/bin/touch /Users/Shared/.com.github.binkleybloom.logoutnow")
    sys.exit(0)

if __name__ == "__main__":
  if os.getlogin() == username:
    time.sleep(10) # waits 10 seconds for application to launch before checking
    main()
  else:
    print "Whoops! Wrong user."
    sys.exit(0)