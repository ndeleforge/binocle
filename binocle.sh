#!/bin/sh

dir=$(dirname "$0")
venv_dir="${dir}/venv"

if [ -d "$venv_dir" ]; then
    . "${venv_dir}/bin/activate"
fi

 python3 "${dir}/source/binocle.py" "$@"
