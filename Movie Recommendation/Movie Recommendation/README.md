Project Title: Content-Based Movie Recommender System

Technology Stacks Used:

Python
Flask
NumPy
Pandas
scikit-learn (sklearn)
Beautiful Soup (bs4)
urllib
pickle
requests
Project Description:
The Content-Based Movie Recommender System is a web application that provides movie recommendations based on user preferences and performs sentiment analysis on user reviews. The system utilizes machine learning algorithms and web scraping techniques to gather movie data and analyze user sentiments.

The project consists of the following key components:

Data Processing:

The application imports necessary Python libraries, including NumPy and Pandas, for data manipulation and analysis.
The Flask framework is used to build the web application.
The project also utilizes scikit-learn (sklearn) for natural language processing (NLP) tasks, such as feature extraction and cosine similarity calculations.
Beautiful Soup (bs4) and urllib are employed for web scraping IMDb reviews and extracting movie details from Wikipedia.
Recommender System:

The system employs a content-based approach to recommend movies similar to the user's preferred movie.
A CountVectorizer is used to transform the movie data into a count matrix, and cosine similarity is calculated to determine the similarity between movies.
The recommender function suggests a list of similar movies based on the user's input.
Sentiment Analysis:

User reviews from IMDb are scraped using web scraping techniques with Beautiful Soup.
The reviews are then processed and analyzed using a pre-trained sentiment analysis model.
The sentiment analysis model, implemented with scikit-learn's Multinomial Naive Bayes classifier, predicts whether a review is positive or negative based on the text data.
Web Application:

The Flask API handles the routing and interaction with the user.
The user interface (UI) is designed using HTML templates and CSS, although the provided design is a basic template.
The application provides endpoints for user interactions, including retrieving movie suggestions, obtaining movie recommendations, and displaying movie details along with user reviews and cast information.
Importance of the Project:
The Content-Based Movie Recommender System is significant for several reasons:

It improves user experience by providing personalized movie recommendations based on their preferences.
The sentiment analysis feature allows users to gain insights into the overall sentiment around a movie based on IMDb reviews.
The project demonstrates the integration of multiple technologies, including machine learning, web scraping, and web development, to create a functional and interactive application.
By leveraging data from external sources like IMDb and Wikipedia, the system enriches the movie information available to users.
Note: The HTML design and CSS in the project are stated to be basic templates, as the developer had limited experience in web development and software development.