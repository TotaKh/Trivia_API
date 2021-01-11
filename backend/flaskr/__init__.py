#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_cors import CORS
import random
from models import setup_db, Question, Category


#----------------------------------------------------------------------------#
# Pagination.
#----------------------------------------------------------------------------#
QUESTIONS_PER_PAGE = 10
# pagination questions (every 10 questions in a page).
def paginate(request, questions):
  page = request.args.get('page', 1, type=int)
  start =  (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  formated = [question.format() for question in questions]
  current_questions = formated [start:end]
  return current_questions


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  # Set up CORS. Allow '*' for origins.
  CORS(app , resources={"/": {"origins": "*"}})

  # Use the after_request decorator to set Access-Control-Allow
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization ,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, OPTIONS, DELETE')
    return response

  #----------------------------------------------------------------------------#
  # Endpoint.
  #----------------------------------------------------------------------------#
  @app.route('/categories')
  def get_Categories():
    ''' 
    GET for all available categories.
    '''
    categories = Category.query.order_by(Category.id).all()
    
    if categories == 0:
      abort(404)

    return jsonify({
      'success': True,
      'categories': {category.id: category.type for category in categories}
    })
  

 
  @app.route('/questions')
  def get_Questions():
    '''
    GET for all available questions return a list of questions, 
    number of total questions, current category, categories.
    '''
    questions = Question.query.order_by(Question.id).all()
    paginate_questions = paginate(request, questions)
    
    if len(paginate_questions) == 0:
      abort(404)

    categories = Category.query.order_by(Category.type).all()

    return jsonify({
      'success': True,
      'questions': paginate_questions,
      'total_questions': len(questions),
      'categories': {category.id: category.type for category in categories},
      'current_category': None
    })

  
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    '''
    An endpoint to DELETE question using a question ID. 
    '''
    question = Question.query.filter(Question.id == question_id).one_or_none()
    if question is None:
      abort(422)
    
    question.delete()

    return jsonify({
      'success': True,  
      'deleted': question_id    
    })
    

  @app.route("/questions", methods=['POST'])
  def add_question():
    '''
    POST endpoint to craete new question which will require 
    the question and answer text, category, and difficulty score.
    '''
    
    body = request.get_json()

    new_question = body.get('question')
    new_answer = body.get('answer')
    new_difficulty = body.get('difficulty')
    new_category = body.get('category')

    if (new_question == '') or (new_answer == ''):
      abort(422)

    try:
      question = Question(question=new_question, answer=new_answer,
        difficulty=new_difficulty, category=new_category)
      question.insert()

      return jsonify({
        'success': True,
        'created': question.id,
      })

    except:
      abort(422)


  @app.route('/questions/search', methods=['POST'])
  def search():
    '''
    POST endpoint to get questions based on a search term,
    return any questions for whom the search term is a substring of the question.
    '''
    data = request.get_json()
    searchTerm = data.get('searchTerm','')
    if searchTerm == '':
      abort(422)
    
    questions = Question.query.filter( Question.question.ilike( f'%{searchTerm}%') ).all()
    paginate_questions = paginate(request,questions)
    if len(paginate_questions) == 0:
      abort(404)
    
    return jsonify({
      'success': True,
      'questions': paginate_questions,
      'total_questions': len(questions)
    })

    
  @app.route('/categories/<int:category_id>/questions')
  def questions_by_category(category_id):
    '''
    GET endpoint to get questions based on category id.
    '''
    questions = Question.query.filter( Question.category == category_id ).all()
    paginate_questions = paginate(request,questions)
    
    if len(paginate_questions) == 0 :
      abort(404)
    
    return jsonify ({
      'success': True,
      'questions': paginate_questions
      })


  @app.route("/quizzes", methods=['POST'])
  def quiz():
    '''
    POST endpoint to get questions to play the quiz.
    return a random questions within the given category, 
    if provided, and that is not one of the previous questions.
    '''
    data = request.get_json()
    category = data.get('quiz_category')
    previous = data.get('previous_questions')

    if category is None:
      abort(400)
    elif category['id'] == 0:
      questions = Question.query.order_by(func.random()).all()
    else :
      questions = Question.query.filter_by(category=category['id']).order_by(func.random()).all()
      
    quiz_question = ''

    for question in questions:
      if question.id not in previous:
        quiz_question = question.format()
        break

    return jsonify ({
      'success': True,
      'question': quiz_question
    })
    

  #----------------------------------------------------------------------------#
  # Error Handlers.
  #----------------------------------------------------------------------------#
  
  @app.errorhandler(400)
  def Bad_Request(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message': "Bad Request"
    }),400

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': "resource not found"
    }),404

  @app.errorhandler(405)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 405,
      'message': "method not allowed"
    }),405

  @app.errorhandler(422)
  def Unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': "unprocessable"
    }),422

    @app.errorhandler(Exception)
    def exception_handler(error):
      return jsonify({
        'success': False,
        'error': 500,
        'message': "Something went wrong"
      }), 500


  
  return app

    