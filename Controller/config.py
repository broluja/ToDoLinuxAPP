"""Config file for Database and Mail."""

import os
from dotenv import load_dotenv

load_dotenv()

# DB Settings
DATABASE_NAME = os.getenv("DATABASE_NAME", "LinuxTodo")
DATABASE_USER = os.getenv("DATABASE_USER", "root")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "root")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")

# Mail Settings
MAIL_API_KEY = os.getenv('KEY')
MAIL_SECRET_KEY = os.getenv('SECRET')
HOST_EMAIL = os.getenv('FROM')
