from flask import Flask, json, abort
import csv

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return '<h3>Example URL to create query: 127.0.0.1:5000/flights/2 <h3>'


@app.route('/flights/<flight_id>', methods=['GET'])
def flights(flight_id):
    with open('flights.csv') as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            if row[0] == flight_id:
                data = {
                    'ArrivalTime': row[6],
                    'DepartureTime': row[4],
                    'Number': row[7]
                }
                return json.dumps(data)
        abort(404)


if __name__ == '__main__':
    app.run()
