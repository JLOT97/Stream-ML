** ETL Process Documentation **



Overview


This file describes the Extraction, Transformation, and Loading (ETL) process performed on a movie dataset. The objective of this process
is to prepare the data for further analysis and use in a recommendation model.


1. Loading and Viewing the Data: 

      In this step, the necessary libraries for data analysis and manipulation are imported. The CSV file 
      containing the movie data is read into a DataFrame from a Google Drive URL using the pandas library. 
      A preview of the first 5 records and general information about the DataFrame is displayed.


2. Unnesting the 'belongs_to_collection' Column: 

      In this step, the 'belongs_to_collection' column is converted from a string format to a
      dictionary format using the parse_col function. Then, the 'belongs_to_collection' column is unnested into 
      separate fields using the pd.concat function.


3. Treatment of Null Values: 

   In this step, null values in the 'revenue' and 'budget' columns are filled with zeros using the fillna function. 
   Rows with null values in the 'release_date' column are dropped using the dropna function.


4. Formatting Dates and Extracting Release Year:

   In this step, dates are formatted into the YYYY-mm-dd format using the pd.to_datetime function, and the release year 
   is extracted from the 'release_date' column. The result is stored in a new column called 'release_year'.


5. Converting Non-Numeric Values to Zeros and Calculating Return on Investment: 

   In this step, non-numeric values in the 'budget' column are converted to zeros using the pd.to_numeric function, and 
   null values in the 'return' column are filled with zeros. Then, the return on investment is calculated by dividing the revenue 
   by the budget.


6. Extracting Specific Values from Dictionary Columns:

   In this step, the convert_to_dict function is defined to convert string values to dictionaries. This function is applied
   to the specified columns ('genres', 'production_companies', 'production_countries', 'spoken_languages') using the extract_values
   function. A new DataFrame called df_movies_aux is created with the extracted values.


7. Unnesting and Merging Relevant Columns:

   In this step, relevant columns ('genres', 'production_companies', 'production_countries', 'spoken_languages') are unnested
   into separate fields using the extract_values function. The extracted values are added to the df_movies_aux DataFrame. 
   Then, the df_movies_copy DataFrame is merged with df_movies_aux using the 'id' column as the merge key.


8. Creating a Backup of the Original DataFrame:

   In this step, a backup copy of the original DataFrame called df_movies_copy is created to prevent data loss during the cleaning 
   and transformation process.


9. Removing Unnecessary Columns:

   In this step, unnecessary columns are dropped from the df_movies_copy DataFrame using the drop function. 
   The 'genres', 'production_companies', 'production_countries', 'spoken_languages', 'belongs_to_collection_id',
   'belongs_to_collection_poster_path', 'belongs_to_collection_backdrop_path', 'video', 'imdb_id', 'adult', 'original_title',
   'poster_path', and 'homepage' columns are removed.


 10. Removing Duplicates in the 'df_movies_copy' DataFrame:

   In this step, duplicates in the 'id' column of the df_movies_copy DataFrame are removed using the drop_duplicates function. 
   The number of duplicates before and after removal is checked.


11. Joining 'df_movies_copy' with 'df_movies_aux':

   In this step, the data type of the 'id' column in the df_movies DataFrame is checked. Then, the 'id' column is converted to
   integers in both the df_movies_copy and df_movies_aux DataFrames. Duplicates in the df_movies_aux DataFrame are removed, 
   and the DataFrames df_movies_copy and df_movies_aux are merged on the 'id' column.


12. Working with 'credits.csv':

   In this step, the 'credits.csv' file is read into the df_credits DataFrame. Duplicates in the 'id' column are checked and removed
   using the drop_duplicates function.


13 Transformation and Extraction of Data in the 'crew' and 'cast' Columns:

   In this step, the character strings in the 'crew' and 'cast' columns are converted to lists of dictionaries using the ast.literal_eval function. 
   The names of directors are extracted from the 'crew' column, and the names of actors are extracted from the 'cast' column.


14. Merging the Movies and Credits DataFrames:

   In this step, the df_movies_combined and df_credits DataFrames are merged using the 'id' column as the merge key. The resulting
   DataFrame is stored in df_combined.


15. Exporting the Final DataFrame to CSV:

   In this step, the final DataFrame df_combined is exported to a CSV file named 'movies_dataset_final2.csv' without including the indices.

