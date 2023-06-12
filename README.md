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

The *Stream-ML* API offers various endpoints that provide unique functionalities for movie data exploration and recommendation generation. Here we describe each one:

    1. `GetFilmingCountByMonth`: This endpoint allows you to find out the number of filmings made in a particular month. You just need to indicate the name of the month or its corresponding number. To use this endpoint, visit: [here](https://stream-ml-jlot.onrender.com/cantidad_filmaciones_mes/{month})

    2. `GetFilmingCountByDay`: Similar to the previous one, this endpoint returns the number of filmings made on a particular day of any month. You just need to provide the day in numeric format. To use this endpoint, visit: [here](https://stream-ml-jlot.onrender.com/cantidad_filmaciones_dia/{day})

    3. `GetFilmScoreByTitle`: Allows you to know the popularity score of a movie based on its title. You just need to provide the movie title. To use this endpoint, visit: [here](https://stream-ml-jlot.onrender.com/score_titulo/{title})

    4. `GetFilmVotesByTitle`: This endpoint provides information about the votes of a movie given its title, including the total number of votes and the average votes. To use this endpoint, visit: [here](https://stream-ml-jlot.onrender.com/votos_titulo/{title})

    5. `GetActorInformation`: Allows you to get information about a particular actor, such as the number of filmings they have participated in, the total return and the average return of their films. You just need to provide the actor's name. To use this endpoint, visit: [here](https://stream-ml-jlot.onrender.com/get_actor/{actor})

    6. `GetDirectorInformation`: This endpoint provides information about a particular director, such as the total return of their films and a list of their films with details such as the title, the release year, the return, the budget, and the revenue of each film. You just need to provide the director's name. To use this endpoint, visit: [here](https://stream-ml-jlot.onrender.com/get_director/{director})

    7. `obtener_recomendacion`: This is the main recommendation endpoint that provides you with a list of recommended films based on the title of a film. To use this endpoint, visit: [here](https://stream-ml-jlot.onrender.com/recomendacion/{title})

    Please replace `{month}`, `{day}`, `{title}`, `{actor}`, `{director}` with the values you want to search for.



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
