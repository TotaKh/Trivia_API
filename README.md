# Full Stack Trivia API Project

## Introduction

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game. 

The main features of the application are:
1) Display questions it's shows the question, category and difficulty rating by default and can show/hide the answer. 
2) Display questions by category.
3) Delete questions.
4) Add new questions and answer. 
5) Search for questions based on a text.
6) Play the quiz game, randomizing questions either all questions or within a specific category, play up to five questions of the chosen category. If there are fewer than five questions in a category, the game will end when there are no more questions in that category.


### Backend directory

The `./backend` directory contains a completed Flask and SQLAlchemy server. 


### Frontend directory

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server.



## Getting Started

### Backend Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### PIP Dependencies

Install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.


#### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


#### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```bash
dropdb trivia
createdb trivia
psql trivia < trivia.psql
```

#### Running the server

From within the `backend` directory first ensure you are working using your created virtual environment. Base URL is: http://127.0.0.1:5000/

To run the server naviging to the `/backend` directory, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 


### Frontend Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).


#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>_tip_: **npm i** is shorthand for **npm install**


#### Running Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```




## Errors

`todo` response code , messages , error type

### Testing
To run the tests naviging to the `/backend` directory and running:
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## API Endpoints 

List of all endpoints in the project:

1. GET '/categories'
2. GET '/questions'
3. DELETE '/questions/<int:question_id>'
4. POST '/questions'
5. POST '/questions/search'
6. GET '/categories/<int:category_id>/questions'
7. POST '/quizzes'


### 1. GET '/categories'

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id:
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 

```

### 2. GET '/questions'
### 3. DELETE '/questions/<int:question_id>'
### 4. POST '/questions'
### 5. POST '/questions/search'
### 6. GET '/categories/<int:category_id>/questions'
### 7. POST '/quizzes'



## Authors
`todo`

## Acknowledgements
`todo`


