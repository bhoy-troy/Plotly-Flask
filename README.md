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

    bash runner.sh true   
     
### Preview

Go to application [Flask](http://172.20.20.100:8000/)

Go to application via [Nginx](http://172.20.20.101)



