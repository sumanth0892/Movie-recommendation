import os
import warnings 
warnings.filterwarnings('ignore')
import pandas as pd

def getData():
	ratingsFile = '/Users/computer/Documents/movieRecommender/rating.csv'
	moviesFile = '/Users/computer/Documents/movieRecommender/movie.csv'

	dfRatings = pd.read_csv(ratingsFile)
	dfMovies = pd.read_csv(moviesFile)

	df = pd.merge(dfRatings,dfMovies,on = 'movieId')
	return df 

	


