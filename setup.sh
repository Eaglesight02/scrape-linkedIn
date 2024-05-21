#!/bin/bash

# To check if last command is executed perfectly or not:
check_last_command() {
    if [ $? -eq 0 ]; then
        return 0            # Success
    else
        return 1            # Failure
    fi
}

# Create a virtual environment in the current directory
python -m venv "linkedin_scraper"
if check_last_command; then
    echo "Created virtual environment"
else
    echo "Failed to create virtual environment"
    exit 1
fi

# Activate the virtual environment in the current directory
current_dir=$(pwd)
/usr/local/bin/virtualenv --python=python3 venv
echo $current_dir
activate () {
    . $current_dir/linkedin_scraper/bin/activate
}
activate

# Check if virtual environment is activated or not
python_src_dir=$current_dir/linkedin_scraper/bin/python
current_python_src_dir=$(which python)

if [ "$python_src_dir" == "$current_python_src_dir" ]; then
    echo "source activated"
else
    echo "source is not activated!!!, check for errors and run the script again!!"
    exit 1
fi

# Upgrade pip
pip install --upgrade pip
if check_last_command; then
    echo "Upgraded pip"
else
    echo "Failed to upgrade pip"
    exit 1
fi

# Download the latest version of selenium
pip install -q selenium==4.21.0
if check_last_command; then
    echo "Installed selenium successfully"
else
    echo "Failed to install selenium"
    exit 1
fi

# Download dotenv(to load dotfiles)
pip install -q python-dotenv
if check_last_command; then
    echo "dotenv installed successfully"
else
    echo "dotenv failed to install"
    exit 1
fi

# Download the required version of google-generativeai
pip install -q google-generativeai==0.5.4
if check_last_command; then
    echo "Installed google-generativeai successfully"
else
    echo "Failed to install google-generativeai"
fi

# Update apt
sudo apt update

# Install chromium-chromedriver
sudo apt install -yq chromium-chromedriver
if check_last_command; then
    echo "chromium-chromedriver installed successfully"
else    
    echo "Failed to install chromium-chromedriver"
fi