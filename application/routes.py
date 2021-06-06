from flask import make_response, jsonify
from flask import request
from application import flask_app, db
from application.models import Movie
from application.resources import MovieSchema
from application.binders import create_from_resource, update_from_resource


@flask_app.route('/', methods=['GET'])
def healthy():
    return '<h1>Movie service is online.</h1>'


@flask_app.route('/movie', methods=['GET'])
def get_movies():
    """
    Gets a list of all movies in Movie table from the database
    """
    print('Ok')
    response = Movie.query.all()
    print('good')
    result = MovieSchema(many=True).dump(response)
    return {'movies': result}, 200


@flask_app.route('/movie', methods=['POST'])
def add_movie(movie_id):
    """
    Adds a movie to the database
    """
    resource_data = request.get_json(force=True)
    movie_resource = MovieSchema().load(resource_data)
    movie_object = create_from_resource(Movie, movie_resource)
    
    db.session.add(movie_object)
    db.session.commit()

    response = MovieSchema().dump(movie_object)
    return {'movie': response}, 201


@flask_app.route('/movie/<movie_id>', methods=['PATCH'])
def update_movie(movie_id):
    """
    Adds a movie to the database
    """
    resource_data = request.json
    movie_resource = MovieSchema().load(resource_data)

    # Check if movie exists in db
    old_movie = Movie.query.filter(Movie.movie_id == movie_id).one_or_none()
    if not old_movie:
        return {'Error': f'The movie with id: {movie_id} does not exists in the database.'}, 409

    update_from_resource(old_movie, movie_resource)

    db.session.commit()

    response = MovieSchema().dump(old_movie)
    return {'movie': response}, 201


@flask_app.route('/movie/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    Movie.query.filter(Movie.movie_id == movie_id).delete()

    db.session.commit()
    return {'Message': f'Movie with id: {movie_id} has been deleted.'}, 200
