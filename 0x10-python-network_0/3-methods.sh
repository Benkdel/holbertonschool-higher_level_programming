#!/bin/bash
# get options available
curl -sI $1 | grep -i Allow | cut -d " " -f2-
