def test_getMovies_success(client, movie_data):
    url = '/movie'
    response = client.get(url)
    assert response.status_code == 200
    result = response.json
    assert len(result['movies']) == 1
    assert result['movies'][0]['title'] == 'test_movie'


def test_addMovie_success(client):
    data = {
        "movieId": 1,
        "title": "test post",
        "movieFormat": "DVD",
        "length": 122,
        "releaseDate": 2010,
        "rating": 2
    }
    url = '/movie'
    response = client.post(url, json=data)
    assert response.status_code == 201
    result = response.json
    assert result['title'] == "test post"
    assert result['movieFormat'] == "DVD"
    assert result['length'] == 122
    assert result['releaseDate'] == 2010
    assert result['rating'] == 2


def test_getMovie_success(client, movie_data):
    url = '/movie/1'
    data = {
        'rating': 1
    }
    response = client.patch(url, json=data)
    assert response.status_code == 201
    result = response.json
    assert result['movie']['rating'] == 1


def test_delMovie_success(client, movie_data):
    url = '/movie/1'
    result = client.delete(url)
    assert result.status_code == 200
    movies = client.get('/movie')
    assert len(movies.json['movies']) == 0
