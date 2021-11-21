# Flask Minimum web-api example

## Create Web-App

### Create Environment

https://flask.palletsprojects.com/en/2.0.x/installation/#install-flask

- `mkdir FlaskExample\`
- `cd .\FlaskExample`
- `python -m venv venv`
- Activate env:
  - windows: `.\venv\Scripts\activate`
  - linux: `. venv/bin/activate`
- `pip install -r env.txt` or `pip install Flask`
- in IDE: select python.exe from venv dir!! (`\venv\Scripts\python.exe`)

### Create Web-App

https://flask.palletsprojects.com/en/2.0.x/quickstart/

## Run

https://flask.palletsprojects.com/en/2.0.x/cli/

- In IDE set working-directory (`FlaskExample`)
- In Shell:

  > export FLASK_APP=app    
  > export FLASK_ENV=development    
  > flask run    

  - if file named `app.py`, no env-var needed. just `flask run`

#### To set non-routable meta-address and Port
- `flask run --host 0.0.0.0 --port 80`


------------------------------------------------------------
# Docker-Image
In terminal (directory of DOCKERFILE) run
- `docker build . -t image_name`  ... **-t** for tag
- check: `docker images`
- run: `docker run image_name`

Docker hub repo: https://hub.docker.com/repository/docker/dasmuesli/minimum_flask_app




------------------------------------------------------------
# Docker run 
- `docker run -e APP_NAME=Scotty flask_startrek-star_trek`