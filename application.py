
"""
This is the flask application page for the movie recommender system.

Author: Wenjing Yang

"""

from flask import Flask, render_template, request, session, g, redirect, url_for, abort, \
     render_template, flash
import os
from movie_recommender import discover_movie
import logging


# Elastic Beanstalk initalization
application = Flask(__name__)
application.config.from_object(__name__) # Load config

# read in the data
output = discover_movie()

# claim variables
indices = output[0]
cosine_sim = output[1]
titles = output[2]

# userinput function
def get_recommendations(title):
    """The main function to get movie recommendations based on userinput

    Args:
        param1 (String): user input (movie title)

    Returns:
        list (list dataframe): a list of 10 suggested movies

    """
    try:
        index = indices[title]
        sim_scores = list(enumerate(cosine_sim[index]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:31]
        movie_indices = [i[0] for i in sim_scores]
        tmp = titles.iloc[movie_indices].head(10)
        return tmp.tolist()
    except:
        return 0

def printresult(movie):
    for i in range (0,10):
        print(movie[i])
        print("")


# first page
@application.route('/', methods=['GET'])
def mainpage():
    """Home page of the webapp
    
    Args:
        Null
    
    Returns:
        flask-obj: rendered html page
        
    """
    return render_template('page1.html')
 

# show the model
@application.route('/',methods=['POST'])
def printmovie():
    """Recommendation page of webapp
    
    Args:
        Null
    
    Returns:
        flask-obj: rendered html page
    """
    title = request.form['userinput']
    recom = get_recommendations(title)
    if recom != 0:
        return render_template('page2.html', result=recom)
    
    return render_template('page2.html', result="Sorry")


if __name__ == "__main__":
    #logging.basicConfig(filename='application.log', level=logging.DEBUG)
    #logger = logging.getLogger(__name__) 
    application.run()




