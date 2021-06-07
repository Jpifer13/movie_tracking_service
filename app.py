
from config import config
from application import create_app

flask_app = create_app(config)

if __name__ == '__main__':
    flask_app.run()
