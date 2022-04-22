#!/bin/bash
# get options available
curl -LisX OPTIONS $1 | grep -i allow | cut -d ' ' -f2-
