#!/bin/bash
echo Script name: $0
echo "Total number of arguments:" $#
if [ "$#" -eq 0 ]; then
    echo "Arguments Count: No arguments provided."
elif [ "$#" -eq 1 ]; then
    echo "Arguments Count: 1"
elif [ "$#" -eq 2 ]; then
    echo "Arguments Count: 2"
elif [ "$#" -gt 2 ]; then
    echo "Arguments Count: 2+"
fi

