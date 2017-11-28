#!/bin/bash
curl -X POST -H "Accept: application/x-protobuf" \
    -H "Content-type: application/x-protobuf" \
    http://127.0.0.1:5000/hellopb --data-binary @person.pb > team.pb