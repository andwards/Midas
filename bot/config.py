import os

API_KEY = 'ENTER ALPACA API KEY'
SECRET_KEY = 'ENTER ALPACA SECRET KEY'
BOT_KEY = 'ENTER DISCORD BOT KEY'
OPENAI_KEY = "ENTER OPEN AI KEY"

def initConfig():
    if os.environ.get('API_KEY') is not None:
        API_KEY = os.environ.get('API_KEY')
    if os.environ.get('SECRET_KEY') is not None:
        SECRET_KEY = os.environ.get('SECRET_KEY')
    if os.environ.get('BOT_KEY') is not None:
        BOT_KEY = os.environ.get('BOT_KEY')
    if os.environ.get('OPENAI_KEY') is not None:
        OPENAI_KEY = os.environ.get('OPENAI_KEY')
