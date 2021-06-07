Project Instructions

Build a service with a database backend for storing and editing a movie collection. Please use a technology stack of your choosing to deliver the application, though use of 
AWS infrastructure is recommended.
  1. Start by briefly documenting the technology stack of your choosing. Let us know whatcomponent you’ve chosen for each layer and why.
  2. Setup a source code repository and share it with us. GitHub or Bitbucket are fine.
  3. You’ll need to deploy your application to a hosting service of your choosing (AWS, DigitalOcean, Azure, etc). Free tiers should be sufficient.
Requirements
  1. The service must create, list, update, and delete movies in the collection.
  2. Each movie in the collection needs the following attributes:
    a. Title [text; length between 1 and 50 characters]
    b. Format [text; allowable values “VHS”, “DVD”, “Streaming”]
    c. Length [time; value between 0 and 500 minutes]
    d. Release Year [integer; value between 1800 and 2100]
    e. Rating [integer; value between 1 and 5]
  3. The service must be accessible over http. You can implement an API, a command line interface (curl, node, etc.) and/or a basic web-based GUI.
  4. Add an authentication method to restrict access to the service.
  
 
 Stack:
  Python
  Sqlalchemy
  Flase
  Postgresql
  AWS RDS
  AWS EC2
  NGINX

All endpoints can be tested with Postman or whatever you like to use for http requests

Endpoints: prefix = 'http://3.21.28.137'
  GET: '/movie' Will return a list of all movies in the database
  POST: '/movie' Will persist a movie to the database with above restrictions
    example requestBody: {
                            'title': 'some title',
                            'movieFormat': 'VHS',
                            'length': 120,
                            'releaseYear': 1999,
                            'rating': 2
                         }
  PATCH: '/movie/:movie_id' Will update any movie given it's movie_id
    example: '/movie/1'
      {
        'title': 'new title'
      }
  DELETE: '/movie/:movie_id' Will delete a movie from the database with the matching movie_id if it exists

This is hosted on an EC2 instance linux free tier and with NGINX running as a reverse proxy all HTTP traffic is routed to the flask application. This
isn't necessarilly how I would deploy a production application, but it will do for a quick weekend homework project. I also spun up a PostgreSQL database
in an AWS RDS instance that all of the data is being stored in. You can see my quick table creation script in this repo. The table doesn't control restrictions
such as a release year between 1800-2100 instead I decided to do that during serialization with marshmallow. So if you look in resources.py you can see that
I am doing checks there to make sure the request body format and data are accurate. Typically those requirements would be in the table definition as well, but
I like to catch any format issues in the api as I prefer using the orm as the database manipulator and migrator. For my api layer I decided to use Flask as it is
extremely lightweight, installs with no extras so I can control everything that is being used my applition, and it is also super quick to build up a simple api.
SqlAlchemy was my chosen orm as it is what I most familiar with rather then writing a bunch of raw sql executions an orm is always safer and protects from things
like injection.
                    
