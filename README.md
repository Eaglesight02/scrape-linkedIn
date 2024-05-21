# scrape-linkedIn

Currently ccraping profiles with (almost) all the different nuts and bolts that people on LinkedIn have on their profiles.

---

# Requirements:

- python(<=3.12.3)
- pip(>=24.0)
- selenium(Python client, version = 4.21.0)
- google-generativeai(0.5.4)

---

# There is a setup.sh script for ubuntu-based systems, run it using:

```sh
cd <navigate_to_your_required_directory>
```

```sh
source setup.sh
```

---

# The commands used in setup.sh are given below with explanations:

## It's better to use a virtual environment to manage the installs

### Creating a virtual environment in linux:

```py
python -m venv "linkedin_scraper"
```

### Activate the venv:

```py
source <path_to_venv_folder>/bin/activate
```

### Upgrade pip:

```py
pip install --upgrade pip
```

### Download the required version of selenium:

```py
pip install -q selenium==4.21.0
```

### Download dotenv(to load .env files):

```py
pip install -q python-dotenv
```

### Download required version of google-generativeai

```py
pip install -q google-generativeai==0.5.4
```

### Upgrade apt (in case of ubuntu):

```sh
sudo apt update
```

### Download chromium-chromedriver for linux:

```sh
sudo apt install -yq chromium-chromedriver
```
