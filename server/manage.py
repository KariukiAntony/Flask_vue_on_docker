import os 
from flask.cli import FlaskGroup
from src import create_app 

config = os.environ.get("CONFIG")
app = create_app(config)
cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()


