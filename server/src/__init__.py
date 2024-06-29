from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
import json
from flask_cors import CORS
from src.config import config_dict
from src.database import close_conn
from src.main import book_bp


def create_app(config: str) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_dict[config])

    # enable CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.route("/api/<int:id>")
    def index(id):
        return jsonify({"message": f"Hello this is the id: {id}"})

    # register the blueprints
    app.register_blueprint(book_bp)

    # handle any exceptions
    @app.errorhandler(HTTPException)
    def handle_exceptions(error):
        response = error.get_response()
        response.data = json.dumps(
            {
                "status code": error.code,
                "name": error.name,
                "description": error.description,
            }
        )
        response.content_type = "application/json"
        return response

    @app.teardown_appcontext
    def close_connection(exception):
        close_conn()

    return app
