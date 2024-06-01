#!/bin/sh

dir=$(d=$(dirname "$0"); cd "$d" && pwd)
dir=$(echo $dir | sed 's/ /\ /g')
python3 "${dir}/../binocle/binocle.py" $*
