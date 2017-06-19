#!/usr/bin/env bash

if [[ $# -ne 1 ]]; then
    echo 'Usage: ./find_title.sh <PROBLEM_NUMBER>'
fi

n=$(( 10#$1 ))

if [[ $n -lt 10 ]]; then
    n="00$n"
elif [[ $n -lt 100 ]]; then
    n="0$n"
fi

result=$(grep -h --no-filename -re "^$n:" . )

if [[ $? -eq 0 ]]; then
    echo $result
else
    echo "Could not find problem."
fi
