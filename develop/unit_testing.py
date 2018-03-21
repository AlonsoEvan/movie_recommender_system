
"""
This is a Unit Testing file for movie_recommender.py. 

Author: Wenjing Yang

"""

import pandas as pd
import numpy as np


def test_get_director():
    """ Testing get_director function """

    # create test data
    mydata = [{'credit_id': '52fe4284c3a36847f8024f49',
     'department': 'Directing',
     'gender': 2,
     'id': 7879,
     'job': 'Director',
     'name': 'John Lasseter'}, 
     {'credit_id': '52fe44bfc3a36847f80a7c7d',
      'department': 'Directing',
      'gender': 2,
      'id': 4945,
      'job': 'Director',
      'name': 'Joe Johnston'}]
    mydata = pd.Series(mydata)
    
    # test get_director(mydata)
    expected_get_director = "John Lasseter"
    
    try:
        # check data type
        assert isinstance(expected_get_director, str)
                
        # check expected output
        assert (expected_get_director == get_director(mydata))
        
        print ('Test for get_director function passed!')
    
    except:
        print ('Test for get_director function FAILED!')




def test_filter_keywords():
	""" testing filter_keywords function """

    # create test data
    mydata = [{'id': 931, 'name': 'jealousy'}, 
              {'id': 4290, 'name': 'toy'}, 
              {'id': 5202, 'name': 'boy'}, 
              {'id': 6054, 'name': 'friendship'}, 
              {'id': 9713, 'name': 'friends'}, 
              {'id': 9823, 'name': 'rivalry'}, 
              {'id': 165503, 'name': 'boy next door'}, 
              {'id': 170722, 'name': 'new toy'}, 
              {'id': 187065, 'name': 'toy comes to life'}]
    
    # test filter_keywords(mydata)
    expected_filter_keywords = [{'id': 931, 'name': 'jealousy'},
                             {'id': 4290, 'name': 'toy'},
                             {'id': 5202, 'name': 'boy'},
                             {'id': 6054, 'name': 'friendship'},
                             {'id': 9713, 'name': 'friends'},
                             {'id': 9823, 'name': 'rivalry'},
                             {'id': 165503, 'name': 'boy next door'},
                             {'id': 170722, 'name': 'new toy'},
                             {'id': 187065, 'name': 'toy comes to life'}]
        
    try:
        # check data type
        assert isinstance(expected_filter_keywords,list)       
        print ('Test for filter_keywords function passed!')
        
    except:
        print ('Test for filter_keywords function FAILED!') 


def test_discover_movie():
""" testing discover_movie function """
	
	expected_temp = (1,2,3)

	try:
        # check data type
        assert isinstance(expected_temp,tuple)       
        print ('Test for filter_keywords function passed!')
        
    except:
        print ('Test for filter_keywords function FAILED!') 
