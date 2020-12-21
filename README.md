# Plotly Flask

## What is it? 

Basic Dash Web Application,  features use  Plotly, React.js and Flask.



## Two options to run the web app

### Via Python

* Option 1 
   
   
    python -m flask_dash.app
     
* Option 2

   
    FLASK_APP=flask_dash/app.py FLASK_ENV=development flask run --port 8080
    
### Via Docker    


Assumes  Docker and Docker Compose are installed

#### How to start?

    bash runner.sh

#### Rebuild

    docker-compose up --build --remove-orphans  --force-recreate  
    
### Preview

[Go to application on localhost http://localhost:8000/](http://localhost:8000/)




