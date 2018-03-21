# Movie Recommendation Flask App

## Project Objective 
This repo can be used to produce a simple movie recommendation web app. The app is written with `Python 3.6`.

## Team Members
* Developer: Wenjing Yang
* Product Owner: Matt Gallagher
* QA: Jamie Chen

## Project Charter
Build a movie recommender system to suggest movies for users. Users can get better experience if they can be recommended with good movies, and thus the website can maintain, and even expand its popularity. 

* Mission: Create an interactive web app that is based on movie contents to provide good movie suggestions to the web users
* Success Criteria: A subjective criteria, which is the user satisfaction on the suggested movies, will be applied to this web app. 

## Data
The raw data is from [Kaggle](https://www.kaggle.com/rounakbanik/the-movies-dataset/data). I used `Python 3` to do some EDA and clean the raw data (code in `EDA/EDA.py`). 

## Pivotal Tracker
[Link to Pivotal Tracker](https://www.pivotaltracker.com/n/projects/2144246)

## Software & Package requirements
Things you need to get it started:
* [conda](https://anaconda.org/): Either Anaconda or Miniconda is fine for this project.
* [git](https://git-scm.com/): You will most likely need version control.

## Set up the app
Below is a brief tutorial to set up the app in a AWS EC2 or Linux. For other systems, the general steps should be the same, but small changes might be needed. 

1. Update. Install git and conda if you have not done so.

    `sudo yum update`

    `sudo yum install git`

    `wget https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
    bash Anaconda3-5.1.0-Linux-x86_64.sh`

2. Clone this GitHub repository to local. Go into the directory, and use the `collegeapp.yml` file to create a conda environment with all required packages and dependecies.

    `conda env create -f collegeapp.yml`

    Then, activate the conda environment by entering `source activate collegeapp`.

3. In the same directory as `collegeapp.yml`, create a file called `config` and paste the following information into the file to configure AWS RDS access.

    `SECRET_KEY = 'development_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://collegeconnect:collegeahead@msiawebapp.cg96n7rbldvk.us-east-1.rds.amazonaws.com:5432/msiawebappdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = True`

4. `app/__init__.py` should have included the line of code: 

    `application.config.from_envvar('APP_SETTINGS', silent=True)`
    
    which tells the application to look at the environmental variable `APP_SETTINGS` for the path to your config file. 
    This means you simply need to set this environmental variable by entering:
    
    `export APP_SETTINGS="path/to/where/your/config/file/is.config`

5. The database has been initialized, so you may skip this step. If this is not the case, please initialize a folder called `data` in `develop` and store the cleaned data ([Google Drive](https://drive.google.com/file/d/1h84q5fhv1MEo6F0YYiqhdGLX854hRmNG/view?usp=sharing)) into this new folder. Then, you should enter `python create_collegedb.py` to initialize the database.

6. Now enter `python application.py`. The app should be running on `http://ec2-52-91-59-235.compute-1.amazonaws.com:5000/home`. Have fun!

## Logging
There are two sets of logging performed. 

1. `application.log` stores the logs of any user interaction with the EC2 application.

2. `createdb.log` stores the logs of database initialization.

## Unit Testing
We performed unit testing for `develop/modeling/model.py` file. The functions we tested are:
* `filter()`
* `modeling()`
* `major_pref_transformation()`
