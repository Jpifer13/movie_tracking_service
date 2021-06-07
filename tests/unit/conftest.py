import os
import pytest
import sqlite3
from application import create_app
from application.models import Movie

@pytest.fixture(scope='session')
def client(request):
    os.environ['APP_CONFIG'] = 'testing'
    from config import config
    flask_app = create_app(config)
    context = flask_app.app_context()
    context.push()

    def tear_down():
        context.pop()
    
    request.addfinalizer(tear_down)
    return flask_app.test_client()

@pytest.fixture(scope='function')
def database(client, request):
    client.application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    client.application.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'connect_args': {
            'detect_types': sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
        },
        'native_datetime': False
    }
    from application import db
    db.app = client.application
    db.create_all()

    def tear_down():
        db.drop_all()

    request.addfinalizer(tear_down)
    return db

@pytest.fixture(scope='function')
def movie_data(database):
    test_movie = Movie(
        title='test_movie',
        movie_format='VHS',
        length=120,
        release_date=1999,
        rating=3
    )
    database.session.add(test_movie)
    database.session.commit()
