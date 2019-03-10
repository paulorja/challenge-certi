from flask import Flask, jsonify

from number_to_text.number_to_text import NumberToText

app = Flask(__name__)

@app.route('/<number>')
def show_number_to_text(number):
    parser = NumberToText()
    result = parser.number_to_text(int(number))
    json_result = jsonify({ "extenso": result })
    return json_result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
