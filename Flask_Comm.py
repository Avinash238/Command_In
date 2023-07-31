from flask import Flask, render_template, request, jsonify
from forex_python.converter import CurrencyRates

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Commit_HTML.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = float(request.form['amount'])

        c = CurrencyRates()
        converted_amount = c.convert(from_currency, to_currency, amount)

        return jsonify({'result': converted_amount})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
