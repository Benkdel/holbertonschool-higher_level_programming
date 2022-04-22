#!/bin/bash
# send json data
curl -H "Content-Type: application/json" -X POST -d @$2 $1
