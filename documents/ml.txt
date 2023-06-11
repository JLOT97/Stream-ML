** Description of Recommendation Model and its Endpoint **




This file describes the process of building a recommendation model and its corresponding endpoint using FastAPI. 
The goal of this model is to provide recommendations for similar movies based on the title of a selected movie.



1. Import the necessary libraries:

    1.1. sklearn.metrics.pairwise.cosine_similarity: This library provides functions for calculating cosine similarity between vectors.
    1.2. sklearn.feature_extraction.text.TfidfVectorizer: This library is used to convert text into a TF-IDF matrix.



2. Data Cleaning:

    2.1. Replace NaN values in the 'genres' column with empty strings.



3. Create a new feature:

    3.1. The 'features' column is created by combining the 'genres' and 'vote_average' columns.



4. Create a TF-IDF matrix:

    4.1. The TfidfVectorizer is used to create a TF-IDF matrix from the combined features.



5.Define the recommendation function:

    5.1. The recommendation function takes a title as input and returns a list of recommended movies based on that title.
    Convert the title to lowercase.

    5.2. Filter movies by the selected title.

    5.3. Calculate similarity between movies based on the combined features using cosine similarity.
    
    5.4. Get the indices of the most similar movies.
    
    5.5. Sort the movies by similarity score from highest to lowest.
    
    5.6. Complete the list with additional movies if necessary.



6. Define the endpoint:

    6.1. An asynchronous endpoint is defined using FastAPI's '@app.get' decorator to handle HTTP GET requests to the "/recomendacion/{titulo}" URL, where "{titulo}" is 
         a path parameter specified by the user.

    6.2. Call the 'recomendacion' function to get the recommended movies based on the specified title.

    6.3. Check if there are no recommended movies for the specified title and return an error message in that case.
    
    6.4. Return the list of recommended movies.



7. Project Objective and Importance


The objective of this project is to develop a content-based movie recommendation system using natural language processing techniques and similarity algorithms. 
The model aims to provide personalized recommendations to users based on movie characteristics such as genre and vote ratings.

The importance of this project lies in enhancing the user experience by suggesting movies that align with their individual preferences. This can help users discover
new movies and broaden their cinematic knowledge. Furthermore, the content-based approach enables precise and relevant recommendations, even for new users without a
 prior interaction history.