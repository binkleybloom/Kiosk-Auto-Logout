Kiosk-Auto-Logout
=================

Automatically logs out specified user when application quits.

Installation
============

Copy LaunchAgent/com.github.binkleybloom.kioskautologout-la.plist to /Library/LaunchAgents

Copy LaunchDaemon/com.github.binkleybloom.kioskautologout-ld.plist to /Library/LaunchDaemons

Copy the contents of usr-local to /usr/local

Modify the appname and username variables in CheckRunningProcess.py to match your environment.

Warnings
========

I have not (yet) tested this with Fast User Switching. The logout.sh script kills any running loginwindow process to force the user to log out, so if more than such process exists... here be dragons.
