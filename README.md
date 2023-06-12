# Stream-ML

# 🎬 Stream-ML Your Movie Recommendation System 🍿

![Project Image](your_image_link)

 Stream-ML is a robust and user-friendly movie recommendation system, designed to help you find your next favorite movie. Based on a dataset of thousands of movies, our system learns from data patterns and similarities between movies to provide the most accurate recommendations. Just enter the title of a movie you like and let  Stream-ML do the rest!

## 📋 Index
1. [Data Cleaning and Preparation Process](#cleaning)
2. [Exploratory Data Analysis](#eda)
3. [Recommendation Model](#model)
4. [Installation](#installation)
5. [How to Use](#use)
6. [Usage Example](#example)
7. [Dependencies](#dependencies)
8. [License](#license)

## 🧹 1. Data Cleaning and Preparation Process <a name="cleaning"></a>

The first step in our project is data cleaning and preparation. In this step, we normalize and clean our dataset for further analysis and modeling. [See more](src/etl.ipynb)

## 📊 2. Exploratory Data Analysis (EDA) <a name="eda"></a>

Once the data is clean and prepared, we perform an EDA to uncover patterns, trends, and relationships in the data. [See more](src/eda.ipynb)

## 🎯 3. Recommendation Model <a name="model"></a>

We use the analysis of the data to build our recommendation system, which provides movie suggestions based on a movie title specified by the user. [See more](main.py)

## 🚀 4. Installation <a name="installation"></a>

No installation is required as the project is deployed on a web server. Users can interact with the API directly from their browser.

## 💡 5. How to Use <a name="use"></a>

Users can interact with the API by visiting the server in their browser and providing a movie title. The API will return a list of recommended movies based on the provided title.

## 📖 6. Usage Example <a name="example"></a>

To get movie recommendations, visit the server in your browser and provide a movie title. The API will return a list of recommended movies.

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
