from marshmallow import Schema, fields, EXCLUDE


class MovieSchema(Schema):
    movie_id = fields.Int(data_key='movieId')
    title = fields.Str(data_key='title')
    movie_format = fields.Str(data_key='movieFormat')
    length = fields.Int(data_key='length')
    release_date = fields.Int(data_key='releaseDate')
    rating = fields.Int(data_key='rating')

    class Meta:
        unknown = EXCLUDE
