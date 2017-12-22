#!/usr/bin/env bash
baseUrl="localhost:5000/share/getPatch"

#curl -d "param1=value1&param2=value2" $baseUrl
curl -sS -X POST $baseUrl