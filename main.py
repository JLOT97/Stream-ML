# Import the necessary libraries
from fastapi import FastAPI
import pandas as pd
import uvicorn
import ast
import sys



#  An instance of the FastAPI class is created. This instance ("app") will serve as the main entry point for the application.
app = FastAPI()



# The final dataset from the ETL process is loaded into a pandas DataFrame. The dataset is loaded from a csv file stored in the provided path. 
# 'dtype' parameter is used to specify the data type for 'column_name' column. 'low_memory' parameter is set to False to optimize memory usage
#  while reading large csv files.


# Read the CSV file containing the movie dataset and store it in a DataFrame with an url of google drive
url = 'https://drive.google.com/file/d/1MzTdMYoQmI15Pl2Eg2Mi3CGaKaGlh6gN/view?usp=sharing'

url='https://drive.google.com/uc?id=' + url.split('/')[-2]

df_combined = pd.read_csv(url) 

#df_combined = pd.read_csv('C:/Users/Asus/JLOT/Documents/StreamHub-ML-Orchestrator/data/movies_dataset_final.csv', dtype={'column_name': str}, low_memory=False)





#  1 - "GetFilmingCountByMonth" 

# Define an asynchronous endpoint with FastAPI's decorator '@app.get'. This will handle HTTP GET requests to the "/cantidad_filmaciones_mes/{mes}" URL where "{mes}" 
# is a path parameter that the user can specify.
@app.get("/cantidad_filmaciones_mes/{mes}")
async def cantidad_filmaciones_mes(mes: str):
    # The 'release_date' column is converted to datetime format for easier manipulation.
    df_combined['release_date'] = pd.to_datetime(df_combined['release_date'])
    
    # Check if the input month is a digit.
    if mes.isdigit():
        #  The input month is converted to an integer and the number of movies released in that month is calculated.
        mes_num = int(mes)
        cantidad = df_combined[df_combined['release_date'].dt.month == mes_num].shape[0]
    else:
        # EN: Convert the input month to lowercase and check if it's in the list of month names.
        mes = mes.lower()
        meses_nombres = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                         'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
        
        if mes in meses_nombres:
            # Find the index of the input month in the list of month names and calculate the number of movies released in that month.
            mes_num = meses_nombres.index(mes) + 1
            cantidad = df_combined[df_combined['release_date'].dt.month == mes_num].shape[0]
        else:
            # If the input month is neither a digit nor a valid month name, return an error message.
            return {"Error": "El mes ingresado no es válido"}

    # Return the number of movies filmed in the specified month.
    return {"mes": mes, "cantidad": cantidad}





# 2 - GetFilmingCountByDay" 

# Define an asynchronous endpoint with FastAPI's decorator '@app.get'. This will handle HTTP GET requests to the "/cantidad_filmaciones_dia/{dia}" URL where "{dia}" 
# is a path parameter that the user can specify.
@app.get("/cantidad_filmaciones_dia/{dia}")
async def cantidad_filmaciones_dia(dia: int):
    # The 'release_date' column is converted to datetime format for easier manipulation.
    df_combined['release_date'] = pd.to_datetime(df_combined['release_date'])

    # The number of movies released on the specified day of any month is calculated.
    cantidad = df_combined[df_combined['release_date'].dt.day == dia].shape[0]

    # EN: Return the number of movies filmed on the specified day.
    return {"dia": dia, "cantidad": cantidad}





# 3 - "GetFilmScoreByTitle" 

# Define an asynchronous endpoint with FastAPI's decorator '@app.get'. This will handle HTTP GET requests to the "/score_titulo/{titulo}" URL where "{titulo}" 
# is a path parameter that the user can specify.
@app.get("/score_titulo/{titulo}")
async def score_titulo(titulo: str):
    # The title input is converted to lowercase for better matching.
    titulo = titulo.lower()

    # Filter the dataframe for movies containing the input title in their title. The title of the dataframe is also converted to lowercase.
    peliculas = df_combined[df_combined['title'].str.lower().str.contains(titulo)]
    
    # Check if the filtered dataframe is empty, meaning no movies were found with the input title.
    if peliculas.empty:
        # If no movies were found, return an error message.
        return {"Error": "Película no encontrada"}
    else:
        # If movies were found, select the first one and extract the title, release year and popularity.
        pelicula = peliculas.iloc[0]
        retorno = {
            "titulo": str(pelicula['title']),
            "anio": str(pelicula['release_year']),
            "popularidad": str(pelicula['popularity'])
        }
        # Return the extracted information.
        return retorno





# 4 - "GetFilmVotesByTitle" 

# Define an asynchronous endpoint with FastAPI's decorator '@app.get'. This will handle HTTP GET requests to the "/votos_titulo/{titulo}" URL where "{titulo}"
# is a path parameter that the user can specify.
@app.get("/votos_titulo/{titulo}")
async def votos_titulo(titulo: str):
    # The title input is converted to lowercase for better matching.
    titulo = titulo.lower()

    # Filter the dataframe for movies that match exactly the input title in their title. The title of the dataframe is also converted to lowercase.
    peliculas = df_combined[df_combined['title'].str.lower() == titulo]
    
    # Check if the filtered dataframe is empty, meaning no movies were found with the input title.
    if peliculas.empty:
        # If no movies were found, return an error message.
        return {"Error": "Película no encontrada"}
    else:
        # If movies were found, select the first one and check if it has enough votes.
        pelicula = peliculas.iloc[0]
        if pelicula['vote_count'] < 2000:
            # If the movie doesn't have enough votes, return an error message.
            return {"Error": f"La película {titulo} no tiene suficientes votos"}
        else:
            # If the movie has enough votes, extract the title, release year, total votes and average votes.
            retorno = {
                "titulo": str(pelicula['title']),
                "anio": str(pelicula['release_year']),
                "voto_total": str(pelicula['vote_count']),
                "voto_promedio": str(pelicula['vote_average'])
            }
            # Return the extracted information.
            return retorno





# 5 - "GetActorInformation"   ---

# Define an asynchronous endpoint with FastAPI's decorator '@app.get'. This will handle HTTP GET requests to the "/get_actor/{actor}" URL where "{actor}" 
# is a path parameter that the user can specify.
@app.get("/get_actor/{actor}")
async def get_actor(actor: str):
    # Filter the dataframe for movies that contain the input actor in their cast. 'na=False' ignores NaN values.
    peliculas_actor = df_combined[df_combined['cast'].str.contains(actor, na=False)]
    
    # Check if the filtered dataframe is empty, meaning no movies were found with the input actor.
    if peliculas_actor.empty:
        # If no movies were found, return an error message.
        return {"Error": "Actor no encontrado"}
    else:
        # If movies were found, calculate the total return, the number of movies and the average return.
        retorno_total = peliculas_actor['return'].sum()
        cantidad_peliculas = peliculas_actor.shape[0]
        retorno_promedio = retorno_total / cantidad_peliculas if cantidad_peliculas > 0 else 0

        # Return the actor's name, total return, number of movies and average return.
        return {"actor": actor,"cantidad_filmaciones": cantidad_peliculas,"retorno_total": retorno_total, "retorno_promedio": retorno_promedio}





# 6 - "GetDirectorInformation" 

# Define an asynchronous endpoint with FastAPI's decorator '@app.get'. This will handle HTTP GET requests to the "/get_director/{director}" URL where "{director}"
#  is a path parameter that the user can specify.
@app.get("/get_director/{director}")
async def get_director(director: str):
    # Filter the dataframe for movies that contain the input director in their crew. 'na=False' ignores NaN values.
    peliculas_director = df_combined[df_combined['crew'].str.contains(director, na=False)]
    
    # Check if the filtered dataframe is empty, meaning no movies were found with the input director.
    if peliculas_director.empty:
        # If no movies were found, return an error message.
        return {"Error": "Director no encontrado"}
    else:
        # If movies were found, create a list of dictionaries, each containing the details of a movie.
        resultados = []
        for _, pelicula in peliculas_director.iterrows():
            resultados.append({
                "titulo": str(pelicula['title']),
                "anio": str(pelicula['release_year']),
                "retorno_pelicula": str(pelicula['return']),
                "budget_pelicula": str(pelicula['budget']),
                "revenue_pelicula": str(pelicula['revenue'])
            })
        
        # Calculate the total return of the director's movies.
        retorno_total = peliculas_director['return'].sum()

        # Return the director's name, total return, and the list of movie details.
        return {
            "director": director,
            "retorno_total_director": str(retorno_total),
            "peliculas": resultados
            }
    





#-----------------------------------------------------------------------------------------------

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

 
# Data Cleaning: Replace NaN values with empty strings
df_combined['genres'] = df_combined['genres'].fillna('')

# Create a new feature that combines genre and vote average
df_combined['features'] = df_combined['genres'].astype(str) + ' ' + df_combined['vote_average'].astype(str)

# Create a TF-IDF matrix for the combined features
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df_combined['features'])

# Define the recommendation function
def recomendacion(titulo):
    # Convert the title to lowercase
    titulo = titulo.lower()

    # Filter movies by the selected title
    pelicula_seleccionada = df_combined[df_combined['title'].str.lower() == titulo]

    if pelicula_seleccionada.empty:
        return []

    # Get the index of the selected movie
    index = pelicula_seleccionada.index[0]

    # Calculate similarity between movies based on the combined features
    similarity_scores = cosine_similarity(tfidf_matrix[index], tfidf_matrix)

    # Obtener los índices de las películas más similares
    similar_movies_indices = similarity_scores.argsort()[0][-5:][::-1]

    # Get the titles and similarity scores of the most similar movies
    peliculas_similares = df_combined.iloc[similar_movies_indices][['title', 'vote_average']].values.tolist()

    # Sort the movies by similarity score from highest to lowest
    peliculas_similares = sorted(peliculas_similares, key=lambda x: x[1], reverse=True)

    # Add additional movies to the list if needed
    while len(peliculas_similares) < 5:
        peliculas_similares.append(['Película adicional', 0])

    return peliculas_similares



# Define an asynchronous endpoint with FastAPI's decorator '@app.get'. This will handle HTTP GET requests to the "/recomendacion/{titulo}" URL where "{titulo}" 
# is a path parameter that the user can specify.
@app.get("/recomendacion/{titulo}")
async def obtener_recomendacion(titulo: str):
    # Call the 'recomendacion' function to get the recommended movies based on the specified title.
    recomendaciones = recomendacion(titulo)

    # Check if there are no recommended movies for the specified title.
    if len(recomendaciones) == 0:
        # Return an error message if no movies are found.
        return {"Error": "Película no encontrada"}
    else:
        # Return the list of recommended movies.
        return {"lista_recomendada": recomendaciones}



 

# This line checks if this script is being run directly (as opposed to being imported as a module in another script). 
if __name__ == "__main__":
    # If the script is being run directly, it uses the 'uvicorn' ASGI server to serve the FastAPI application. It runs on the local machine (host="0.0.0.0") on port 8000.
    # 'reload=True' enables hot reloading, which means the server will automatically update whenever a change is made to the script.
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



# http://127.0.0.1:8000/docs#/