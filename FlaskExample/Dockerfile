FROM ubuntu

RUN echo 'Dockerfile first try =)'

RUN apt update
RUN apt -y install python3 python3.8-venv pip git

RUN git clone https://github.com/OliverZott/docker-examples.git
WORKDIR /docker-examples/FlaskExample/
RUN python3 -m venv venv
RUN pip install -r env.txt 

ENTRYPOINT FLASK_APP="app.py" flask run --host=0.0.0.0