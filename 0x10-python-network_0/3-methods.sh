#!/bin/bash
# get options available
curl -s $1 | grep -i Allow | cut -d " " -f2-
