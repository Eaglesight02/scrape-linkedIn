#!/bin/bash

# Activate the existing venv:
source linkedin_scraper/bin/activate

# update apt
sudo apt update

# Download latest version of chromium-browser from ubuntu's official PPA
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Install the downloaded .deb file
sudo apt install -y ./google-chrome-stable_current_amd64.deb

# Get version:
output=$(google-chrome --version)

# Extract version from output
version=$(echo "$output" | awk "(print $3)")

# Get the correct version of chrome-driver:
wget "https://storage.googleapis.com/chrome-for-testing-public/$version/linux64/chromedriver-linux64.zip"

# Unzip the folder
unzip chromedriver-linux64

# Move the chromedriver file to binary folder:
sudo mv chromedriver-linux64/chromedriver /usr/local/bin

# Remove the downloaded files:
sudo rm -rf ./google-chrome-stable_current_amd64.deb
sudo rm -rf chromedriver-linux64
sudo rm -rf chromedriver-linux64.zip