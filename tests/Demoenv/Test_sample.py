from dotenv import load_dotenv
import os
def test_auth():
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username,password)