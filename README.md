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
The raw data is from [Kaggle](https://www.kaggle.com/rounakbanik/the-movies-dataset/data). I used `Python 3` to do some EDA and clean the raw data (code in `develop/EDA.ipynb`). 

## Pivotal Tracker
[Link to Pivotal Tracker](https://www.pivotaltracker.com/n/projects/2144246)

## Software & Package requirements
Things you need to get it started:
* [conda](https://anaconda.org/): Either Anaconda or Miniconda is fine for this project.
* [git](https://git-scm.com/): You will most likely need version control.

## Website link
[Link to the web app](http://final-deploy-dev.us-west-2.elasticbeanstalk.com/)


## Logging
There are two sets of logging performed. 
1. `application.log` stores the logs of any user interaction with the Beanstalk application.


## Unit Testing
We performed unit testing for `develop/modeling/model.py` file. The functions we tested are:
* `get_director()`
* `filter_keywords()`
* `discover_movie()`
