#!/bin/bash

echo "Running build script"

# Getting the source file path using this technique as it allows for symbolic links
SCRIPT_DIR=''
pushd "$(dirname "$(readlink -f "$BASH_SOURCE")")" > /dev/null && {
    SCRIPT_DIR="$PWD"
    popd > /dev/null
}
echo $SCRIPT_DIR
cd "$SCRIPT_DIR"

rm -fr build
rm -fr dist
rm -fr dim.egg-info

python setup.py sdist bdist_wheel