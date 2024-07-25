from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()

KEY_WEATHER = os.getenv('Openweather_Key')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
SECRET = os.environ.get('SECRET')
