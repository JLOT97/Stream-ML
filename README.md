# 🎬 Stream-ML Your Movie Recommendation System 🍿

![Project Image](your_image_link)

 *Stream-ML* is a robust and user-friendly movie recommendation system, designed to help you find your next favorite movie. Based on a dataset of thousands of movies, our system learns from data patterns and similarities between movies to provide the most accurate recommendations. Just enter the title of a movie you like and let  *Stream-ML* do the rest!

## 📋 Index
1. [Data Cleaning and Preparation Process](#cleaning)
2. [Exploratory Data Analysis](#eda)
3. [Recommendation Model](#model)
4. [How to Use](#use)
6. [Usage Example](#example)
7. [API Endpoints](#endpoints)
8. [Dependencies](#dependencies)
8. [License](#license)

## 🧹 1. Data Cleaning and Preparation Process <a name="cleaning"></a>

The first step in our project is data cleaning and preparation. In this step, we normalize and clean our dataset for further analysis and modeling. [See more](src/etl.ipynb)

## 📊 2. Exploratory Data Analysis (EDA) <a name="eda"></a>

Once the data is clean and prepared, we perform an EDA to uncover patterns, trends, and relationships in the data. [See more](src/eda.ipynb)

## 🎯 3. Recommendation Model <a name="model"></a>

We use the analysis of the data to build our recommendation system, which provides movie suggestions based on a movie title specified by the user. [See more](main.py)

## 💡 4. How to Use <a name="use"></a>

Users can interact with the API by visiting the server in their browser and providing a movie title. The API will return a list of recommended movies based on the provided title.

## 📖 5. Usage Example <a name="example"></a>

To get movie recommendations, visit the server in your browser and provide a movie title. The API will return a list of recommended movies.

## 📚 6. API Endpoints <a name="endpoints"></a>

The *MovieMate* API offers various endpoints that provide unique functionalities for movie data exploration and recommendation generation. Here we describe each of them:

1. [`GetFilmingCountByMonth`](https://stream-ml-jlot.onrender.com/docs): This endpoint allows you to find out the number of filmings made in a particular month. You just need to indicate the name of the month (in Spanish) or its corresponding number. To use this endpoint, simply click on the endpoint name.

2. [`GetFilmingCountByDay`](https://stream-ml-jlot.onrender.com/docs): Similar to the previous one, this endpoint returns the number of filmings made on a specific day of any month. You only need to provide the day in numeric format. To use this endpoint, simply click on the endpoint name.

3. [`GetFilmScoreByTitle`](https://stream-ml-jlot.onrender.com/docs): It allows you to know the popularity score of a movie based on its title. You just need to provide the movie title. To use this endpoint, simply click on the endpoint name.

4. [`GetFilmVotesByTitle`](https://stream-ml-jlot.onrender.com/docs): This endpoint provides information about the votes for a movie given its title, including the total number of votes and the average vote. To use this endpoint, simply click on the endpoint name.

5. [`GetActorInformation`](https://stream-ml-jlot.onrender.com/docs): It allows you to retrieve information about a specific actor, such as the number of films they have participated in, the total return, and the average return of their movies. You just need to provide the actor's name. To use this endpoint, simply click on the endpoint name.

6. [`GetDirectorInformation`](https://stream-ml-jlot.onrender.com/docs): This endpoint provides information about a specific director, such as the total return of their movies and a list of their movies with details such as title, release year, return, budget, and revenue. You just need to provide the director's name. To use this endpoint, simply click on the endpoint name.

7. [`get_recommendation`](https://stream-ml-jlot.onrender.com/docs): This is the main recommendation endpoint that provides a list of recommended movies based on a movie title. To use this endpoint, simply click on the endpoint name.



*please click on the endpoint titles and it will redirect you to the server and also replace `{mes}`, `{dia}`, `{titulo}`, `{actor}`, `{director}` with the values you want to search for.*



## ⚙️ 7. Dependencies <a name="dependencies"></a>

The project depends on the following libraries:
- pandas
- numpy
- seaborn
- matplotlib
- sklearn
- FastAPI
- Uvicorn
- missingno
- sweetviz
- wordcloud

## 📄 8. License <a name="license"></a>

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 2, June 1991.
