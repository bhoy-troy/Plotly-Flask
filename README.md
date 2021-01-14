# Plotly Flask

## What is it? 

Basic Dash Web Application,  features use  Plotly, React.js and Flask.

## Two options to run the web app

##### Note:
__Docker is not required to run the flask app__

### Via Python

The simplest way is to run the bash file `python_runner.sh`

* Option 1

    ./python_runner.sh
    
    
* Option 2
   

    python -m flask_dash.app
     
* Option 3
   
    FLASK_APP=flask_dash/app.py FLASK_ENV=development flask run --port 8080
    
### Via Docker    

__This assumes Docker and Docker Compose are installed__

#### How to start?

    bash runner.sh

#### Rebuild

    bash runner.sh true   
     
### Preview

##### Plain Python 

Go to application [Flask](http://localhost:8000/)

##### When running Docker containers

Go to application [Flask](http://172.20.20.100:8000/)

Go to application via [Nginx](http://172.20.20.101)



### Clean Up

    isort .
    black .
    
##### Docker Lint

    docker run --rm -i hadolint/hadolint < flask_dash/Dockerfile
    docker run --rm -i hadolint/hadolint < nginx/Dockerfile