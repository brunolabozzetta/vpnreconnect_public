@echo off
color 6f
START "" /I FortiSSLVPNclient disconnect
taskkill /im forticlient.exe /f
taskkill /im FortiSSLVPNclient.exe /f
taskkill /im FortiTray.exe /f
START "" /I FortiSSLVPNclient connect -h 200.221.49.142:3333 -u user:password123 -i -q -m
timeout 10
color 2f
timeout 5
exit
