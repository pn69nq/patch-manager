#!/usr/bin/env bash
FILE_PATCH=app/build/outputs/apk/app-alibaba-release.apk
SERVER="http://192.168.1.142:5000/uploads"
curl -F "file=@$FILE_PATCH" $SERVER