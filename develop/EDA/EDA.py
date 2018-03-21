#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 18:39:43 2018

@author: wenjingyang
"""
import pandas as pd

# read in the table of movie information 
movie = pd.read_csv("/Users/wenjingyang/Documents/Winter 2018/MSiA423 - Analytics Value Chain/msia423_webapp/data/movies_metadata.csv")
movie.head(10)

# check NAs in all columns
movie.isnull().sum() 
movie['id'].isnull().sum()
movie['title'].isnull().sum()
movie['genres'].isnull().sum()
# --> id column has no NA
# --> title column has 6 NAs
# --> genre column has no NA

# check the 6 rows of NA in titles
movie['title'].head(20)
movie[movie['title'].isnull()][['id']]
 
# --> something strange happens to the id column

# i have to check the format of the id column again
movie['id'].head(1000)

# i found a method to check the abnormality in the id column. 
# Use the function pd.to_numeric() to check if there are only 3 rows with strange id

pd.to_numeric(movie['id']) # error message: Unable to parse string "1997-08-20" at position 19730

# remove this row
movie = movie.drop(movie.index[19730])

# repeat the process until no error shows up
pd.to_numeric(movie['id'])
# remove this row
movie = movie.drop(movie.index[29502])
pd.to_numeric(movie['id'])
movie = movie.drop(movie.index[35585])
pd.to_numeric(movie['id']) # no error message --> id column is fixed 

# continue checking NAs in titles
movie[movie['title'].isnull()][['id']]

# drop the rows with NA in titles
movie = movie[movie.title.notnull()]
movie[movie['title'].isnull()][['id']]

# check the data type 
movie['title']
movie['id'] = pd.to_numeric(movie['id'])
movie['id']
movie['genres'] # let's deal with this column later 

# read in the table of ratings
rating = pd.read_csv("/Users/wenjingyang/Documents/Winter 2018/MSiA423 - Analytics Value Chain/msia423_webapp/data/ratings.csv")

# check NAs in columns
rating.isnull().sum() #--> no NAs

# check data types
rating['userId']
rating['movieId']
rating['rating']


import numpy as np
import matplotlib.pyplot as plt

# plot the rating
plt.hist(rating['rating'])

# calculate the number of movie ratings for users
movie_1_user = rating.groupby('userId',as_index=False).agg({'movieId':[np.size]})
movie_1_user.columns = ['userId','movie_sum']
movie_1_user.head(10)
#plt.bar(movie_1_user['userId'], movie_1_user['movie_sum'])
#plt.show()

#plt.bar(movie_1_user['userId'], movie_1_user['movie_sum'])


# calculate the avg rating of each person --> detect the personalized factor (which we can use as weight in the following calculations)
user_avg_rating = rating.groupby('userId').agg({'rating':[np.sum]})
user_avg_rating.columns = ['rating_sum']
user_avg_rating = user_avg_rating['rating_sum']/movie_1_user['movie_sum']
user_avg_rating.columns = ['rating_avg']
user_avg_rating.head(10)

# find the top10 most rated movies (the times of being rated)
rating_1_movie = rating.groupby('movieId').agg({'rating':[np.size]})
rating_1_movie.columns = ['rating_times']
rating_1_movie.sort_values(by='rating_times',ascending=False).head(10)

# find the top10 highest rated movies (movies with highest average ratings)
movie_avg_rating = rating.groupby('movieId').agg({'rating':[np.sum]})
movie_avg_rating.head(10)
movie_avg_rating.columns = ['rating_sum'] 
movie_avg_rating = movie_avg_rating['rating_sum']/rating_1_movie['rating_times']
movie_avg_rating.columns = ['avg_rating']


rating_1_movie.sort_values(by='rating_times',ascending=False).head(10)

movie_avg_rating



# Next time, we need to merge the movie table and rating table together to have a better
# idea of the distributions of each movie titles. Then, with the information collected this week
# and other knowledge about recommender systems i will learn next week, i should build the initial
# recommender model for the data on my local machine.








