#!/bin/bash
# run mysql with sudo privilieges

script_name=$1
db_name=$2

cat $script_name | sudo mysql $db_name

