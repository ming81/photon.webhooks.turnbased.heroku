import os
from flask import Flask, request

import db

app = Flask(__name__)
app.debug = True 
db.set_game_state(1, 2);

@app.route('/')
def hello():
    return 'Hello World 6666!'

from webhooks import GameClose
from webhooks import GameCreate
from webhooks import GameEvent
from webhooks import GameJoin
from webhooks import GameLeave
from webhooks import GameProperties
from webhooks import GetGameList
