import os
from dotenv import load_dotenv


load_dotenv()
TEST_URL = os.getenv("TEST_URL")
TEST_USERNAME = os.getenv("TEST_USERNAME")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
