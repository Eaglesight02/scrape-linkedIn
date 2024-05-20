#!/bin/bash

# Update apt
sudo apt update

# install chromium-chromedriver
sudo apt install -yq chromium-chromedriver

# Create a python virtual environment
python -m venv "linkedin_scraper"

# activate the venv
current_dir=$(pwd)
/usr/local/bin/virtualenv --python=python3 venv
echo $current_dir
activate () {
    . $current_dir/linkedin_scraper/bin/activate
}
activate


# Install selenium
pip3 install selenium==4.21.0