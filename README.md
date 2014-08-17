Kiosk-Auto-Logout
=================

Automatically logs out specified user when application quits.

Initially inspired from Ross Shaffer and Andrew Uchenick's presentation "Replacing Dual Boots With Virtual Desktops in Managed Macs" at the 2014 Penn State MacAdmin's conference. 

Ross & Andrew's approach called for user action and two separate logins - user authenticates to the Mac, user launches Citrix client, user authenticates to the Windows VM. 

I wanted to make the experience more seamless for the enduser. I create a user named "Windows", with the Windows icon as the user picture. When that user is clicked, it launches the Terminal application and immediately brings the user to the Windows login. When the Win user is finished, they log out of the Terminal Server, and as soon as they quit the application it immediately returns them to the OS X login screen.

Setup
======

Create a local-only, account without a password. Configure it with parental controls and the limited finder, and restrict its allowed applications to a single app which auto-launches on login (Microsoft Remote Desktop in my case). 

Enter the shortname of the limited user and the process name of the allowed app (you can check for this in Activity Monitor) into /usr/local/CheckRunningProcess.py. 

Upon login, CheckRunningProcess.py checks if the current user is the one specified (and immediately exits if not). If the user is correct, the script pauses 10 seconds to allow the application to launch, and then tests if the process is running once a second.

If the process is not found, CheckRuningProcess.py creates an invisible file in the /Users/Shared directory. The LaunchDaemon definition watches for this file. Upon creation will fire the logout.sh script (as root) and kills the loginwindow process, immediately logging the user out.

Concerns
========

Q - Isn't this really a rough way to log someone out? Will they have an opportunity to save their documents if needed?

A - Yes, it is very heavy handed. No, they won't have a chance to save their docs once the application quits. However, if used in the controlled manner outlined above, it's a non-issue. Since the intent is for kiosk style functionality, the state of the OS X account is static and no user continuity is implied. Keep in mind that the VM/Terminal Server will provide all this - the Mac is a dumb terminal in this user's scope.


Installation
============

Copy LaunchAgent/com.github.binkleybloom.kioskautologout-la.plist to /Library/LaunchAgents

Copy LaunchDaemon/com.github.binkleybloom.kioskautologout-ld.plist to /Library/LaunchDaemons

Copy the contents of usr-local to /usr/local

Modify the appname and username variables in CheckRunningProcess.py to match your environment.

Warnings
========

I have not (yet) tested this with Fast User Switching. The logout.sh script kills any running loginwindow process to force the user to log out, so if more than such process exists... here be dragons.
