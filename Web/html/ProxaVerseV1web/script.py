
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')
    
    if password == "user":
        response = {'message': 'Correct'}
        return jsonify(response), 200
    else:
        response = {'message': 'Incorrect'}
        return jsonify(response), 400

if __name__ == '__main__':
    app.run()
 