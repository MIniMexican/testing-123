import os

SCRIPT = os.path.join(os.path.dirname(__file__), 'app.sh')

os.execl('/bin/bash', 'bash (python -u app.py)', SCRIPT)

Flask==0.10.1

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

input = raw_input('Enter a number:')

if len(input) > 0:
    print ("A number was not entered")
  else times = raw_input ('Enter a number to times the last number by:')
  
answer = input * t
Flask==0.10.1

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

input = raw_input('Enter a number:')

if len(input) > 0:
    print ("A number was not entered")
  else times = raw_input ('Enter a number to times the last number by:')
  
answer = input * times
print answer
  
times
print answer
  
