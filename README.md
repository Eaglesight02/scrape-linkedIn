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
sudo apt install -y chromium-browser
```
- Note: In ubuntu-based systems, it needs snap to work properly (for newer versions, it is installed by default) - need to put the versions of ubuntu here
