#!/bin/bash
# get options available
curl -s $1 | grep -i allow | cut -d ' ' -f2-
