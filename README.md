# Price scraping for amazon

## Requirement 
- python 3
- docker

## Setup 
- Create a virtual environment, you can run: `rm -rf venv  && virtualenv venv"`
- Activate the virtual environment: `source $(pwd)/venv/bin/activate`
- Install python packages: `sudo pip install -r requirements.txt`

## Docker 
To build the image run: `docker build -t price-scrapping:0.0.1 .`
To see the built image: `docker images`
To run a container: `docker run --name price -d price-scrapping:0.0.1 `
