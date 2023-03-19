from flask import Flask
from flask_cors import CORS
from embedding_based_cf import CF_bp

app = Flask(__name__)   
cors = CORS(app)

app.register_blueprint(CF_bp)

if __name__ == '__main__':
    app.run(port=5000, debug=True)