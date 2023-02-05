# secrets

You can use all these scripts to retrieve data from the otx.alienvault.com service and search for secrets in various storages, all popular clouds and firebase are collected.

Firebase Exploiter - https://github.com/reewardius/firebaseExploiter

APK Leaks: 

- https://github.com/arxenix/firebase-scanner
- https://github.com/shivsahni/FireBaseScanner
- https://github.com/dwisiswant0/apkleaks
- https://github.com/arijitdirghanji/Find-Hardcoded
- https://github.com/optiv/mobile-nuclei-templates
- https://github.com/r00tkie/grep-pattern
- https://github.com/m4ll0k/BBTz/blob/master/dapk.py

Secrets:

- https://github.com/newrelic/rusty-hog
- https://github.com/toufik-airane/leakin
- https://github.com/valayDave/tell-me-your-secrets
- https://github.com/Yelp/detect-secrets
- https://github.com/effortlessdevsec/ApkRecon
- https://www.youtube.com/watch?v=a255VGZn8dk
- https://youtu.be/6-M_7O3A8AI

Google Dorks - Cloud Storage:

- site:http://s3.amazonaws.com "target[.]com"
- site:http://blob.core.windows.net "target[.]com"
- site:http://googleapis.com "target[.]com"
- site:http://drive.google.com "target[.]com"
- site:http://aliyuncs.com "target[.]com"

For firebase there is nothing like that, use otx, get the last 250 results, and use firebaseExploiter utility to get potential endpoints that have read permission (/.json), download them out through curl and scan for secrets, or browse manually.

Tools for Android Pentest:

- https://hackmd.io/@EAn_g7N6SjWYxIeKEo4X7Q/HymJsIQyi
- https://github.com/MobSF/Mobile-Security-Framework-MobSF
