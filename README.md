# Disaster-Response-Pipelines
Disaster Response Pipelines

This is part of Udacity's Data Scientist Nanodegree program. In this project, disaster data from [Figure Eight](https://www.figure-eight.com/) has been analyzed to build a model for an API that classifies disaster messages.

In the data folder, you'll find a data set containing real messages that were sent during disaster events. Machine learning pipeline has been created to categorize these events so that the messages can be sent to an appropriate disaster relief agency.

This project includes a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data.

### Table of Contents

1. [Installation/Instructions](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation/Instructions <a name="installation"></a>

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python.  The code should run with no issues using Python versions 3.*.

Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

## Project Motivation<a name="motivation"></a>

In this project, I was originally interestested in identifying the best technical indicators to predict stock price movement, either up or down using pre-calculated technical indicator based on historical stock data. In the attempts to achieve this, I have realized that the accuracy obtained is not as high as I had hoped for. Therefore, this project then aims to

1. Compare the accuracy of prediction using SVW, SVM with PCA, and Neural Networks.
2. What are the most weighted indicators in the top PCA components?
3. Based on this data, can we visualize the data to see if we can really separate the two classes, price up or down?


## File Descriptions <a name="files"></a>

The notebook showing step by step from data cleaning to the three models is available here.

## Results<a name="results"></a>

The main findings of the code can be found at the post available [here](https://medium.com/@amaluddin11/best-indicators-for-day-traders-e029d526f336).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

The Copyright and License information for the data can be referred at [Elsevier Data in Brief](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5219605/) where the data was originally published. Otherwise, feel free to use the code here as you would like!


