#!/bin/bash

if [ $# -lt 1 ]; then
    printf "Usage: $0 <operation> <options>\n"
    printf "Operations:\n"
    printf "\tactivate <-f to force recreation of venv>\n"
    printf "\tdeactivate\n"
    printf "\ttest\n"
    printf "\tpylint\n"
    printf "\trun\n"
    printf "NOTE: To use the activate & deactivate operations this script must be called like so:\n"
    printf "\t. ./letsDevelop.sh\n\n"
    exit
fi

if [ $1 == "activate" ]; then
    if [ "$2" == "-f" ]; then
        printf "Forcing new creation of virtual environment\n"
        rm -rf ./venv
    fi

    if [ ! -d ./venv ]; then
        printf "Creating virtual environment\n"
        python3 -m venv venv

        printf "Activating virtual environment\n"
        source venv/bin/activate

        printf "Installing required packages\n"
        pip install pip --upgrade
        pip install -e .
        pip install -r tests/pip_requirements.txt
    else
        printf "Activating virtual environment\n"
        source venv/bin/activate
    fi
fi

if [ $1 == "deactivate" ]; then
    printf "Deactivating virtual environment\n"
    deactivate
fi

if [ $1 == "test" ]; then
    source venv/bin/activate
    pytest tests/
    deactivate
fi

if [ $1 == "pylint" ]; then
    source venv/bin/activate
    pylint tests/
    deactivate
fi
