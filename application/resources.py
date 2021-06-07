from marshmallow import Schema, fields, EXCLUDE, post_load
from application.exceptions import BadRequestBody


class MovieSchema(Schema):
    movie_id = fields.Int(data_key='movieId')
    title = fields.Str(data_key='title')
    movie_format = fields.Str(data_key='movieFormat')
    length = fields.Int(data_key='length')
    release_date = fields.Int(data_key='releaseDate')
    rating = fields.Int(data_key='rating')

    @post_load
    def check_restrictions(self, data, **kwargs):
        if data.get('length') and not 500 > data['length'] > 0:
            raise BadRequestBody(message=f"length is formatted incorrectly. Needs to be between 0-500 but {data['length']} was sent.")
        elif data.get('release_date') and not 2100 > data['release_date'] > 1800:
            raise BadRequestBody(message=f"releaseDate is formatted incorrectly. Needs to be between 1800-2100 but {data['release_date']} was sent.")
        elif data.get('rating') and not 5 >= data['rating'] >= 1:
            raise BadRequestBody(message=f"rating is formatted incorrectly. Needs to be between 1-5 but {data['rating']} was sent.")
        
        return data

    class Meta:
        unknown = EXCLUDE
