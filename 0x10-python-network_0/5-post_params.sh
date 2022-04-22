#!/bin/bash
# send post params 
curl -sX POST -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD' $1
