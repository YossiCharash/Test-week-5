from flask import Flask
from routes.accident_route import Accidents



app = Flask(__name__)

app.register_blueprint(Accidents)


if __name__ == '__main__':
    app.run()
