# Disaster-Response-Pipelines

### Table of Contents

1. [Description](#Description)
2. [File Descriptions](#files)
3. [Installation/Instructions](#installation)
4. [Acknowledgements](#Acknowledgements)

## Description
Disaster Response Pipelines

This is part of Udacity's Data Scientist Nanodegree program. In this project, disaster data from [Figure Eight](https://www.figure-eight.com/) has been analyzed to build a model for an API that classifies disaster messages.

In the data folder, you'll find a data set containing real messages that were sent during disaster events. Machine learning pipeline has been created to categorize these events so that the messages can be sent to an appropriate disaster relief agency.

This project includes a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data.

## File Descriptions <a name="files"></a>

Folder: data

disaster_messages.csv - real messages sent during disaster events provided by Figure Eight.

disaster_categories.csv - the categories of the messages.

process_data.py - to load raw messages, clean the messages and save the messages as inputs for Machine Learning model.

testing.db - a saved cleaned dataset.

ETL Pipeline Preparation.ipynb - notebook file in preparation for process_data.py (html is also provided).


Folder: models

train_classifier.py - to load cleaned data, build ML model, train and test the model, and save the model for web application.

haha.pkl - a saved model for web application.

ML Pipeline Preparation.ipynb - notebook file in preparation for train_classifier.py (html is also provided).

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

## Acknowledgements<a name="Acknowledgements"></a>

[Figure Eight](https://www.figure-eight.com/) for providing real messages sent during disaster events.

[Udacity](https://www.udacity.com/) for excellent learning experience!


