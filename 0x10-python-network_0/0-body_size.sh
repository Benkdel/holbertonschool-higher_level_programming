#!/bin/bash
# get http body size using curl
curl -sI $1 | grep -i content-Length | awk '{print $2}'
