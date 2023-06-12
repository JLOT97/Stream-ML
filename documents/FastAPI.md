** FastAPI Process Description **

This file outlines the process of creating a web API using FastAPI, which serves data from a CSV file containing information on movies. FastAPI is a modern, fast 
(high-performance) web framework that is designed to be easy to use, quick to code, with fewer bugs, and with impressive performance.



1. Library Import: The necessary libraries are imported, including FastAPI, pandas, uvicorn, ast, and sys.


2. FastAPI Instance: An instance of the FastAPI class is created, which will serve as the main entry point for the application.


3. CSV File Loading: The final CSV file from the ETL process is loaded into a pandas DataFrame. This file is stored on Google Drive and is accessed via a URL.


4. Endpoint Creation: Several endpoints are created in FastAPI to serve the data from the pandas DataFrame. Each endpoint represents a different route in the API and 
   serves a different function.


   a. GetFilmingCountByMonth: This endpoint receives a month parameter (either a number or a month name) and returns the number of filmings conducted in that month.
   
   b. GetFilmingCountByDay: This endpoint receives a day parameter (a number) and returns the number of filmings conducted on that day of the month.
   
   c. GetFilmScoreByTitle: This endpoint receives a movie title parameter and returns the title, release year, and popularity of the movie.
   
   d. GetFilmVotesByTitle: This endpoint receives a movie title parameter and returns the title, release year, total votes, and average vote of the movie.
   
   e. GetActorInformation: This endpoint receives an actor name parameter and returns the actor's name, the number of filmings he has participated in, the total 
      return, and the average return of his films.
   
   f. GetDirectorInformation: This endpoint receives a director name parameter and returns the director's name, the total return of his films, and a list of details 
      of the movies he has directed.

Each endpoint uses the HTTP GET method to receive requests, and the request parameters are passed as part of the URL.


5. Error Handling: Each endpoint checks whether the input parameters are valid and whether the requested data exists. If not, an appropriate error message is returned.


6. FastAPI Execution: This script is running directly (instead of being imported as a module in another script), it uses the ASGI server 'uvicorn' to serve the 
   FastAPI application. It is running on the local machine (host="0.0.0.0.0") on port 8000. 'reload=True' enables hot reloading, which means that the server will 
   be automatically updated every time a change is made to the script.
