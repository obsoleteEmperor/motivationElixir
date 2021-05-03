#server code to keep our bot running


from flask import Flask            #Python web framework to keep our bot online
from threading import Thread       #Threads to ensure that both the server and our bot runs at the same time

app = Flask('')

@app.route('/')
def home():                        #Displays this to anyone who visits the bot's page
    return "Hello. I am alive! We are in beta testing, expect frequent sudden bot downtime. Cheers, have a good day! \n Motivation Elixir v2.1.1"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()