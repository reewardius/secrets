# secrets

Mobile-Nuclei-Templates & Apktool
```
> find . -iname "*.apk" -exec apktool d -o {}_out {} \;
> nuclei -target /path-to-allapks/ -t /path-to-tamplates/mobile-nuclei-templates/
```

You can use all these scripts to retrieve data from the otx.alienvault.com service and search for secrets in various storages, all popular clouds and firebase are collected.

Firebase Dorks:
```
- Github: firebaseio.com
- site:github.com google-services.json
```
Firebase Exploiter - https://github.com/reewardius/firebaseExploiter

APK Leaks: 
```
- Recon https://github.com/hanhanhanz/apkframe
- https://github.com/arxenix/firebase-scanner
- https://github.com/shivsahni/FireBaseScanner
- https://github.com/dwisiswant0/apkleaks
- https://github.com/arijitdirghanji/Find-Hardcoded
- https://github.com/optiv/mobile-nuclei-templates
- https://github.com/r00tkie/grep-pattern
- https://github.com/teknogeek/get_schemas
- https://github.com/devkekops/checkkarlmarx
- https://github.com/jayateertha043/apksec
- https://github.com/sdushantha/dora
- https://github.com/talos-security/SEBASTiAn
- https://github.com/Cyber-Buddy/APKHunt
- https://github.com/utkarsh24122/apknuke
```
Secrets:
```
- https://github.com/newrelic/rusty-hog
- https://github.com/toufik-airane/leakin
- https://github.com/valayDave/tell-me-your-secrets
- https://github.com/Yelp/detect-secrets
- https://github.com/Skyscanner/whispers
- https://github.com/disruptops/cred_scanner
- https://github.com/effortlessdevsec/ApkRecon
- https://www.youtube.com/watch?v=a255VGZn8dk
- https://youtu.be/6-M_7O3A8AI
```
Google Dorks - Cloud Storage:
```
- site:http://s3.amazonaws.com "target[.]com"
- site:http://blob.core.windows.net "target[.]com"
- site:http://googleapis.com "target[.]com"
- site:http://drive.google.com "target[.]com"
- site:http://aliyuncs.com "target[.]com"
```
For firebase there is nothing like that, use otx, get the last 250 results, and use firebaseExploiter utility to get potential endpoints that have read permission (/.json), download them out through curl and scan for secrets, or browse manually.

Tools for Android Pentest:
```
- https://hackmd.io/@EAn_g7N6SjWYxIeKEo4X7Q/HymJsIQyi
- https://github.com/MobSF/Mobile-Security-Framework-MobSF
```
Additional

```
site:tesla.com -www -shop -share -ir -mfa
site:pastebin.com
site:jsfiddle.net
site:codebeautify.org
site:codepen.io "tesla.com"
site:tesla.com ext:php inurl:?
site:openbugbounty.org inurl:reports intext:"yahoo.com"
(site:tesla.com | site:teslamotors.com) & "choose file"
```
