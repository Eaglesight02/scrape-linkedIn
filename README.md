# scrape-linkedIn
Currently scraping profiles with (almost) all the different nuts and bolts that people on LinkedIn have on their profiles.


# Requirements:
- python(3.12.3)
- pip(24.0)
- selenium(Python client, version = 4.21.0)


## It's better to use a virtual environment to manage the installs
### Creating a virtual environment in linux:
```py
python -m venv "linkedin_scraper"
```
### Activate the venv:
```py
source <path_to_venv_folder>/bin/activate
```


## Download chrome and chromedriver for linux based system (debian with apt):
- Update repositories:
```sh
sudo apt update
```
- Download the latest version of chromium-browser from ubuntu's official PPA (Personal Package respository)
```sh
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```
- Install the downloaded debian package
```sh
# Navigate to the directory where you've downloaded the debian package
sudo apt install ./google-chrome-stable_current_amd64.deb
```
- Remove the debian package after installation
```sh
# Navigate to the directory where you've downloaded the debian package. (Note, use "sudo rm -rf" with caution)
sudo rm -rf ./google-chrome-stable_current_amd64.deb
```
- Check the version of the chromium browser
```sh
google-chrome --version
```
- Download the required chromium-driver as per the given version of the chrome browser:
    - For stable releases (until version 114.0.5735.90 at the time of writing) - [link](https://developer.chrome.com/docs/chromedriver/downloads)
    - For experimental releases (until the latest versions) - [link](https://googlechromelabs.github.io/chrome-for-testing/)   
- For 64-bit linux-based systems:     
```sh
wget https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/linux64/chromedriver-linux64.zip
```
- Unzip the zip folder
```sh
# Make sure you are in the same directory as the downloaded zip file
unzip chromedriver-linux64
```
- Move the chromedriver file to binary folder:
```sh
# Make sure you are in the same directory as the downloaded zip file
sudo mv chromedriver-linux64/chromedriver /usr/local/bin
```
- Remove the downloaded zip file after successful installation
```sh
# Make sure you are in the same directory as the downloaded zip file
sudo rm -rf chromedriver-linux64.zip
```