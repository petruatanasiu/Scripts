#! /usr/bin/env bash

#tree $1

#function demo(){
# tree $1
#}

#demo /Users/petru/Lucru

read="$1"

if [[  "${read}" =~ [0-9] ]]; then
 echo 'Numeric'
else
 curl https://wttr.in/"${read}"
fi
