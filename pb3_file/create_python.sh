#!/bin/bash
protoc -I . --python3_out=../pb3 *.proto
