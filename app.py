from flask import Flask, jsonify
from bd import carros  

app = Flask(__name__)  

@app.route('/carros', methods=['GET'])  
def get_carros():
    return jsonify(carros)  

if __name__ == '__main__':  
    app.run(debug=True)  