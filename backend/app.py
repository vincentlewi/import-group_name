from flask import Flask
from flask_cors import CORS
from movie import movie_bp
from cb_kev import cb_kev_bp
from cb_kev_multi import cb_kev_multi_bp
from combo import combo_bp

app = Flask(__name__)   
cors = CORS(app)

app.register_blueprint(movie_bp)
app.register_blueprint(cb_kev_bp)
app.register_blueprint(cb_kev_multi_bp)
# app.register_blueprint(combo_bp)

if __name__ == '__main__':
    app.run(port=5000, debug=True)