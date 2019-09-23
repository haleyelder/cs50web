import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
DATABASE_URL = "postgresql://postgres:admin@localhost/books"

#postgres://skqoscfvpasiyb:51c91e71d1661887d091d96832e1f9a4ad7a4be420c174d7de8f166e30345973@ec2-54-225-200-15.compute-1.amazonaws.com:5432/dbrogbvguiop8l



# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"
