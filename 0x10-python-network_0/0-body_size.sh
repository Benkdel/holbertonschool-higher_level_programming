#!/bin/bash
# get http body size using curl

URL=$1

curl -sI $URL | grep -i content-Length | awk '{print $2}'
