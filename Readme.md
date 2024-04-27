# Movie Recommender System (Content-Based Filtering)

## Overview

This Movie Recommender System is based on content-based filtering, utilizing a dataset obtained from Kaggle. The system suggests movie recommendations to users based on the content and features of movies they have liked or selected.

## Data Collection

The movie dataset used in this project was sourced from Kaggle. The dataset contains information about various movies, including titles, genres, and other relevant features. The dataset was obtained from the following Kaggle URL: [Kaggle Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

## Data Preprocessing

Before building the recommender system, a series of preprocessing steps were performed on the dataset. This includes cleaning the data, handling missing values, and combining multiple datasets if necessary. Weights were assigned to features to capture the relevance of each attribute in the recommendation process.

## Implementation

The recommender system employs content-based filtering, which recommends movies similar to those a user has liked. The similarity between movies is calculated based on specific features, such as genre, actors, and other relevant attributes. This ensures that recommendations are tailored to the user's preferences.

## Front-End Interface

To enhance user experience, a user-friendly front-end interface was created using Streamlit. Users can select their preferred movie from the provided list, and upon clicking the recommendation button, the system suggests a curated list of movies based on their selection.
and deployed it.

## How to Run

1. Clone the repository to your local machine.
2. Install the required dependencies by running: `pip install -r requirements.txt`.
3. Run the Streamlit app with the command: `streamlit run app.py`.
4. Access the recommender system through the provided web interface.

## File Structure

- `app.py`: Contains the Streamlit app code for the front-end.
- `movies.pkl`: Pickled file containing the preprocessed movie dataset.
- `similarity.pkl`: Pickled file containing the calculated similarity matrix.

## Acknowledgments

- Kaggle for providing the movie dataset.
- Streamlit for simplifying the creation of the user interface.
- The open-source community for valuable resources and inspiration.

Feel free to explore and contribute to further enhancements of this Movie Recommender System. 
Enjoy discovering new movies tailored to your preferences!
